"""
Implementación Completa del Método Simplex con Tableau
Soporta MAX y MIN, con Método de Dos Fases para variables artificiales
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
import re


class SimplexTableau:
    EPS = 1e-9  # Tolerancia para comparaciones numéricas
    
    def __init__(self, c: List[float], A: List[List[float]], b: List[float], 
                 constraint_types: List[str], opt_type: str = 'max'):
        """
        Inicializa el problema de programación lineal
        
        Args:
            c: Coeficientes de la función objetivo
            A: Matriz de coeficientes de restricciones
            b: Vector de términos independientes
            constraint_types: Lista de tipos ['<=', '>=', '=']
            opt_type: 'max' o 'min'
        """
        self.opt_type = opt_type.lower()
        self.original_opt_type = self.opt_type
        self.n_original_vars = len(c)
        self.n_constraints = len(b)
        self.c_original = c.copy()
        
        # Convertir MIN a MAX internamente
        if self.opt_type == 'min':
            c = [-ci for ci in c]
            self.opt_type = 'max'  # Trabajamos internamente como maximización
        
        # Contador de variables
        self.n_slack = 0      # Variables de holgura
        self.n_surplus = 0    # Variables de exceso
        self.n_artificial = 0 # Variables artificiales
        
        # Construir tableau con variables de holgura/exceso/artificiales
        self.tableau, self.basic_vars, self.artificial_vars = self._build_initial_tableau(
            c, A, b, constraint_types
        )
        
        # Historial de iteraciones
        self.iterations = []
        self.current_iteration = 0
        self.phase = 1 if self.n_artificial > 0 else 2
        
        # Guardar estado inicial
        self._save_iteration(None, None, None, None, 
                           f"Tableau Inicial - {'Fase I' if self.phase == 1 else 'Fase II'}")
    
    def _build_initial_tableau(self, c: List[float], A: List[List[float]], 
                               b: List[float], constraint_types: List[str]) -> Tuple:
        """Construye el tableau inicial con todas las variables necesarias"""
        tableau_rows = []
        basic_vars = []
        artificial_vars = []
        
        # Determinar cuántas variables de cada tipo necesitamos
        for ct in constraint_types:
            if ct == '<=':
                self.n_slack += 1
            elif ct == '>=':
                self.n_surplus += 1
                self.n_artificial += 1
            elif ct == '=':
                self.n_artificial += 1
        
        total_vars = self.n_original_vars + self.n_slack + self.n_surplus + self.n_artificial
        
        # Construir filas de restricciones
        slack_idx = 0
        surplus_idx = 0
        artificial_idx = 0
        
        for i in range(self.n_constraints):
            row = A[i].copy()
            
            # Agregar variables de holgura (todas como ceros inicialmente)
            for _ in range(self.n_slack):
                row.append(0.0)
            
            # Agregar variables de exceso (todas como ceros inicialmente)
            for _ in range(self.n_surplus):
                row.append(0.0)
            
            # Agregar variables artificiales (todas como ceros inicialmente)
            for _ in range(self.n_artificial):
                row.append(0.0)
            
            # Configurar la variable específica para esta restricción
            if constraint_types[i] == '<=':
                # Variable de holgura
                row[self.n_original_vars + slack_idx] = 1.0
                basic_vars.append(self.n_original_vars + slack_idx)
                slack_idx += 1
            elif constraint_types[i] == '>=':
                # Variable de exceso (negativa) y artificial (positiva)
                row[self.n_original_vars + self.n_slack + surplus_idx] = -1.0
                row[self.n_original_vars + self.n_slack + self.n_surplus + artificial_idx] = 1.0
                basic_vars.append(self.n_original_vars + self.n_slack + self.n_surplus + artificial_idx)
                artificial_vars.append(self.n_original_vars + self.n_slack + self.n_surplus + artificial_idx)
                surplus_idx += 1
                artificial_idx += 1
            elif constraint_types[i] == '=':
                # Solo variable artificial
                row[self.n_original_vars + self.n_slack + self.n_surplus + artificial_idx] = 1.0
                basic_vars.append(self.n_original_vars + self.n_slack + self.n_surplus + artificial_idx)
                artificial_vars.append(self.n_original_vars + self.n_slack + self.n_surplus + artificial_idx)
                artificial_idx += 1
            
            row.append(b[i])  # RHS
            tableau_rows.append(row)
        
        # Fila Z
        if self.n_artificial > 0:
            # Fase I: Minimizar suma de artificiales (convertido a MAX)
            z_row = [0.0] * total_vars
            for ai in artificial_vars:
                z_row[ai] = -1.0  # Queremos maximizar -A (minimizar A)
        else:
            # Fase II directa: usar función objetivo original
            z_row = [-ci for ci in c]  # MAX
            z_row.extend([0.0] * (self.n_slack + self.n_surplus + self.n_artificial))
        
        z_row.append(0.0)  # Valor inicial de Z
        tableau_rows.append(z_row)
        
        tableau = np.array(tableau_rows, dtype=float)
        
        # Si tenemos artificiales, hacer la fila Z dual factible
        if self.n_artificial > 0:
            for i in range(self.n_constraints):
                if basic_vars[i] in artificial_vars:
                    # Restar la fila de la variable artificial de la fila Z
                    tableau[-1] = tableau[-1] - tableau[i]
        
        return tableau, basic_vars, artificial_vars
    
    def _save_iteration(self, pivot_col: Optional[int], pivot_row: Optional[int],
                       entering_var: Optional[int], leaving_var: Optional[int],
                       operation: str):
        """Guarda el estado actual del tableau"""
        # Verificar optimalidad
        z_row = self.tableau[-1, :-1]
        is_optimal = all(z_row >= -self.EPS)
        
        # Valor objetivo actual
        z_value = self.tableau[-1, -1]
        
        # Ajustar según fase y tipo de optimización
        if self.phase == 2:
            if self.original_opt_type == 'min':
                objective_value = -z_value  # Convertir de MAX a MIN
            else:
                objective_value = z_value
        else:
            objective_value = z_value  # En Fase I, mostrar el valor directo
        
        # Formatear nombres de variables
        entering_var_name = self._format_var_name(entering_var) if entering_var is not None else None
        leaving_var_name = self._format_var_name(leaving_var) if leaving_var is not None else None
        
        iteration_data = {
            'iteration': self.current_iteration,
            'description': operation,
            'tableau': self.tableau.copy(),
            'basic_vars': self.basic_vars.copy(),
            'pivot_col': pivot_col,
            'pivot_row': pivot_row,
            'entering_var': entering_var_name,
            'leaving_var': leaving_var_name,
            'operation': operation,
            'objective_value': round(objective_value, 4),
            'is_optimal': is_optimal,
            'z_value': round(z_value, 4),
            'phase': self.phase,
            'tableau_info': {
                'n_rows': self.n_constraints,
                'n_cols': self.tableau.shape[1] - 1,
                'basic_vars': [self._format_var_name(bv) for bv in self.basic_vars]
            },
            'pivot_info': {
                'row': pivot_row,
                'col': pivot_col,
                'element': round(float(self.tableau[pivot_row, pivot_col]), 4)
            } if pivot_row is not None and pivot_col is not None else None
        }
        self.iterations.append(iteration_data)
    
    def _format_var_name(self, var_idx: int) -> str:
        """Formatea el nombre de una variable según su índice"""
        if var_idx < self.n_original_vars:
            return f'x{var_idx + 1}'
        elif var_idx < self.n_original_vars + self.n_slack:
            return f'S{var_idx - self.n_original_vars + 1}'
        elif var_idx < self.n_original_vars + self.n_slack + self.n_surplus:
            return f'E{var_idx - self.n_original_vars - self.n_slack + 1}'
        else:
            return f'A{var_idx - self.n_original_vars - self.n_slack - self.n_surplus + 1}'
    
    def _find_pivot_column(self) -> Optional[int]:
        """Encuentra la columna pivote (Bland's Rule: menor índice con valor negativo)"""
        z_row = self.tableau[-1, :-1]
        
        # Buscar valores negativos (queremos maximizar)
        negative_indices = []
        for i in range(len(z_row)):
            if z_row[i] < -self.EPS:
                # En Fase I, NO permitir que variables artificiales entren a la base
                if self.phase == 1 and i in self.artificial_vars:
                    continue
                negative_indices.append(i)
        
        if not negative_indices:
            return None  # Óptimo alcanzado
        
        # Bland's Rule: elegir el índice menor
        return min(negative_indices)
    
    def _find_pivot_row(self, pivot_col: int) -> Optional[int]:
        """Encuentra la fila pivote usando el ratio mínimo (Bland's Rule en empates)"""
        min_ratio = float('inf')
        pivot_row = None
        
        for i in range(self.n_constraints):
            denominator = self.tableau[i, pivot_col]
            if denominator > self.EPS:
                ratio = self.tableau[i, -1] / denominator
                if ratio >= -self.EPS:  # Ratio no negativo
                    if ratio < min_ratio - self.EPS:
                        min_ratio = ratio
                        pivot_row = i
                    elif abs(ratio - min_ratio) < self.EPS:
                        # Empate: Bland's Rule (menor índice de variable básica)
                        if pivot_row is None or self.basic_vars[i] < self.basic_vars[pivot_row]:
                            pivot_row = i
        
        return pivot_row
    
    def _pivot_operation(self, pivot_row: int, pivot_col: int) -> str:
        """Realiza la operación de pivoteo"""
        pivot_element = self.tableau[pivot_row, pivot_col]
        operations = []
        
        # 1. Dividir fila pivote
        if abs(pivot_element - 1.0) > self.EPS:
            operations.append(f"F{pivot_row + 1} = F{pivot_row + 1} / {pivot_element:.4g}")
            self.tableau[pivot_row] = self.tableau[pivot_row] / pivot_element
        
        # 2. Hacer ceros en el resto de la columna
        for i in range(len(self.tableau)):
            if i != pivot_row:
                multiplier = self.tableau[i, pivot_col]
                if abs(multiplier) > self.EPS:
                    row_name = f"F{i + 1}" if i < self.n_constraints else "FZ"
                    pivot_row_name = f"F{pivot_row + 1}"
                    
                    if multiplier > 0:
                        operations.append(f"{row_name} = {row_name} - {multiplier:.4g} × {pivot_row_name}")
                    else:
                        operations.append(f"{row_name} = {row_name} + {abs(multiplier):.4g} × {pivot_row_name}")
                    
                    self.tableau[i] = self.tableau[i] - multiplier * self.tableau[pivot_row]
        
        return " | ".join(operations)
    
    def solve(self, max_iterations: int = 100) -> Dict:
        """Resuelve el problema usando Simplex (con Dos Fases si es necesario)"""
        try:
            # FASE I: Eliminar variables artificiales
            if self.phase == 1:
                for iteration in range(max_iterations):
                    pivot_col = self._find_pivot_column()
                    
                    if pivot_col is None:
                        # Verificar si todas las artificiales salieron de la base
                        artificial_in_basis = any(bv in self.artificial_vars for bv in self.basic_vars)
                        
                        if artificial_in_basis or abs(self.tableau[-1, -1]) > self.EPS:
                            # Problema infactible
                            return self._build_solution('infeasible', 
                                "El problema no tiene solución factible (artificiales en base con valor no cero)")
                        
                        # Fase I completada, pasar a Fase II
                        self._transition_to_phase_ii()
                        break
                    
                    pivot_row = self._find_pivot_row(pivot_col)
                    
                    if pivot_row is None:
                        return self._build_solution('unbounded', "Problema no acotado en Fase I")
                    
                    # Realizar pivoteo
                    entering_var = pivot_col
                    leaving_var = self.basic_vars[pivot_row]
                    operations = self._pivot_operation(pivot_row, pivot_col)
                    self.basic_vars[pivot_row] = entering_var
                    
                    self.current_iteration += 1
                    self._save_iteration(pivot_col, pivot_row, entering_var, leaving_var, 
                                       f"Fase I - {operations}")
                
                if self.phase == 1:
                    return self._build_solution('max_iterations', "Máximo de iteraciones en Fase I")
            
            # FASE II: Optimizar función objetivo original
            for iteration in range(max_iterations):
                pivot_col = self._find_pivot_column()
                
                if pivot_col is None:
                    return self._build_solution('optimal')
                
                pivot_row = self._find_pivot_row(pivot_col)
                
                if pivot_row is None:
                    return self._build_solution('unbounded', "Problema no acotado")
                
                # Realizar pivoteo
                entering_var = pivot_col
                leaving_var = self.basic_vars[pivot_row]
                operations = self._pivot_operation(pivot_row, pivot_col)
                self.basic_vars[pivot_row] = entering_var
                
                self.current_iteration += 1
                phase_label = "Fase II" if self.n_artificial > 0 else "Simplex"
                self._save_iteration(pivot_col, pivot_row, entering_var, leaving_var,
                                   f"{phase_label} - {operations}")
            
            return self._build_solution('max_iterations', "Máximo de iteraciones alcanzado")
        
        except Exception as e:
            return {
                'success': False,
                'status': 'error',
                'error': f'Error durante la ejecución del Simplex: {str(e)}'
            }
    
    def _transition_to_phase_ii(self):
        """Transición de Fase I a Fase II"""
        self.phase = 2
        
        # Reemplazar fila Z con la función objetivo original
        c = self.c_original if self.original_opt_type == 'min' else [-ci for ci in self.c_original]
        
        # Construir Z-row: solo variables originales tienen costos
        z_row = [-ci for ci in c]  # MAX de variables originales
        # Todas las demás variables (holgura, exceso, artificiales) tienen coeficiente 0
        total_additional = self.n_slack + self.n_surplus + self.n_artificial
        z_row.extend([0.0] * total_additional)
        z_row.append(0.0)  # RHS
        
        self.tableau[-1] = np.array(z_row)
        
        # Hacer la fila Z dual factible respecto a las variables básicas ORIGINALES
        # Solo ajustamos si una variable básica es original (x1, x2, ...) y tiene coeficiente no-cero en Z
        for i in range(self.n_constraints):
            bv = self.basic_vars[i]
            # Solo ajustar para variables originales en la base
            if bv < self.n_original_vars:
                if abs(self.tableau[-1, bv]) > self.EPS:
                    multiplier = self.tableau[-1, bv]
                    self.tableau[-1] = self.tableau[-1] - multiplier * self.tableau[i]
        
        # IMPORTANTE: Forzar a 0 los coeficientes de variables de exceso y artificiales
        # Estas variables no deben entrar a la base en Fase II
        start_idx = self.n_original_vars + self.n_slack
        end_idx = start_idx + self.n_surplus + self.n_artificial
        for j in range(start_idx, end_idx):
            self.tableau[-1, j] = 0.0
        
        self.current_iteration += 1
        self._save_iteration(None, None, None, None, "Transición a Fase II - Función objetivo restaurada")
    
    def _build_solution(self, status: str, error_msg: str = None) -> Dict:
        """Construye el diccionario de solución"""
        if status == 'optimal':
            solution = {}
            for i in range(self.n_original_vars):
                if i in self.basic_vars:
                    row_idx = self.basic_vars.index(i)
                    value = self.tableau[row_idx, -1]
                    solution[f'x{i + 1}'] = round(float(value), 4)
                else:
                    solution[f'x{i + 1}'] = 0.0
            
            z_value = self.tableau[-1, -1]
            if self.original_opt_type == 'min':
                # Para MIN, el RHS de Z-row después de hacer dual-factible
                # representa directamente el valor óptimo (positivo)
                optimal_value = z_value
            else:
                # Para MAX, el RHS es directo
                optimal_value = z_value
            
            return {
                'success': True,
                'status': 'optimal',
                'optimal_value': round(optimal_value, 4),
                'solution': solution,
                'opt_type': self.original_opt_type,
                'iterations': self.iterations,
                'method': 'Simplex con Tableau' + (' (Dos Fases)' if self.n_artificial > 0 else ''),
                'estado_final': 'Óptimo'
            }
        
        elif status == 'infeasible':
            return {
                'success': False,
                'status': 'infeasible',
                'error': error_msg or 'El problema no tiene solución factible',
                'iterations': self.iterations,
                'estado_final': 'Infeasible'
            }
        
        elif status == 'unbounded':
            return {
                'success': False,
                'status': 'unbounded',
                'error': error_msg or 'La solución es no acotada (unbounded)',
                'iterations': self.iterations,
                'estado_final': 'No limitado'
            }
        
        else:
            return {
                'success': False,
                'status': 'error',
                'error': error_msg or 'Error desconocido',
                'iterations': self.iterations,
                'estado_final': 'Error'
            }


def parse_objective(s: str) -> Tuple[str, List[float]]:
    """Parse la función objetivo"""
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
    """Parse una restricción"""
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
    
    # Normalizar: RHS debe ser no negativo
    if rhs_value < 0:
        coefficients = [-c for c in coefficients]
        rhs_value = -rhs_value
        # Invertir operador
        if op == '<=':
            op = '>='
        elif op == '>=':
            op = '<='
    
    return coefficients, op, rhs_value


def solve_simplex_tableau(objective_str: str, constraints_list: List[str]) -> Dict:
    """
    Resuelve un problema de programación lineal usando Simplex con Dos Fases
    """
    try:
        # Parse objetivo
        opt_type, obj_coeffs = parse_objective(objective_str)
        n_vars = len(obj_coeffs)
        
        # Parse restricciones
        A = []
        b = []
        constraint_types = []
        
        for constraint_str in constraints_list:
            constraint_str = constraint_str.strip()
            if not constraint_str or re.match(r'x\d+\s*>=\s*0', constraint_str.lower()):
                continue
            
            try:
                coeffs, op, rhs = parse_constraint(constraint_str, n_vars)
                A.append(coeffs)
                b.append(rhs)
                constraint_types.append(op)
            except Exception:
                continue
        
        if not A:
            return {
                'success': False,
                'status': 'error',
                'error': 'No se encontraron restricciones válidas.'
            }
        
        # Crear y resolver tableau
        tableau = SimplexTableau(obj_coeffs, A, b, constraint_types, opt_type)
        result = tableau.solve()
        
        return result
    
    except Exception as e:
        return {
            'success': False,
            'status': 'error',
            'error': f'Error al procesar el problema: {str(e)}'
        }
