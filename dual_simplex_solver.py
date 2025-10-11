import re
from typing import Dict, List
from simplex_solver import parse_objective, parse_constraint
from pulp import LpProblem, LpVariable, LpMaximize, LpMinimize, LpStatus, value

def solve_dual_simplex(objective_str: str, constraints_list: List[str]) -> Dict:
    try:
        opt_type, obj_coeffs = parse_objective(objective_str)
        n_vars = len(obj_coeffs)
        constraints = []
        for constraint_str in constraints_list:
            constraint_str = constraint_str.strip()
            if not constraint_str or re.match(r'x\d+\s*>=\s*0', constraint_str.lower()):
                continue
            try:
                coeffs, op, rhs = parse_constraint(constraint_str, n_vars)
                constraints.append({'coeffs': coeffs, 'op': op, 'rhs': rhs})
            except Exception as e:
                pass
        if not constraints:
            return {'success': False, 'status': 'error', 'error': 'No se encontraron restricciones válidas.'}
        sense = LpMaximize if opt_type == 'max' else LpMinimize
        prob = LpProblem("Dual_Simplex", sense)
        x = [LpVariable(f'x{i+1}', lowBound=0) for i in range(n_vars)]
        prob += sum(obj_coeffs[i] * x[i] for i in range(n_vars)), "Z"
        for idx, c in enumerate(constraints):
            lhs = sum(c['coeffs'][i] * x[i] for i in range(n_vars))
            if c['op'] == '<=':
                prob += lhs <= c['rhs'], f"R{idx+1}"
            elif c['op'] == '>=':
                prob += lhs >= c['rhs'], f"R{idx+1}"
            else:
                prob += lhs == c['rhs'], f"R{idx+1}"
        prob.solve()
        status = LpStatus[prob.status]
        if status == 'Optimal':
            solution = {}
            for i in range(n_vars):
                val = x[i].varValue
                solution[f'x{i+1}'] = round(val if val is not None else 0.0, 4)
            return {'success': True, 'status': 'optimal', 'optimal_value': round(value(prob.objective), 4), 'solution': solution, 'opt_type': opt_type, 'method': 'Dual Simplex'}
        elif status == 'Infeasible':
            return {'success': False, 'status': 'infeasible', 'error': 'El problema no tiene solución factible.'}
        elif status == 'Unbounded':
            return {'success': False, 'status': 'unbounded', 'error': 'La solución es no acotada.'}
        else:
            return {'success': False, 'status': 'error', 'error': f'Estado del solver: {status}'}
    except Exception as e:
        return {'success': False, 'status': 'error', 'error': f'Error: {str(e)}'}
