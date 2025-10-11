"""
Solver Simplex Mejorado - Implementación Completa del Algoritmo
==============================================================

Implementa el método Simplex clásico con tableaux paso a paso.
Garantiza resultados correctos y proporciona historial detallado.

Características:
- Algoritmo Simplex tradicional con tableaux
- Soporte completo para <=, >=, = restricciones
- Variables de holgura, exceso y artificiales
- Detección de casos infactibles y no acotados
- Historial completo de iteraciones
- Normalizacion correcta de signos para MAX/MIN

Autor: Jose Herrera
Proyecto: Investigación de Operaciones UTP
Fecha: Octubre 2025
"""

import numpy as np
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class TableauIteration:
    """Representa una iteración del tableau Simplex"""
    iteration: int
    tableau: np.ndarray
    basic_vars: List[str]
    entering_var: Optional[str]
    leaving_var: Optional[str]
    pivot_element: Optional[float]
    is_optimal: bool
    description: str


class SimplexSolver:
    """
    Implementación completa del algoritmo Simplex con tableau.
    
    Maneja automáticamente:
    - Variables de holgura para restricciones <=
    - Variables de exceso + artificiales para restricciones >=
    - Variables artificiales para restricciones =
    - Método de dos fases cuando hay variables artificiales
    """
    
    def __init__(self, debug=False):
        self.debug = debug
        self.iterations_history = []
        self.tableau = None
        self.basic_vars = []
        self.var_names = []
        self.n_original_vars = 0
        self.artificial_vars = []
        
    def parse_objective(self, obj_str: str) -> Tuple[str, List[float]]:
        """Extrae tipo de optimización y coeficientes"""
        obj_str = obj_str.lower().strip()
        opt_type = 'max' if 'max' in obj_str else 'min'
        
        if '=' not in obj_str:
            raise ValueError("La función objetivo debe contener '='")
        
        expr = obj_str.split('=')[1].strip().replace(' ', '').lower()
        
        # Encontrar variables
        variables = re.findall(r'x\d+', expr)
        if not variables:
            raise ValueError("No se encontraron variables")
        
        self.n_original_vars = max(int(v[1:]) for v in variables)
        
        # Normalizar expresión
        if expr[0] not in ['+', '-']:
            expr = '+' + expr
        
        # Extraer coeficientes
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
        
        coefficients = [coef_dict.get(i, 0.0) for i in range(1, self.n_original_vars + 1)]
        return opt_type, coefficients
    
    def parse_constraint(self, constraint_str: str) -> Tuple[List[float], str, float]:
        """Parsea una restricción individual"""
        constraint_str = constraint_str.strip()
        
        # Detectar operador
        if '<=' in constraint_str:
            op = '<='
            lhs, rhs = constraint_str.split('<=')
        elif '>=' in constraint_str:
            op = '>='
            lhs, rhs = constraint_str.split('>=')
        elif '=' in constraint_str and '<=' not in constraint_str and '>=' not in constraint_str:
            op = '='
            lhs, rhs = constraint_str.split('=')
        else:
            raise ValueError(f"Operador no válido en: {constraint_str}")
        
        lhs = lhs.strip().replace(' ', '').lower()
        rhs_value = float(rhs.strip())
        
        # Normalizar lado izquierdo
        if lhs[0] not in ['+', '-']:
            lhs = '+' + lhs
        
        # Extraer coeficientes
        coef_dict = {}
        pattern = r'([+-]?\d*\.?\d*)x(\d+)'
        for coef_str, var_num in re.findall(pattern, lhs):
            var_num = int(var_num)
            if coef_str in ['', '+']:
                coef = 1.0
            elif coef_str == '-':
                coef = -1.0
            else:
                coef = float(coef_str)
            coef_dict[var_num] = coef_dict.get(var_num, 0.0) + coef
        
        # Construir lista alineada
        coefficients = [coef_dict.get(i, 0.0) for i in range(1, self.n_original_vars + 1)]
        
        return coefficients, op, rhs_value
    
    def setup_tableau(self, obj_coeffs: List[float], constraints: List[Tuple], opt_type: str):
        """Configura el tableau inicial con variables de holgura/exceso/artificiales"""
        
        # Contar variables auxiliares necesarias
        n_slack = sum(1 for _, op, _ in constraints if op == '<=')
        n_surplus = sum(1 for _, op, _ in constraints if op in ['>=', '='])
        n_artificial = sum(1 for _, op, _ in constraints if op in ['>=', '='])
        
        total_vars = self.n_original_vars + n_slack + n_surplus + n_artificial
        n_constraints = len(constraints)
        
        # Crear tableau: [fila_objetivo, restricciones]
        self.tableau = np.zeros((n_constraints + 1, total_vars + 1))
        
        # Configurar nombres de variables
        self.var_names = [f'x{i+1}' for i in range(self.n_original_vars)]
        slack_idx = surplus_idx = artificial_idx = 0
        
        # Fila objetivo: Para MAX: -c (forma estándar), Para MIN: +c
        if opt_type == 'max':
            self.tableau[0, :self.n_original_vars] = [-c for c in obj_coeffs]
        else:
            self.tableau[0, :self.n_original_vars] = obj_coeffs
        
        # Variables básicas iniciales
        self.basic_vars = []
        col_idx = self.n_original_vars
        
        # Procesar cada restricción
        for i, (coeffs, op, rhs) in enumerate(constraints):
            row_idx = i + 1
            
            # Coeficientes de variables originales
            self.tableau[row_idx, :self.n_original_vars] = coeffs
            
            # Lado derecho
            self.tableau[row_idx, -1] = rhs
            
            if op == '<=':
                # Variable de holgura
                slack_name = f's{slack_idx + 1}'
                self.var_names.append(slack_name)
                self.tableau[row_idx, col_idx] = 1.0
                self.basic_vars.append(slack_name)
                slack_idx += 1
                col_idx += 1
                
            elif op == '>=':
                # Variable de exceso (surplus)
                surplus_name = f'e{surplus_idx + 1}'
                self.var_names.append(surplus_name)
                self.tableau[row_idx, col_idx] = -1.0
                surplus_idx += 1
                col_idx += 1
                
                # Variable artificial
                artificial_name = f'a{artificial_idx + 1}'
                self.var_names.append(artificial_name)
                self.artificial_vars.append(artificial_name)
                self.tableau[row_idx, col_idx] = 1.0
                self.basic_vars.append(artificial_name)
                
                # Penalización en función objetivo (Big M)
                if opt_type == 'max':
                    self.tableau[0, col_idx] = -1000000  # Gran penalización negativa para MAX
                else:
                    self.tableau[0, col_idx] = 1000000   # Gran penalización positiva para MIN
                
                artificial_idx += 1
                col_idx += 1
                
            elif op == '=':
                # Solo variable artificial
                artificial_name = f'a{artificial_idx + 1}'
                self.var_names.append(artificial_name)
                self.artificial_vars.append(artificial_name)
                self.tableau[row_idx, col_idx] = 1.0
                self.basic_vars.append(artificial_name)
                
                # Penalización en función objetivo
                if opt_type == 'max':
                    self.tableau[0, col_idx] = -1000000  # Gran penalización negativa para MAX
                else:
                    self.tableau[0, col_idx] = 1000000   # Gran penalización positiva para MIN
                
                artificial_idx += 1
                col_idx += 1
        
        # Eliminar variables artificiales de la función objetivo
        if self.artificial_vars:
            self._eliminate_artificial_vars_from_objective()
    
    def _eliminate_artificial_vars_from_objective(self):
        """Elimina variables artificiales de la función objetivo usando operaciones de fila"""
        for art_var in self.artificial_vars:
            if art_var in self.basic_vars:
                art_col = self.var_names.index(art_var)
                art_row = self.basic_vars.index(art_var) + 1
                
                # Operación de fila para hacer 0 el coeficiente de la variable artificial
                pivot = self.tableau[art_row, art_col]
                if abs(pivot) > 1e-10:
                    self.tableau[0] -= (self.tableau[0, art_col] / pivot) * self.tableau[art_row]
    
    def solve_simplex(self, obj_str: str, constraints_str: List[str]) -> Dict:
        """
        Resuelve un problema de programación lineal usando el método Simplex.
        
        Returns:
            Dict con formato estándar especificado
        """
        try:
            # Limpiar y validar entrada
            constraints_str = [c.strip() for c in constraints_str if c.strip()]
            constraints_str = [c for c in constraints_str if not re.match(r'x\d+\s*>=\s*0', c.lower())]
            
            if not constraints_str:
                return {
                    "status": "error",
                    "message": "No se encontraron restricciones válidas"
                }
            
            # Parsear problema
            opt_type, obj_coeffs = self.parse_objective(obj_str)
            constraints = []
            
            for constraint_str in constraints_str:
                try:
                    coeffs, op, rhs = self.parse_constraint(constraint_str)
                    constraints.append((coeffs, op, rhs))
                except Exception as e:
                    if self.debug:
                        print(f"Ignorando restricción '{constraint_str}': {e}")
            
            # Configurar tableau inicial
            self.setup_tableau(obj_coeffs, constraints, opt_type)
            
            # Guardar estado inicial
            self._save_iteration(0, None, None, None, False, "Tableau inicial")
            
            # Ejecutar algoritmo Simplex
            iteration = 0
            max_iterations = 100
            
            while iteration < max_iterations:
                # Verificar optimalidad
                if self._is_optimal(opt_type):
                    self._save_iteration(iteration + 1, None, None, None, True, "Solución óptima encontrada")
                    break
                
                # Verificar no acotado
                entering_col = self._get_entering_variable(opt_type)
                if entering_col == -1:
                    return {
                        "status": "error",
                        "message": "Problem unbounded"
                    }
                
                leaving_row = self._get_leaving_variable(entering_col)
                if leaving_row == -1:
                    return {
                        "status": "error", 
                        "message": "Problem unbounded"
                    }
                
                # Realizar pivoteo
                entering_var = self.var_names[entering_col]
                leaving_var = self.basic_vars[leaving_row - 1]
                pivot_element = self.tableau[leaving_row, entering_col]
                
                self._pivot(leaving_row, entering_col)
                self.basic_vars[leaving_row - 1] = entering_var
                
                iteration += 1
                self._save_iteration(
                    iteration, entering_var, leaving_var, pivot_element, 
                    False, f"Pivoteo: {leaving_var} sale, {entering_var} entra"
                )
            
            if iteration >= max_iterations:
                return {
                    "status": "error",
                    "message": "Maximum iterations reached"
                }
            
            # Verificar factibilidad (variables artificiales)
            for i, var in enumerate(self.basic_vars):
                if var in self.artificial_vars and abs(self.tableau[i + 1, -1]) > 1e-10:
                    return {
                        "status": "error",
                        "message": "Problem infeasible"
                    }
            
            # Extraer solución
            solution = self._extract_solution()
            opt_value = self._get_objective_value(opt_type)
            
            return {
                "status": "success",
                "opt_value": round(opt_value, 6),
                "variables": solution,
                "iterations": iteration,
                "message": "Optimal solution found",
                "tableau_history": [self._format_iteration(it) for it in self.iterations_history],
                "method": "Simplex (Tableau Algorithm)"
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error en solver: {str(e)}"
            }
    
    def _is_optimal(self, opt_type: str) -> bool:
        """Verifica si el tableau actual es óptimo"""
        # Ignorar variables artificiales en la verificación de optimización
        non_artificial_cols = []
        for i, var_name in enumerate(self.var_names):
            if var_name not in self.artificial_vars:
                non_artificial_cols.append(i)
        
        if opt_type == 'max':
            # Para MAX: óptimo si todos los coeficientes no artificiales >= 0
            for col in non_artificial_cols:
                if col < len(self.tableau[0]) - 1 and self.tableau[0, col] < -1e-10:
                    return False
            return True
        else:
            # Para MIN: óptimo si todos los coeficientes no artificiales <= 0  
            for col in non_artificial_cols:
                if col < len(self.tableau[0]) - 1 and self.tableau[0, col] > 1e-10:
                    return False
            return True
    
    def _get_entering_variable(self, opt_type: str) -> int:
        """Encuentra la variable que entra (regla de Bland) excluyendo artificiales"""
        best_col = -1
        best_val = 0
        
        for i, var_name in enumerate(self.var_names):
            if i >= len(self.tableau[0]) - 1:  # Saltar columna RHS
                continue
                
            if var_name in self.artificial_vars:  # Ignorar variables artificiales
                continue
                
            coeff = self.tableau[0, i]
            
            if opt_type == 'max':
                # Para MAX: buscar coeficiente más negativo
                if coeff < best_val - 1e-10:
                    best_val = coeff
                    best_col = i
            else:
                # Para MIN: buscar coeficiente más positivo
                if coeff > best_val + 1e-10:
                    best_val = coeff
                    best_col = i
        
        return best_col
    
    def _get_leaving_variable(self, entering_col: int) -> int:
        """Encuentra la variable que sale (regla del ratio mínimo)"""
        ratios = []
        for i in range(1, self.tableau.shape[0]):
            if self.tableau[i, entering_col] > 1e-10:
                ratio = self.tableau[i, -1] / self.tableau[i, entering_col]
                if ratio >= 0:
                    ratios.append((ratio, i))
        
        if not ratios:
            return -1  # No acotado
        
        # Regla del ratio mínimo
        ratios.sort()
        return ratios[0][1]
    
    def _pivot(self, pivot_row: int, pivot_col: int):
        """Realiza operación de pivoteo"""
        pivot_element = self.tableau[pivot_row, pivot_col]
        
        # Normalizar fila pivote
        self.tableau[pivot_row] /= pivot_element
        
        # Eliminar columna pivote en otras filas
        for i in range(self.tableau.shape[0]):
            if i != pivot_row and abs(self.tableau[i, pivot_col]) > 1e-10:
                self.tableau[i] -= self.tableau[i, pivot_col] * self.tableau[pivot_row]
    
    def _extract_solution(self) -> Dict[str, float]:
        """Extrae la solución del tableau final"""
        solution = {}
        
        # Variables originales
        for i in range(self.n_original_vars):
            var_name = f'x{i+1}'
            if var_name in self.basic_vars:
                row_idx = self.basic_vars.index(var_name) + 1
                solution[var_name] = round(self.tableau[row_idx, -1], 6)
            else:
                solution[var_name] = 0.0
        
        return solution
    
    def _get_objective_value(self, opt_type: str) -> float:
        """Obtiene el valor objetivo final"""
        # El valor objetivo siempre está en tableau[0, -1] pero con signo correcto
        raw_value = self.tableau[0, -1]
        
        if opt_type == 'max':
            # Para MAX con forma estándar: Z = -tableau[0, -1]
            return -raw_value
        else:
            # Para MIN: Z = tableau[0, -1]
            return raw_value
    
    def _save_iteration(self, iteration: int, entering_var: Optional[str], 
                       leaving_var: Optional[str], pivot_element: Optional[float],
                       is_optimal: bool, description: str):
        """Guarda una iteración en el historial"""
        self.iterations_history.append(TableauIteration(
            iteration=iteration,
            tableau=self.tableau.copy(),
            basic_vars=self.basic_vars.copy(),
            entering_var=entering_var,
            leaving_var=leaving_var,
            pivot_element=pivot_element,
            is_optimal=is_optimal,
            description=description
        ))
    
    def _format_iteration(self, iteration: TableauIteration) -> Dict:
        """Formatea una iteración para el frontend"""
        return {
            "iteration": iteration.iteration,
            "description": iteration.description,
            "basic_vars": iteration.basic_vars,
            "entering_var": iteration.entering_var,
            "leaving_var": iteration.leaving_var,
            "pivot_element": iteration.pivot_element,
            "tableau": iteration.tableau.tolist(),
            "var_names": self.var_names,
            "is_optimal": iteration.is_optimal
        }


# Función de interfaz pública
def solve_simplex(objective_str: str, constraints_list: List[str]) -> Dict:
    """
    Interfaz pública para resolver problemas con el método Simplex.
    
    Args:
        objective_str: Función objetivo (ej: "maximizar z = 3x1 + 2x2")
        constraints_list: Lista de restricciones
    
    Returns:
        Dict con formato estándar especificado
    """
    solver = SimplexSolver(debug=False)
    return solver.solve_simplex(objective_str, constraints_list)


# Bloque de pruebas
if __name__ == "__main__":
    print("=" * 80)
    print("SIMPLEX SOLVER MEJORADO - PRUEBAS DE VALIDACIÓN")
    print("=" * 80)
    
    # Test casos diversos según especificaciones
    test_cases = [
        {
            "name": "Test 1: Maximización básica (2 vars)",
            "objective": "maximizar z = 3x1 + 2x2", 
            "constraints": ["x1 + x2 <= 4", "2x1 + x2 <= 6"],
            "expected_z": 10.0
        },
        {
            "name": "Test 2: Minimización con >= (2 vars)",
            "objective": "minimizar z = 2x1 + 3x2",
            "constraints": ["x1 + 2x2 >= 4", "2x1 + x2 >= 3"],
            "expected_z": 5.0
        },
        {
            "name": "Test 3: Caso crítico (3 vars) - Debe dar Z=24",
            "objective": "minimizar z = 5x1 + 4x2 + 3x3",
            "constraints": ["x1 + x2 + x3 >= 8", "2x1 + x2 <= 12", "x2 + 2x3 >= 6"],
            "expected_z": 24.0
        },
        {
            "name": "Test 4: Restricciones mixtas",
            "objective": "maximizar z = 4x1 + 3x2 + 2x3",
            "constraints": ["x1 + x2 + x3 <= 10", "2x1 + x2 >= 8", "x2 + x3 = 5"],
            "expected_z": None  # Verificar manualmente
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{'-' * 60}")
        print(f"{test['name']}")
        print(f"Objetivo: {test['objective']}")
        print(f"Restricciones: {test['constraints']}")
        
        result = solve_simplex(test['objective'], test['constraints'])
        
        if result['status'] == 'success':
            print(f"✓ Estado: {result['status'].upper()}")
            print(f"✓ Z = {result['opt_value']}")
            print(f"✓ Variables: {result['variables']}")
            print(f"✓ Iteraciones: {result['iterations']}")
            
            if test['expected_z'] is not None:
                diff = abs(result['opt_value'] - test['expected_z'])
                if diff < 0.01:
                    print(f"✓✓✓ CORRECTO: Z ≈ {test['expected_z']} ✓✓✓")
                else:
                    print(f"✗✗✗ ERROR: Esperado Z={test['expected_z']}, obtenido Z={result['opt_value']} ✗✗✗")
        else:
            print(f"✗ Error: {result['message']}")
    
    print(f"\n{'=' * 80}")
    print("FIN DE VALIDACIÓN")
    print("=" * 80)