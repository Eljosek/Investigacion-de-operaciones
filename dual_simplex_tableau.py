"""
Implementación del Método Dual Simplex con Tableau
Genera visualización paso a paso con todas las iteraciones
Versión: 2.0.1 - Bug fix NumPy arrays
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
import re


class DualSimplexTableau:
    def __init__(self, c: List[float], A: List[List[float]], b: List[float], opt_type: str = 'min'):
        """
        Inicializa el problema de programación lineal para Dual Simplex
        
        Args:
            c: Coeficientes de la función objetivo
            A: Matriz de coeficientes de restricciones
            b: Vector de términos independientes
            opt_type: 'max' o 'min'
        
        Nota: El método Dual Simplex trabaja mejor con problemas de minimización
        con restricciones >= que se convierten a <= multiplicando por -1
        """
        self.opt_type = opt_type.lower()
        self.n_vars = len(c)
        self.n_constraints = len(b)
        
        self.c_original = c.copy()
        
        # Variables de holgura/exceso
        self.slack_vars = list(range(self.n_vars, self.n_vars + self.n_constraints))
        
        # Construir tableau inicial
        # Para Dual Simplex, necesitamos forma estándar con variables de holgura
        self.tableau = []
        for i in range(self.n_constraints):
            row = A[i].copy()
            # Agregar variables de holgura
            slack = [0] * self.n_constraints
            slack[i] = 1
            row.extend(slack)
            row.append(b[i])
            self.tableau.append(row)
        
        # Fila objetivo (Z)
        # Para Dual Simplex con restricciones >= convertidas a <=:
        # - MIN: Dual-factibilidad requiere Z-row >= 0, usamos c directamente
        # - MAX: Dual-factibilidad requiere Z-row <= 0, usamos -c
        # IMPORTANTE: Esto es DIFERENTE del Simplex estándar
        if self.opt_type == 'min':
            z_row = c.copy()  # [c1, c2, ...] positivos para dual-factibilidad
        else:
            # Para MAX en Dual-Simplex, queremos Z-row <= 0
            # Usamos coeficientes negativos: [-c1, -c2, ...]
            z_row = [-ci for ci in c]
        
        z_row.extend([0] * self.n_constraints)  # Coeficientes de holgura
        z_row.append(0)  # RHS inicial de Z
        self.tableau.append(z_row)
        
        self.tableau = np.array(self.tableau, dtype=float)
        
        # Variables básicas iniciales
        self.basic_vars = self.slack_vars.copy()
        
        # Historial de iteraciones
        self.iterations = []
        self.current_iteration = 0
        
        # Guardar estado inicial
        self._save_iteration(
            pivot_col=None,
            pivot_row=None,
            entering_var=None,
            leaving_var=None,
            operation="Tableau Inicial - Dual Simplex",
            ratios=None
        )
    
    def _save_iteration(self, pivot_col: Optional[int], pivot_row: Optional[int],
                       entering_var: Optional[int], leaving_var: Optional[int],
                       operation: str, ratios: Optional[List[Tuple[int, float]]] = None):
        """Guarda el estado actual del tableau"""
        # Verificar factibilidad primal (RHS no negativos)
        # IMPORTANTE: Usar np.all() para evitar error de ambigüedad con arrays
        rhs_col = self.tableau[:self.n_constraints, -1]
        is_feasible = np.all(rhs_col >= -1e-10)
        
        # Verificar optimalidad (factibilidad dual)
        # Para Dual Simplex:
        # - MIN: Todos los reduced costs (Zj - Cj) deben ser >= 0
        # - MAX: Todos los reduced costs deben ser <= 0
        z_row = self.tableau[-1, :-1]
        if self.opt_type == 'min':
            is_optimal = is_feasible and np.all(z_row >= -1e-10)
        else:  # MAX
            is_optimal = is_feasible and np.all(z_row <= 1e-10)
        
        # Valor objetivo actual
        # El tableau siempre representa: Z + (costos)*x = RHS
        # Para MIN: Z-row es [c1, c2, ..., valor], entonces Z = -valor
        # Para MAX: Convertimos a MIN -Z, entonces Z-row es [-c1, -c2, ..., valor], y Z_original = valor
        z_value = self.tableau[-1, -1]
        if self.opt_type == 'min':
            objective_value = round(-z_value, 4)  # MIN: Z = -valor_tableau
        else:
            objective_value = round(z_value, 4)  # MAX: Z_original = valor_tableau (ya es -Z_min)
        
        # Formatear nombres de variables
        entering_var_name = f'x{entering_var+1}' if entering_var is not None and entering_var < self.n_vars else (f'S{entering_var-self.n_vars+1}' if entering_var is not None else None)
        leaving_var_name = f'x{leaving_var+1}' if leaving_var is not None and leaving_var < self.n_vars else (f'S{leaving_var-self.n_vars+1}' if leaving_var is not None else None)
        
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
            'objective_value': objective_value,
            'is_optimal': is_optimal,
            'is_feasible': is_feasible,
            'ratios': ratios if ratios else [],
            'dual_info': {
                'primal_feasible': is_feasible,
                'dual_feasible': is_optimal,
                'status': 'Óptimo' if is_optimal else ('Factible' if is_feasible else 'No factible')
            },
            'tableau_info': {
                'n_rows': self.n_constraints,
                'n_cols': self.n_vars + self.n_constraints,
                'basic_vars': [f'x{bv+1}' if bv < self.n_vars else f'S{bv-self.n_vars+1}' for bv in self.basic_vars]
            },
            'pivot_info': {
                'row': pivot_row,
                'col': pivot_col,
                'element': float(self.tableau[pivot_row, pivot_col]) if pivot_row is not None and pivot_col is not None else None
            } if pivot_row is not None and pivot_col is not None else None
        }
        self.iterations.append(iteration_data)
    
    def _find_leaving_row(self) -> Optional[int]:
        """
        Encuentra la fila pivote (variable saliente) en Dual Simplex
        Busca el RHS más negativo (solución no factible)
        """
        min_rhs = float('inf')
        leaving_row = None
        
        for i in range(self.n_constraints):
            rhs = self.tableau[i, -1]
            if rhs < -1e-10 and rhs < min_rhs:
                min_rhs = rhs
                leaving_row = i
        
        return leaving_row
    
    def _find_entering_column(self, leaving_row: int) -> Tuple[Optional[int], List[Tuple[int, float]]]:
        """
        Encuentra la columna pivote (variable entrante) en Dual Simplex
        Usa el ratio mínimo de z_j / a_{leaving_row,j} donde a_{leaving_row,j} < 0
        
        Returns:
            Tupla de (columna_pivote, lista_de_ratios)
        """
        z_row = self.tableau[-1, :-1]
        leaving_row_coeffs = self.tableau[leaving_row, :-1]
        
        ratios = []
        valid_ratios = []
        
        for j in range(len(leaving_row_coeffs)):
            coeff = leaving_row_coeffs[j]
            z_coeff = z_row[j]
            
            if coeff < -1e-10:  # Solo columnas con coeficiente negativo
                ratio = z_coeff / coeff
                ratios.append((j, ratio))
                
                # Para Dual Simplex:
                # - MIN: Z-row >= 0, coeff < 0, entonces ratio <= 0. Buscamos ratio menos negativo (máximo)
                # - MAX: Z-row <= 0, coeff < 0, entonces ratio >= 0. Buscamos ratio mínimo positivo
                if self.opt_type == 'min':
                    # Ratios negativos o cero son válidos
                    if ratio <= 1e-10:
                        valid_ratios.append((j, ratio))
                else:  # MAX
                    # Ratios positivos o cero son válidos
                    if ratio >= -1e-10:
                        valid_ratios.append((j, ratio))
        
        if not valid_ratios:
            return None, ratios
        
        # Elegir el ratio apropiado
        if self.opt_type == 'min':
            # Ratio menos negativo (máximo)
            entering_col = max(valid_ratios, key=lambda x: x[1])[0]
        else:  # MAX
            # Ratio mínimo positivo
            entering_col = min(valid_ratios, key=lambda x: x[1])[0]
        return entering_col, ratios
    
    def _pivot_operation(self, pivot_row: int, pivot_col: int) -> List[str]:
        """Realiza la operación de pivoteo y retorna las operaciones realizadas"""
        operations = []
        pivot_element = self.tableau[pivot_row, pivot_col]
        
        # 1. Dividir fila pivote por el elemento pivote
        if abs(pivot_element - 1.0) > 1e-10:
            operations.append(f"F{pivot_row + 1} = F{pivot_row + 1} / ({pivot_element:.4g})")
            self.tableau[pivot_row] = self.tableau[pivot_row] / pivot_element
        
        # 2. Hacer ceros en el resto de la columna pivote
        for i in range(len(self.tableau)):
            if i != pivot_row:
                multiplier = self.tableau[i, pivot_col]
                if abs(multiplier) > 1e-10:
                    row_label = f"F{i + 1}" if i < self.n_constraints else "Z"
                    pivot_label = f"F{pivot_row + 1}"
                    
                    if multiplier > 0:
                        operations.append(f"{row_label} = {row_label} - {multiplier:.4g} × {pivot_label}")
                    else:
                        operations.append(f"{row_label} = {row_label} + {abs(multiplier):.4g} × {pivot_label}")
                    
                    self.tableau[i] = self.tableau[i] - multiplier * self.tableau[pivot_row]
        
        return operations
    
    def _is_optimal(self) -> bool:
        """
        Verifica si la solución es óptima
        Para Dual Simplex: todos los RHS deben ser no negativos (factibilidad primal)
        """
        for i in range(self.n_constraints):
            if self.tableau[i, -1] < -1e-10:
                return False
        return True
    
    def solve(self, max_iterations: int = 100) -> Dict:
        """
        Resuelve el problema usando el método Dual Simplex
        
        Returns:
            Dict con el resultado y todas las iteraciones
        """
        try:
            for iteration in range(max_iterations):
                # Verificar optimalidad
                if self._is_optimal():
                    return self._build_solution('optimal')
                
                # Encontrar fila saliente (RHS más negativo)
                leaving_row = self._find_leaving_row()
                
                if leaving_row is None:
                    # No hay RHS negativos, solución óptima
                    return self._build_solution('optimal')
                
                # Encontrar columna entrante
                entering_col, ratios = self._find_entering_column(leaving_row)
                
                if entering_col is None:
                    # No hay columna válida, problema infactible
                    return self._build_solution('infeasible')
                
                # Variables entrante y saliente
                entering_var = entering_col
                leaving_var = self.basic_vars[leaving_row]
                
                # Realizar pivoteo
                operations = self._pivot_operation(leaving_row, entering_col)
                
                # Actualizar variable básica
                self.basic_vars[leaving_row] = entering_var
                
                # Incrementar iteración
                self.current_iteration += 1
                
                # Guardar iteración
                operation_str = " | ".join(operations)
                self._save_iteration(
                    pivot_col=entering_col,
                    pivot_row=leaving_row,
                    entering_var=entering_var,
                    leaving_var=leaving_var,
                    operation=operation_str,
                    ratios=ratios
                )
            
            # Máximo de iteraciones alcanzado
            return self._build_solution('max_iterations')
        
        except Exception as e:
            return {
                'success': False,
                'status': 'error',
                'error': f'Error durante la ejecución del Dual Simplex: {str(e)}'
            }
    
    def _build_solution(self, status: str) -> Dict:
        """Construye el diccionario de solución"""
        if status == 'optimal':
            # Extraer valores de las variables
            solution = {}
            for i in range(self.n_vars):
                if i in self.basic_vars:
                    row_idx = self.basic_vars.index(i)
                    value = self.tableau[row_idx, -1]
                    solution[f'x{i + 1}'] = round(float(value), 4)
                else:
                    solution[f'x{i + 1}'] = 0.0
            
            # Valor óptimo
            # Para MIN: tableau tiene Z + cx = b, entonces Z_opt = -b
            # Para MAX: convertimos a min(-Z), tableau tiene -Z + (-c)x = b, entonces Z_opt = b
            z_value = self.tableau[-1, -1]
            if self.opt_type == 'min':
                optimal_value = round(-z_value, 4)  # MIN: Z = -valor_RHS
            else:
                optimal_value = round(z_value, 4)  # MAX: Z = valor_RHS
            
            return {
                'success': True,
                'status': 'optimal',
                'optimal_value': round(optimal_value, 4),
                'solution': solution,
                'opt_type': self.opt_type,
                'iterations': self.iterations,
                'method': 'Dual Simplex con Tableau',
                'factibilidad_dual': 'Verificada',
                'estado_final': 'Óptimo'
            }
        
        elif status == 'infeasible':
            return {
                'success': False,
                'status': 'infeasible',
                'error': 'El problema no tiene solución factible (infeasible).',
                'iterations': self.iterations,
                'factibilidad_dual': 'No factible',
                'estado_final': 'Infeasible'
            }
        
        elif status == 'max_iterations':
            return {
                'success': False,
                'status': 'error',
                'error': 'Se alcanzó el máximo de iteraciones sin encontrar solución óptima.',
                'iterations': self.iterations,
                'estado_final': 'Error'
            }
        
        else:
            return {
                'success': False,
                'status': 'error',
                'error': 'Estado desconocido.',
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
    return coefficients, op, rhs_value


def solve_dual_simplex_tableau(objective_str: str, constraints_list: List[str]) -> Dict:
    """
    Resuelve un problema de programación lineal usando el método Dual Simplex con tableau
    
    NOTA: Para problemas con >= en minimización, se resuelve convirtiendo a forma estándar
    """
    try:
        # Parse objetivo
        opt_type, obj_coeffs = parse_objective(objective_str)
        n_vars = len(obj_coeffs)
        
        # Parse restricciones
        constraints = []
        for constraint_str in constraints_list:
            constraint_str = constraint_str.strip()
            if not constraint_str or re.match(r'x\d+\s*>=\s*0', constraint_str.lower()):
                continue
            
            try:
                coeffs, op, rhs = parse_constraint(constraint_str, n_vars)
                
                # Para Dual Simplex, convertir >= en <= con coeficientes negados
                # Ejemplo: x1 + 2x2 >= 6  →  -x1 - 2x2 + S1 = -6  (RHS negativo es OK para Dual Simplex)
                if op == '>=':
                    # Negar ambos lados: -x1 - 2x2 <= -6
                    coeffs = [-c for c in coeffs]
                    rhs = -rhs
                
                constraints.append({'coeffs': coeffs, 'rhs': rhs, 'type': op})
            except Exception as e:
                continue
        
        if not constraints:
            return {
                'success': False,
                'status': 'error',
                'error': 'No se encontraron restricciones válidas.'
            }
        
        # Construir matrices
        A = [c['coeffs'] for c in constraints]
        b = [c['rhs'] for c in constraints]
        
        # Crear y resolver tableau
        tableau = DualSimplexTableau(obj_coeffs, A, b, opt_type)
        result = tableau.solve()
        
        return result
    
    except Exception as e:
        import traceback
        return {
            'success': False,
            'status': 'error',
            'error': f'Error al procesar el problema: {str(e)}\n{traceback.format_exc()}'
        }
