import re
from typing import Dict, List, Tuple
from pulp import LpProblem, LpVariable, LpMaximize, LpMinimize, LpStatus, value

def parse_objective(s: str) -> Tuple[str, List[float]]:
    s_lower = s.lower().strip()
    opt_type = 'max' if 'max' in s_lower else 'min'
    if '=' not in s:
        raise ValueError("La función objetivo debe contener '='")
    expr = s.split('=')[1].strip().replace(' ', '').lower()
    variables = re.findall(r'x\d+', expr)
    if not variables:
        raise ValueError("No se encontraron variables")
    n_vars = max(int(v[1:]) for v in variables)
    if expr[0] not in ['+', '-']:
        expr = '+' + expr
    coef_dict = {}
    pattern = r'([+-]?\d*\.?\d*)x(\d+)'
    for coef_str, var_num in re.findall(pattern, expr):
        var_num = int(var_num)
        if coef_str in ['', '+']:
            coef = 1.0
        elif coef_str == '-':
            coef = -1.0
        else:
            coef = float(coef_str)
        coef_dict[var_num] = coef_dict.get(var_num, 0.0) + coef
    coefficients = [coef_dict.get(i, 0.0) for i in range(1, n_vars + 1)]
    return opt_type, coefficients

def parse_constraint(s: str, n_vars: int) -> Tuple[List[float], str, float]:
    if '<=' in s:
        op, parts = '<=', s.split('<=')
    elif '>=' in s:
        op, parts = '>=', s.split('>=')
    elif '=' in s:
        op, parts = '=', s.split('=')
    else:
        raise ValueError(f"No se encontró operador en: {s}")
    lhs, rhs = parts[0].strip(), parts[1].strip()
    rhs_value = float(rhs)
    lhs_clean = lhs.replace(' ', '').lower()
    if lhs_clean[0] not in ['+', '-']:
        lhs_clean = '+' + lhs_clean
    coef_dict = {}
    pattern = r'([+-]?\d*\.?\d*)x(\d+)'
    for coef_str, var_num in re.findall(pattern, lhs_clean):
        var_num = int(var_num)
        if coef_str in ['', '+']:
            coef = 1.0
        elif coef_str == '-':
            coef = -1.0
        else:
            coef = float(coef_str)
        coef_dict[var_num] = coef_dict.get(var_num, 0.0) + coef
    coefficients = [coef_dict.get(i, 0.0) for i in range(1, n_vars + 1)]
    return coefficients, op, rhs_value

def solve_simplex(objective_str: str, constraints_list: List[str]) -> Dict:
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
        prob = LpProblem("Simplex", sense)
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
            return {'success': True, 'status': 'optimal', 'optimal_value': round(value(prob.objective), 4), 'solution': solution, 'opt_type': opt_type, 'method': 'Simplex'}
        elif status == 'Infeasible':
            return {'success': False, 'status': 'infeasible', 'error': 'El problema no tiene solución factible.'}
        elif status == 'Unbounded':
            return {'success': False, 'status': 'unbounded', 'error': 'La solución es no acotada.'}
        else:
            return {'success': False, 'status': 'error', 'error': f'Estado del solver: {status}'}
    except Exception as e:
        return {'success': False, 'status': 'error', 'error': f'Error: {str(e)}'}
