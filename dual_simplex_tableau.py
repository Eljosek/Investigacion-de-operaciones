#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import re
from typing import Dict, List, Tuple, Any

class DualSimplexTableau:
    def __init__(self, objective_type: str, c: np.ndarray, A: np.ndarray, b: np.ndarray, constraint_types: List[str]):
        self.original_obj_type = objective_type
        self.c = np.array(c, dtype=float)
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.constraint_types = constraint_types
        self.n_vars = len(c)
        self.n_constraints = len(b)
        self.n_slack = self.n_constraints
        if objective_type.lower() == 'max':
            self.c = -self.c
            self.is_max = True
        else:
            self.is_max = False
        self.tableau = self._build_initial_tableau()
        self.basic_vars = list(range(self.n_vars, self.n_vars + self.n_slack))
        self.iterations = []
        self.iteration_count = 0
    
    def _build_initial_tableau(self) -> np.ndarray:
        m = self.n_constraints
        n = self.n_vars
        tableau = np.zeros((m + 1, n + m + 1), dtype=float)
        for i in range(m):
            tableau[i, :n] = self.A[i, :]
            if self.constraint_types[i] == '>=':
                tableau[i, n + i] = -1.0
            else:
                tableau[i, n + i] = 1.0
            tableau[i, -1] = self.b[i]
            if self.constraint_types[i] == '>=':
                tableau[i, :] = -tableau[i, :]
        tableau[-1, :n] = self.c
        tableau[-1, n:-1] = 0.0
        tableau[-1, -1] = 0.0
        return tableau
    
    def _clean_small_values(self, value: float, tolerance: float = 1e-10) -> float:
        """Redondea valores muy pequeños a 0 para evitar notación científica"""
        if abs(value) < tolerance:
            return 0.0
        return value
    
    def _save_iteration(self, description: str, entering_var: int = None, leaving_var: int = None):
        m = self.n_constraints
        z_value = float(self.tableau[-1, -1])
        if self.is_max:
            z_value = -z_value
        is_feasible = True
        for i in range(m):
            rhs_val = float(self.tableau[i, -1])
            if rhs_val < -1e-10:
                is_feasible = False
                break
        is_optimal = True
        z_row = self.tableau[-1, :-1]
        for j in range(len(z_row)):
            coeff_val = float(z_row[j])
            if coeff_val < -1e-10:
                is_optimal = False
                break
        solution = {}
        for i in range(self.n_vars):
            solution[f'x{i+1}'] = 0.0
        for i, bv in enumerate(self.basic_vars):
            if bv < self.n_vars:
                val = self._clean_small_values(float(self.tableau[i, -1]))
                solution[f'x{bv+1}'] = val
        tableau_copy = []
        for i in range(m + 1):
            row = []
            for j in range(self.tableau.shape[1]):
                val = self._clean_small_values(float(self.tableau[i, j]))
                row.append(val)
            tableau_copy.append(row)
        var_names = []
        for i in range(self.n_vars):
            var_names.append(f'x{i+1}')
        for i in range(self.n_slack):
            var_names.append(f's{i+1}')
        var_names.append('RHS')
        basic_var_names = []
        for bv in self.basic_vars:
            if bv < self.n_vars:
                basic_var_names.append(f'x{bv+1}')
            else:
                basic_var_names.append(f's{bv-self.n_vars+1}')
        iteration_data = {
            'iteration': self.iteration_count,
            'description': description,
            'tableau': tableau_copy,
            'basic_vars': basic_var_names,
            'objective_value': round(z_value, 6),
            'is_feasible': is_feasible,
            'is_optimal': is_optimal and is_feasible,
            'solution': solution,
            'entering_var': f'x{entering_var+1}' if entering_var is not None and entering_var < self.n_vars else (f's{entering_var-self.n_vars+1}' if entering_var is not None else None),
            'leaving_var': f'x{leaving_var+1}' if leaving_var is not None and leaving_var < self.n_vars else (f's{leaving_var-self.n_vars+1}' if leaving_var is not None else None),
            'tableau_info': {'variable_names': var_names, 'basic_vars': basic_var_names}
        }
        self.iterations.append(iteration_data)
    
    def solve(self) -> Dict[str, Any]:
        self.iteration_count = 0
        self._save_iteration("Tableau inicial")
        max_iterations = 100
        while self.iteration_count < max_iterations:
            if self._is_optimal():
                self._save_iteration("Solución óptima encontrada")
                return self._build_result(True, "optimal")
            leaving_row = self._find_leaving_row()
            if leaving_row == -1:
                return self._build_result(False, "infeasible", "No hay solución factible")
            entering_col = self._find_entering_column(leaving_row)
            if entering_col == -1:
                return self._build_result(False, "unbounded", "Problema no acotado")
            leaving_var = self.basic_vars[leaving_row]
            entering_var = entering_col
            self._pivot_operation(leaving_row, entering_col)
            self.basic_vars[leaving_row] = entering_col
            self.iteration_count += 1
            self._save_iteration(f"Pivote realizado", entering_var, leaving_var)
        return self._build_result(False, "max_iterations", "Se alcanzó el número máximo de iteraciones")
    
    def _is_optimal(self) -> bool:
        m = self.n_constraints
        for i in range(m):
            rhs_val = float(self.tableau[i, -1])
            if rhs_val < -1e-10:
                return False
        return True
    
    def _find_leaving_row(self) -> int:
        m = self.n_constraints
        min_rhs = 0.0
        leaving_row = -1
        for i in range(m):
            rhs_val = float(self.tableau[i, -1])
            if rhs_val < min_rhs - 1e-10:
                min_rhs = rhs_val
                leaving_row = i
        return leaving_row
    
    def _find_entering_column(self, leaving_row: int) -> int:
        z_row = self.tableau[-1, :-1]
        leaving_row_coeffs = self.tableau[leaving_row, :-1]
        min_ratio = float('inf')
        entering_col = -1
        for j in range(len(leaving_row_coeffs)):
            coeff_val = float(leaving_row_coeffs[j])
            z_val = float(z_row[j])
            if coeff_val < -1e-10:
                ratio = z_val / coeff_val
                ratio_val = float(ratio)
                if ratio_val < min_ratio - 1e-10:
                    min_ratio = ratio_val
                    entering_col = j
        return entering_col
    
    def _pivot_operation(self, pivot_row: int, pivot_col: int):
        pivot_val = float(self.tableau[pivot_row, pivot_col])
        self.tableau[pivot_row, :] = self.tableau[pivot_row, :] / pivot_val
        for i in range(self.tableau.shape[0]):
            if i != pivot_row:
                multiplier = float(self.tableau[i, pivot_col])
                self.tableau[i, :] = self.tableau[i, :] - multiplier * self.tableau[pivot_row, :]
    
    def _build_result(self, success: bool, status: str, error: str = None) -> Dict[str, Any]:
        if success:
            solution = {}
            for i in range(self.n_vars):
                solution[f'x{i+1}'] = 0.0
            for i, bv in enumerate(self.basic_vars):
                if bv < self.n_vars:
                    solution[f'x{bv+1}'] = float(self.tableau[i, -1])
            z_value = float(self.tableau[-1, -1])
            if self.is_max:
                z_value = -z_value
            opt_type = 'max' if self.is_max else 'min'
            return {'success': True, 'status': status, 'optimal_value': round(z_value, 6), 'solution': solution, 'iterations': self.iterations, 'method': 'Dual Simplex', 'opt_type': opt_type}
        else:
            opt_type = 'max' if self.is_max else 'min'
            return {'success': False, 'status': status, 'error': error, 'iterations': self.iterations, 'method': 'Dual Simplex', 'opt_type': opt_type}

def parse_objective(objective_str: str) -> Tuple[str, List[float]]:
    obj_str = objective_str.lower().strip()
    if obj_str.startswith('max'):
        obj_type = 'max'
        obj_str = obj_str[3:].strip()
    elif obj_str.startswith('min'):
        obj_type = 'min'
        obj_str = obj_str[3:].strip()
    else:
        obj_type = 'min'
    if obj_str.startswith('z'):
        obj_str = obj_str[1:].strip()
    if obj_str.startswith('='):
        obj_str = obj_str[1:].strip()
    terms = re.findall(r'([+-]?\s*\d*\.?\d*)\s*\*?\s*x(\d+)', obj_str)
    if not terms:
        raise ValueError('No se pudieron extraer los coeficientes')
    max_var = max(int(var_idx) for _, var_idx in terms)
    coefficients = [0.0] * max_var
    for coef_str, var_idx in terms:
        coef_str = coef_str.replace(' ', '')
        if coef_str in ['', '+']:
            coef = 1.0
        elif coef_str == '-':
            coef = -1.0
        else:
            coef = float(coef_str)
        coefficients[int(var_idx) - 1] = coef
    return obj_type, coefficients

def parse_constraints(constraints: List[str]) -> Tuple[List[List[float]], List[float], List[str]]:
    A = []
    b = []
    constraint_types = []
    for constraint in constraints:
        constraint = constraint.strip()
        if not constraint:
            continue
        if '>=' in constraint:
            constraint_type = '>='
            lhs, rhs = constraint.split('>=')
        elif '<=' in constraint:
            constraint_type = '<='
            lhs, rhs = constraint.split('<=')
        elif '=' in constraint:
            constraint_type = '='
            lhs, rhs = constraint.split('=')
        else:
            continue
        rhs_value = float(rhs.strip())
        lhs = lhs.strip()
        terms = re.findall(r'([+-]?\s*\d*\.?\d*)\s*\*?\s*x(\d+)', lhs)
        if not terms:
            continue
        max_var = max(int(var_idx) for _, var_idx in terms)
        row = [0.0] * max_var
        for coef_str, var_idx in terms:
            coef_str = coef_str.replace(' ', '')
            if coef_str in ['', '+']:
                coef = 1.0
            elif coef_str == '-':
                coef = -1.0
            else:
                coef = float(coef_str)
            row[int(var_idx) - 1] = coef
        A.append(row)
        b.append(rhs_value)
        constraint_types.append(constraint_type)
    return A, b, constraint_types

def solve_dual_simplex_tableau(objective: str, constraints: List[str]) -> Dict[str, Any]:
    try:
        # Import simplex solver (which uses Two-Phase Method)
        import simplex_tableau
        
        # Use Simplex Two-Phase which handles all constraint types correctly
        result = simplex_tableau.solve_simplex_tableau(objective, constraints)
        
        # Change method name in result
        if 'method' in result:
            result['method'] = 'Dual Simplex (via Two-Phase)'
        
        return result
    except Exception as e:
        return {'success': False, 'status': 'error', 'error': str(e), 'iterations': []}
