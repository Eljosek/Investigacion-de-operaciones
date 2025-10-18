"""
Implementación del Método Simplex con Tableau
Genera visualización paso a paso con todas las iteraciones
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
import re


class SimplexTableau:
    def __init__(self, c: List[float], A: List[List[float]], b: List[float], opt_type: str = 'max'):
        """
        Inicializa el problema de programación lineal en forma estándar
        
        Args:
            c: Coeficientes de la función objetivo
            A: Matriz de coeficientes de restricciones
            b: Vector de términos independientes
            opt_type: 'max' o 'min'
        """
        self.opt_type = opt_type.lower()
        self.n_vars = len(c)  # Variables originales
        self.n_constraints = len(b)
        
        # No convertir, mantener el tipo original
        self.c_original = c.copy()
        
        # Variables de holgura
        self.slack_vars = list(range(self.n_vars, self.n_vars + self.n_constraints))
        
        # Construir tableau inicial
        # Formato: [variables originales | variables de holgura | RHS]
        self.tableau = []
        for i in range(self.n_constraints):
            row = A[i].copy()
            # Agregar variables de holgura (identidad)
            slack = [0] * self.n_constraints
            slack[i] = 1
            row.extend(slack)
            row.append(b[i])
            self.tableau.append(row)
        
        # Fila objetivo (Z) - negativos para maximización
        # Para max: ponemos -c en la fila Z (para que al resolver, aumentar una variable con coef negativo mejore Z)
        # Para min: ponemos c directamente
        if self.opt_type == 'max':
            z_row = [-ci for ci in c]
        else:
            z_row = c.copy()
        z_row.extend([0] * self.n_constraints)  # Coeficientes de holgura en Z
        z_row.append(0)  # Valor inicial de Z
        self.tableau.append(z_row)
        
        # Convertir a numpy array
        self.tableau = np.array(self.tableau, dtype=float)
        
        # Variables básicas iniciales (variables de holgura)
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
            operation="Tableau Inicial"
        )
    
    def _save_iteration(self, pivot_col: Optional[int], pivot_row: Optional[int],
                       entering_var: Optional[int], leaving_var: Optional[int],
                       operation: str):
        """Guarda el estado actual del tableau"""
        # Verificar optimalidad
        z_row = self.tableau[-1, :-1]
        if self.opt_type == 'max':
            is_optimal = all(z_row >= -1e-10)
        else:
            is_optimal = all(z_row >= -1e-10)
        
        # Valor objetivo actual
        if self.opt_type == 'max':
            objective_value = -self.tableau[-1, -1]
        else:
            objective_value = self.tableau[-1, -1]
        
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
            'z_value': self.tableau[-1, -1],
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
    
    def _find_pivot_column(self) -> Optional[int]:
        """Encuentra la columna pivote (variable entrante)"""
        z_row = self.tableau[-1, :-1]
        
        # Para minimización: el más negativo
        # Para maximización (ya convertido): el más negativo
        negative_indices = np.where(z_row < -1e-10)[0]
        
        if len(negative_indices) == 0:
            return None  # Óptimo alcanzado
        
        # Elegir el más negativo (regla de Bland para evitar ciclos)
        pivot_col = negative_indices[np.argmin(z_row[negative_indices])]
        return pivot_col
    
    def _find_pivot_row(self, pivot_col: int) -> Optional[int]:
        """Encuentra la fila pivote (variable saliente) usando el ratio mínimo"""
        ratios = []
        for i in range(self.n_constraints):
            denominator = self.tableau[i, pivot_col]
            if denominator > 1e-10:  # Solo positivos
                ratio = self.tableau[i, -1] / denominator
                ratios.append((ratio, i))
            else:
                ratios.append((float('inf'), i))
        
        # Filtrar ratios válidos (no negativos)
        valid_ratios = [(r, i) for r, i in ratios if r >= 0 and r != float('inf')]
        
        if not valid_ratios:
            return None  # Problema no acotado
        
        # Elegir el ratio mínimo
        min_ratio, pivot_row = min(valid_ratios, key=lambda x: x[0])
        return pivot_row
    
    def _pivot_operation(self, pivot_row: int, pivot_col: int) -> List[str]:
        """Realiza la operación de pivoteo y retorna las operaciones realizadas"""
        operations = []
        pivot_element = self.tableau[pivot_row, pivot_col]
        
        # 1. Dividir fila pivote por el elemento pivote
        if abs(pivot_element - 1.0) > 1e-10:
            operations.append(f"F{pivot_row + 1} = F{pivot_row + 1} / {pivot_element:.4g}")
            self.tableau[pivot_row] = self.tableau[pivot_row] / pivot_element
        
        # 2. Hacer ceros en el resto de la columna pivote
        for i in range(len(self.tableau)):
            if i != pivot_row:
                multiplier = self.tableau[i, pivot_col]
                if abs(multiplier) > 1e-10:
                    # Determinar el nombre de la fila
                    row_name = f"F{i + 1}" if i < self.n_constraints else "FZ"
                    pivot_row_name = f"F{pivot_row + 1}"
                    
                    if multiplier > 0:
                        operations.append(f"{row_name} = {row_name} - {multiplier:.4g} × {pivot_row_name}")
                    else:
                        operations.append(f"{row_name} = {row_name} + {abs(multiplier):.4g} × {pivot_row_name}")
                    self.tableau[i] = self.tableau[i] - multiplier * self.tableau[pivot_row]
        
        return operations
    
    def solve(self, max_iterations: int = 100) -> Dict:
        """
        Resuelve el problema usando el método Simplex
        
        Returns:
            Dict con el resultado y todas las iteraciones
        """
        try:
            for iteration in range(max_iterations):
                # Encontrar columna pivote
                pivot_col = self._find_pivot_column()
                
                if pivot_col is None:
                    # Solución óptima encontrada
                    return self._build_solution('optimal')
                
                # Encontrar fila pivote
                pivot_row = self._find_pivot_row(pivot_col)
                
                if pivot_row is None:
                    # Problema no acotado
                    return self._build_solution('unbounded')
                
                # Variables entrante y saliente
                entering_var = pivot_col
                leaving_var = self.basic_vars[pivot_row]
                
                # Realizar pivoteo
                operations = self._pivot_operation(pivot_row, pivot_col)
                
                # Actualizar variable básica
                self.basic_vars[pivot_row] = entering_var
                
                # Incrementar iteración
                self.current_iteration += 1
                
                # Guardar iteración
                operation_str = " | ".join(operations)
                self._save_iteration(
                    pivot_col=pivot_col,
                    pivot_row=pivot_row,
                    entering_var=entering_var,
                    leaving_var=leaving_var,
                    operation=operation_str
                )
            
            # Máximo de iteraciones alcanzado
            return self._build_solution('max_iterations')
        
        except Exception as e:
            return {
                'success': False,
                'status': 'error',
                'error': f'Error durante la ejecución del Simplex: {str(e)}'
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
            
            # Valor óptimo - está directamente en el RHS de la fila Z
            optimal_value = self.tableau[-1, -1]
            
            return {
                'success': True,
                'status': 'optimal',
                'optimal_value': round(optimal_value, 4),
                'solution': solution,
                'opt_type': self.opt_type,
                'iterations': self.iterations,
                'method': 'Simplex con Tableau'
            }
        
        elif status == 'unbounded':
            return {
                'success': False,
                'status': 'unbounded',
                'error': 'La solución es no acotada (unbounded).',
                'iterations': self.iterations
            }
        
        elif status == 'max_iterations':
            return {
                'success': False,
                'status': 'error',
                'error': 'Se alcanzó el máximo de iteraciones sin encontrar solución óptima.',
                'iterations': self.iterations
            }
        
        else:
            return {
                'success': False,
                'status': 'error',
                'error': 'Estado desconocido.',
                'iterations': self.iterations
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


def solve_simplex_tableau(objective_str: str, constraints_list: List[str]) -> Dict:
    """
    Resuelve un problema de programación lineal usando el método Simplex con tableau
    
    Args:
        objective_str: String de la función objetivo (ej: "max z = 3x1 + 2x2")
        constraints_list: Lista de strings con las restricciones
    
    Returns:
        Dict con la solución y todas las iteraciones del tableau
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
                
                # Normalizar restricciones a forma estándar (<=)
                # Para Simplex, necesitamos RHS no negativos
                if op == '<=':
                    # Caso normal: mantener como está si RHS >= 0
                    if rhs >= 0:
                        constraints.append({'coeffs': coeffs, 'rhs': rhs, 'type': '<='})
                    else:
                        # Si RHS < 0, negar ambos lados
                        constraints.append({'coeffs': [-c for c in coeffs], 'rhs': -rhs, 'type': '<='})
                elif op == '>=':
                    # Para >=, convertir a <= multiplicando por -1
                    coeffs_neg = [-c for c in coeffs]
                    rhs_neg = -rhs
                    # Asegurar RHS no negativo
                    if rhs_neg < 0:
                        coeffs_neg = [-c for c in coeffs_neg]
                        rhs_neg = -rhs_neg
                    constraints.append({'coeffs': coeffs_neg, 'rhs': rhs_neg, 'type': '<='})
                elif op == '=':
                    # Para igualdades, tratarlas como <= (simplificado)
                    if rhs >= 0:
                        constraints.append({'coeffs': coeffs, 'rhs': rhs, 'type': '<='})
                    else:
                        constraints.append({'coeffs': [-c for c in coeffs], 'rhs': -rhs, 'type': '<='})
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
        tableau = SimplexTableau(obj_coeffs, A, b, opt_type)
        result = tableau.solve()
        
        return result
    
    except Exception as e:
        return {
            'success': False,
            'status': 'error',
            'error': f'Error al procesar el problema: {str(e)}'
        }
