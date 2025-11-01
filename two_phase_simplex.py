#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Método Simplex con Dos Fases (Variables Artificiales)
Implementación para problemas de Programación Lineal con restricciones mixtas

Autor: José Miguel Herrera Gutiérrez
Para: Investigación de Operaciones - UTP
Fecha: Octubre 2025
"""

import numpy as np
import re
from typing import Dict, List, Tuple, Any, Optional


class TwoPhaseSimplexSolver:
    """
    Resuelve problemas de Programación Lineal usando el Método Simplex con Dos Fases.
    
    Soporta:
    - Restricciones <=, >= y =
    - Problemas de maximización y minimización
    - Detección de infactibilidad, no acotamiento, degeneración
    """
    
    def __init__(self, objective: str, constraints: List[str], opt_type: str = 'max'):
        """
        Inicializa el solver con el problema de PL.
        
        Args:
            objective: Función objetivo (ej: "3x1 + 5x2")
            constraints: Lista de restricciones (ej: ["4x1 + x2 >= 4", "x2 <= 3"])
            opt_type: 'max' o 'min'
        """
        self.objective_str = objective.strip()
        self.constraints_str = [c.strip() for c in constraints]
        self.opt_type = opt_type.lower()
        
        # Variables del problema
        self.n_vars = 0              # Número de variables de decisión
        self.n_constraints = 0       # Número de restricciones
        self.n_slack = 0             # Número de variables de holgura
        self.n_excess = 0            # Número de variables de exceso
        self.n_artificial = 0        # Número de variables artificiales
        
        # Coeficientes originales
        self.obj_coeffs = []         # Coeficientes de la función objetivo original
        self.constraint_matrix = []  # Matriz de coeficientes de restricciones
        self.rhs = []                # Lado derecho de las restricciones
        self.constraint_types = []   # Tipos: '<=', '>=', '='
        
        # Variables de control
        self.var_names = []          # Nombres de todas las variables
        self.basic_vars = []         # Índices de variables básicas actuales
        self.nonbasic_vars = []      # Índices de variables no básicas
        
        # Tableau
        self.tableau = None          # Tableau actual
        
        # Historial
        self.iterations_phase1 = []  # Iteraciones de Fase I
        self.iterations_phase2 = []  # Iteraciones de Fase II
        self.iteration_count = 0     # Contador de iteraciones
        
        # Tolerancia numérica
        self.EPS = 1e-10
        
    def _clean_small_values(self, value: float, tolerance: float = 1e-10) -> float:
        """Redondea valores muy pequeños a 0 para evitar notación científica."""
        if abs(value) < tolerance:
            return 0.0
        return value
    
    def parse_objective(self) -> Tuple[List[float], int]:
        """
        Parsea la función objetivo y extrae coeficientes.
        
        Returns:
            Tupla (coeficientes, número_de_variables)
        """
        # Remover "max" o "min" y "z ="
        obj_clean = re.sub(r'(max|min|maximize|minimizar)\s*', '', self.objective_str, flags=re.IGNORECASE)
        obj_clean = re.sub(r'z\s*=\s*', '', obj_clean, flags=re.IGNORECASE)
        obj_clean = obj_clean.strip()
        
        # Encontrar todos los términos (ej: "3x1", "-5x2", "x3")
        pattern = r'([+-]?\s*\d*\.?\d*)\s*x(\d+)'
        matches = re.findall(pattern, obj_clean)
        
        if not matches:
            raise ValueError("No se pudo parsear la función objetivo. Formato esperado: '3x1 + 5x2'")
        
        # Determinar número de variables
        max_var_index = max(int(m[1]) for m in matches)
        n_vars = max_var_index
        
        # Inicializar coeficientes en 0
        coeffs = [0.0] * n_vars
        
        # Llenar coeficientes
        for coef_str, var_idx in matches:
            coef_str = coef_str.replace(' ', '')
            
            if coef_str == '' or coef_str == '+':
                coef = 1.0
            elif coef_str == '-':
                coef = -1.0
            else:
                coef = float(coef_str)
            
            coeffs[int(var_idx) - 1] = coef
        
        # Si es MIN, convertir a MAX multiplicando por -1
        if self.opt_type == 'min':
            coeffs = [-c for c in coeffs]
        
        return coeffs, n_vars
    
    def parse_constraints(self) -> Tuple[List[List[float]], List[float], List[str]]:
        """
        Parsea las restricciones y extrae coeficientes, RHS y tipos.
        
        Returns:
            Tupla (matriz_coeficientes, rhs, tipos)
        """
        matrix = []
        rhs = []
        types = []
        
        for constraint in self.constraints_str:
            # Ignorar restricciones de no negatividad
            if 'x' in constraint.lower() and '>=' in constraint and '0' in constraint:
                if constraint.count('x') == 1:  # Solo "xi >= 0"
                    continue
            
            # Detectar tipo de restricción
            if '<=' in constraint:
                constraint_type = '<='
                parts = constraint.split('<=')
            elif '>=' in constraint:
                constraint_type = '>='
                parts = constraint.split('>=')
            elif '=' in constraint and '!' not in constraint:
                constraint_type = '='
                parts = constraint.split('=')
            else:
                continue
            
            if len(parts) != 2:
                raise ValueError(f"Restricción mal formada: {constraint}")
            
            lhs = parts[0].strip()
            rhs_value = float(parts[1].strip())
            
            # Parsear lado izquierdo
            pattern = r'([+-]?\s*\d*\.?\d*)\s*x(\d+)'
            matches = re.findall(pattern, lhs)
            
            if not matches:
                raise ValueError(f"No se pudo parsear restricción: {constraint}")
            
            # Inicializar fila de coeficientes
            row = [0.0] * self.n_vars
            
            for coef_str, var_idx in matches:
                coef_str = coef_str.replace(' ', '')
                
                if coef_str == '' or coef_str == '+':
                    coef = 1.0
                elif coef_str == '-':
                    coef = -1.0
                else:
                    coef = float(coef_str)
                
                row[int(var_idx) - 1] = coef
            
            matrix.append(row)
            rhs.append(rhs_value)
            types.append(constraint_type)
        
        return matrix, rhs, types
    
    def normalize_problem(self):
        """
        Normaliza el problema a forma estándar:
        - <= : agrega variable de holgura
        - >= : agrega variable de exceso y artificial
        - = : agrega variable artificial
        """
        # Parsear función objetivo
        self.obj_coeffs, self.n_vars = self.parse_objective()
        
        # Parsear restricciones
        self.constraint_matrix, self.rhs, self.constraint_types = self.parse_constraints()
        self.n_constraints = len(self.constraint_matrix)
        
        if self.n_constraints == 0:
            raise ValueError("No se encontraron restricciones válidas")
        
        # Contar variables adicionales necesarias
        self.n_slack = sum(1 for t in self.constraint_types if t == '<=')
        self.n_excess = sum(1 for t in self.constraint_types if t == '>=')
        self.n_artificial = sum(1 for t in self.constraint_types if t in ['>=', '='])
        
        # Crear nombres de variables
        self.var_names = []
        
        # Variables de decisión
        for i in range(self.n_vars):
            self.var_names.append(f'x{i+1}')
        
        # Variables de holgura
        slack_count = 0
        for i, ctype in enumerate(self.constraint_types):
            if ctype == '<=':
                slack_count += 1
                self.var_names.append(f's{slack_count}')
        
        # Variables de exceso
        excess_count = 0
        for i, ctype in enumerate(self.constraint_types):
            if ctype == '>=':
                excess_count += 1
                self.var_names.append(f'e{excess_count}')
        
        # Variables artificiales
        artificial_count = 0
        for i, ctype in enumerate(self.constraint_types):
            if ctype in ['>=', '=']:
                artificial_count += 1
                self.var_names.append(f'A{artificial_count}')
        
        print(f"\n📊 Problema Normalizado:")
        print(f"  Variables de decisión: {self.n_vars}")
        print(f"  Restricciones: {self.n_constraints}")
        print(f"  Variables de holgura: {self.n_slack}")
        print(f"  Variables de exceso: {self.n_excess}")
        print(f"  Variables artificiales: {self.n_artificial}")
        print(f"  Tipos de restricciones: {self.constraint_types}")
    
    def build_initial_tableau_phase1(self):
        """
        Construye el tableau inicial para Fase I.
        
        Función objetivo Fase I: min W = suma de variables artificiales
        """
        # Dimensiones del tableau
        n_rows = self.n_constraints + 1  # restricciones + fila Z
        n_cols = self.n_vars + self.n_slack + self.n_excess + self.n_artificial + 1  # variables + RHS
        
        # Inicializar tableau
        self.tableau = np.zeros((n_rows, n_cols))
        
        # Llenar restricciones
        slack_idx = self.n_vars
        excess_idx = self.n_vars + self.n_slack
        artificial_idx = self.n_vars + self.n_slack + self.n_excess
        
        current_slack = 0
        current_excess = 0
        current_artificial = 0
        
        for i, ctype in enumerate(self.constraint_types):
            # Coeficientes de variables de decisión
            for j in range(self.n_vars):
                self.tableau[i, j] = self.constraint_matrix[i][j]
            
            # Agregar variable según tipo
            if ctype == '<=':
                # Agregar holgura
                self.tableau[i, slack_idx + current_slack] = 1.0
                current_slack += 1
            
            elif ctype == '>=':
                # Agregar exceso (negativa) y artificial
                self.tableau[i, excess_idx + current_excess] = -1.0
                self.tableau[i, artificial_idx + current_artificial] = 1.0
                current_excess += 1
                current_artificial += 1
            
            elif ctype == '=':
                # Solo agregar artificial
                self.tableau[i, artificial_idx + current_artificial] = 1.0
                current_artificial += 1
            
            # RHS
            self.tableau[i, -1] = self.rhs[i]
        
        # Fila Z de Fase I: coeficientes 1 para variables artificiales
        for i in range(self.n_artificial):
            self.tableau[-1, artificial_idx + i] = 1.0
        
        # Variables básicas iniciales
        self.basic_vars = []
        current_slack = 0
        current_artificial = 0
        
        for i, ctype in enumerate(self.constraint_types):
            if ctype == '<=':
                # Holgura es básica
                self.basic_vars.append(slack_idx + current_slack)
                current_slack += 1
            else:
                # Artificial es básica
                self.basic_vars.append(artificial_idx + current_artificial)
                current_artificial += 1
        
        # Hacer operaciones de fila para forma canónica (Fase I)
        # Las artificiales básicas deben tener coeficiente 0 en fila Z
        for i, var_idx in enumerate(self.basic_vars):
            if var_idx >= artificial_idx:  # Es artificial
                # Fila_Z = Fila_Z - coef(artificial) × Fila_i
                coef = self.tableau[-1, var_idx]
                if abs(coef) > self.EPS:
                    self.tableau[-1, :] -= coef * self.tableau[i, :]
        
        print(f"\n✅ Tableau Inicial Fase I construido:")
        print(f"  Dimensiones: {n_rows} x {n_cols}")
        print(f"  Variables básicas: {[self.var_names[i] for i in self.basic_vars]}")
        print(f"  W inicial: {self._clean_small_values(self.tableau[-1, -1])}")

    def solve(self) -> Dict[str, Any]:
        """
        Método principal que ejecuta el algoritmo de Dos Fases.
        
        Returns:
            Diccionario con resultados completos
        """
        try:
            # FASE 2: Normalización
            print("\n" + "="*70)
            print("🚀 INICIANDO MÉTODO SIMPLEX DOS FASES")
            print("="*70)
            
            self.normalize_problem()
            
            # Si no hay artificiales, es un problema estándar (solo <=)
            if self.n_artificial == 0:
                print("\n⚠️ No hay variables artificiales. Usar método Simplex estándar.")
                return {
                    'success': False,
                    'error': 'Este problema no requiere Dos Fases. Use el método Simplex estándar.',
                    'opt_type': 'max' if self.opt_type == 'max' else 'min'
                }
            
            self.build_initial_tableau_phase1()
            
            # FASE 3: Ejecutar Fase I
            print("\n" + "="*70)
            print("📍 FASE I: Minimizar suma de variables artificiales")
            print("="*70)
            
            phase1_result = self.phase_one()
            
            if not phase1_result['feasible']:
                return {
                    'success': False,
                    'status': 'infeasible',
                    'error': 'Problema INFACTIBLE: No se pudo eliminar todas las variables artificiales',
                    'opt_type': 'max' if self.opt_type == 'max' else 'min',
                    'iterations_phase1': self.iterations_phase1,
                    'iterations_phase2': [],
                    'total_iterations': len(self.iterations_phase1)
                }
            
            print(f"\n✅ FASE I COMPLETADA: Problema FACTIBLE (W = 0)")
            
            # FASE 4: Ejecutar Fase II
            print("\n" + "="*70)
            print("📍 FASE II: Optimizar función objetivo original")
            print("="*70)
            
            phase2_result = self.phase_two()
            
            # FASE 5: Construir resultado final
            return self.build_result(phase2_result)
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Error durante la ejecución: {str(e)}',
                'opt_type': 'max' if self.opt_type == 'max' else 'min'
            }
    
    def select_pivot_column_phase1(self) -> Optional[int]:
        """
        Selecciona columna pivote para Fase I (minimización de W).
        Regla: Columna con coeficiente MÁS NEGATIVO en fila Z (entrando mejora W).
        
        Returns:
            Índice de columna pivote o None si es óptimo
        """
        z_row = self.tableau[-1, :-1]  # Fila Z sin RHS
        
        # Buscar el coeficiente más negativo
        min_coef = -self.EPS
        pivot_col = None
        
        for j in range(len(z_row)):
            if z_row[j] < min_coef:
                min_coef = z_row[j]
                pivot_col = j
        
        # Si no hay coeficientes negativos, ya es óptimo
        if min_coef >= -self.EPS:
            return None
        
        return pivot_col
    
    def select_pivot_row(self, pivot_col: int) -> Optional[int]:
        """
        Selecciona fila pivote usando razón mínima (Minimum Ratio Test).
        
        Args:
            pivot_col: Índice de columna pivote
            
        Returns:
            Índice de fila pivote o None si no acotado
        """
        min_ratio = float('inf')
        pivot_row = None
        
        for i in range(self.n_constraints):
            pivot_element = self.tableau[i, pivot_col]
            
            # Solo considerar elementos positivos
            if pivot_element > self.EPS:
                rhs = self.tableau[i, -1]
                ratio = rhs / pivot_element
                
                if ratio >= 0 and ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row = i
        
        return pivot_row
    
    def perform_pivot(self, pivot_row: int, pivot_col: int):
        """
        Realiza operaciones de pivoteo (Gauss-Jordan).
        
        Args:
            pivot_row: Índice de fila pivote
            pivot_col: Índice de columna pivote
        """
        pivot_element = self.tableau[pivot_row, pivot_col]
        
        # Dividir fila pivote por elemento pivote
        self.tableau[pivot_row, :] /= pivot_element
        
        # Hacer ceros en columna pivote (excepto en fila pivote)
        for i in range(len(self.tableau)):
            if i != pivot_row:
                multiplier = self.tableau[i, pivot_col]
                self.tableau[i, :] -= multiplier * self.tableau[pivot_row, :]
        
        # Actualizar variable básica
        self.basic_vars[pivot_row] = pivot_col
        
        # Limpiar valores muy pequeños
        self.tableau = np.vectorize(self._clean_small_values)(self.tableau)
    
    def save_iteration_phase1(self, iteration: int, pivot_row: Optional[int], 
                             pivot_col: Optional[int], status: str):
        """
        Guarda información de una iteración de Fase I.
        
        Args:
            iteration: Número de iteración
            pivot_row: Fila pivote (None si es última iteración)
            pivot_col: Columna pivote (None si es última iteración)
            status: Estado ('iterating', 'optimal', 'infeasible', 'unbounded')
        """
        iter_data = {
            'iteration': iteration,
            'phase': 1,
            'tableau': self.tableau.copy().tolist(),  # Convertir a lista para Jinja2
            'basic_vars': self.basic_vars.copy(),
            'basic_var_names': [self.var_names[i] for i in self.basic_vars],
            'w_value': self._clean_small_values(self.tableau[-1, -1]),
            'status': status
        }
        
        if pivot_row is not None and pivot_col is not None:
            iter_data['pivot_row'] = pivot_row
            iter_data['pivot_col'] = pivot_col
            iter_data['entering_var'] = self.var_names[pivot_col]
            iter_data['leaving_var'] = self.var_names[self.basic_vars[pivot_row]]
            iter_data['pivot_element'] = self._clean_small_values(
                self.tableau[pivot_row, pivot_col]
            )
        
        # Valores actuales de variables básicas
        iter_data['solution'] = {}
        for i, var_idx in enumerate(self.basic_vars):
            var_name = self.var_names[var_idx]
            var_value = self._clean_small_values(self.tableau[i, -1])
            iter_data['solution'][var_name] = var_value
        
        self.iterations_phase1.append(iter_data)
    
    def check_feasibility_phase1(self) -> bool:
        """
        Verifica si el problema es factible (W = 0 dentro de tolerancia).
        
        Returns:
            True si W ≈ 0, False en caso contrario
        """
        w_value = self.tableau[-1, -1]
        return abs(w_value) < self.EPS
    
    def phase_one(self) -> Dict[str, Any]:
        """
        Ejecuta Fase I: Minimizar W = suma de artificiales.
        
        Returns:
            Diccionario con resultado de Fase I
        """
        iteration = 0
        
        # Guardar iteración inicial
        self.save_iteration_phase1(iteration, None, None, 'initial')
        print(f"\n  Iteración {iteration}: W = {self._clean_small_values(self.tableau[-1, -1])}")
        
        max_iterations = 100  # Límite de seguridad
        
        while iteration < max_iterations:
            iteration += 1
            
            # Paso 1: Seleccionar columna pivote
            pivot_col = self.select_pivot_column_phase1()
            
            if pivot_col is None:
                # Ya es óptimo
                self.save_iteration_phase1(iteration, None, None, 'optimal')
                print(f"  Iteración {iteration}: ÓPTIMO alcanzado")
                break
            
            # Paso 2: Seleccionar fila pivote
            pivot_row = self.select_pivot_row(pivot_col)
            
            if pivot_row is None:
                # Problema no acotado (raro en Fase I)
                self.save_iteration_phase1(iteration, None, None, 'unbounded')
                print(f"  ⚠️ Problema no acotado en Fase I")
                return {'feasible': False, 'reason': 'unbounded'}
            
            # Paso 3: Realizar pivoteo
            entering_var = self.var_names[pivot_col]
            leaving_var = self.var_names[self.basic_vars[pivot_row]]
            
            print(f"  Iteración {iteration}: {entering_var} entra, {leaving_var} sale")
            
            self.perform_pivot(pivot_row, pivot_col)
            
            # Guardar iteración
            w_value = self._clean_small_values(self.tableau[-1, -1])
            self.save_iteration_phase1(iteration, pivot_row, pivot_col, 'iterating')
            
            print(f"    → W = {w_value}")
        
        # Verificar factibilidad
        is_feasible = self.check_feasibility_phase1()
        
        if not is_feasible:
            w_final = self._clean_small_values(self.tableau[-1, -1])
            print(f"\n  ❌ INFACTIBLE: W = {w_final} ≠ 0")
            return {
                'feasible': False, 
                'reason': 'infeasible',
                'w_value': w_final
            }
        
        print(f"\n  ✅ FACTIBLE: W = 0")
        return {
            'feasible': True,
            'iterations': iteration
        }
    
    def transition_to_phase2(self):
        """
        Prepara el tableau para Fase II:
        - Elimina columnas de variables artificiales
        - Reemplaza fila Z con objetivo original
        - Hace operaciones de fila para forma canónica
        """
        print(f"\n🔄 Transición a Fase II...")
        
        # Identificar columnas artificiales
        artificial_start = self.n_vars + self.n_slack + self.n_excess
        artificial_end = artificial_start + self.n_artificial
        
        # Eliminar columnas de artificiales
        cols_to_keep = list(range(artificial_start)) + [self.tableau.shape[1] - 1]  # Sin artificiales + RHS
        self.tableau = self.tableau[:, cols_to_keep]
        
        # Actualizar nombres de variables
        self.var_names = self.var_names[:artificial_start]
        
        # Actualizar índices de variables básicas
        new_basic_vars = []
        for var_idx in self.basic_vars:
            if var_idx < artificial_start:
                new_basic_vars.append(var_idx)
            else:
                # Variable artificial era básica (no debería pasar si W=0)
                print(f"  ⚠️ Variable artificial {self.var_names[var_idx]} aún básica")
        
        self.basic_vars = new_basic_vars
        
        # Reemplazar fila Z con objetivo original
        z_row = np.zeros(self.tableau.shape[1])
        
        # Coeficientes de variables de decisión (ya convertidos si era MIN)
        for i in range(self.n_vars):
            z_row[i] = -self.obj_coeffs[i]  # Negativo para forma estándar
        
        # Variables de holgura, exceso tienen coeficiente 0 en objetivo
        # (ya están en 0 porque inicializamos con zeros)
        
        # RHS = 0 inicialmente
        z_row[-1] = 0.0
        
        self.tableau[-1, :] = z_row
        
        # Hacer operaciones de fila para forma canónica
        # Variables básicas deben tener coeficiente 0 en fila Z
        for i, var_idx in enumerate(self.basic_vars):
            coef = self.tableau[-1, var_idx]
            if abs(coef) > self.EPS:
                # Fila_Z = Fila_Z - coef × Fila_i
                self.tableau[-1, :] -= coef * self.tableau[i, :]
        
        # Limpiar valores pequeños
        self.tableau = np.vectorize(self._clean_small_values)(self.tableau)
        
        print(f"  ✅ Columnas artificiales eliminadas")
        print(f"  ✅ Función objetivo original restaurada")
        print(f"  ✅ Variables básicas: {[self.var_names[i] for i in self.basic_vars]}")
        print(f"  ✅ Z inicial: {self._clean_small_values(self.tableau[-1, -1])}")
    
    def select_pivot_column_phase2(self) -> Optional[int]:
        """
        Selecciona columna pivote para Fase II (maximización).
        Regla: Columna con coeficiente MÁS NEGATIVO en fila Z.
        
        Returns:
            Índice de columna pivote o None si es óptimo
        """
        z_row = self.tableau[-1, :-1]  # Fila Z sin RHS
        
        # Buscar el coeficiente más negativo
        min_coef = self.EPS
        pivot_col = None
        
        for j in range(len(z_row)):
            if z_row[j] < min_coef:
                min_coef = z_row[j]
                pivot_col = j
        
        # Si no hay coeficientes negativos, ya es óptimo
        if min_coef >= -self.EPS:
            return None
        
        return pivot_col
    
    def save_iteration_phase2(self, iteration: int, pivot_row: Optional[int], 
                             pivot_col: Optional[int], status: str):
        """
        Guarda información de una iteración de Fase II.
        
        Args:
            iteration: Número de iteración
            pivot_row: Fila pivote (None si es última iteración)
            pivot_col: Columna pivote (None si es última iteración)
            status: Estado ('iterating', 'optimal', 'unbounded')
        """
        iter_data = {
            'iteration': iteration,
            'phase': 2,
            'tableau': self.tableau.copy().tolist(),  # Convertir a lista para Jinja2
            'basic_vars': self.basic_vars.copy(),
            'basic_var_names': [self.var_names[i] for i in self.basic_vars],
            'z_value': self._clean_small_values(self.tableau[-1, -1]),
            'status': status
        }
        
        if pivot_row is not None and pivot_col is not None:
            iter_data['pivot_row'] = pivot_row
            iter_data['pivot_col'] = pivot_col
            iter_data['entering_var'] = self.var_names[pivot_col]
            iter_data['leaving_var'] = self.var_names[self.basic_vars[pivot_row]]
            iter_data['pivot_element'] = self._clean_small_values(
                self.tableau[pivot_row, pivot_col]
            )
        
        # Valores actuales de variables de DECISIÓN
        iter_data['solution'] = {}
        for i in range(self.n_vars):
            var_name = self.var_names[i]
            # Buscar si es básica
            if i in self.basic_vars:
                row_idx = self.basic_vars.index(i)
                var_value = self._clean_small_values(self.tableau[row_idx, -1])
            else:
                var_value = 0.0
            iter_data['solution'][var_name] = var_value
        
        self.iterations_phase2.append(iter_data)
    
    def check_unbounded_phase2(self, pivot_col: int) -> bool:
        """
        Verifica si el problema es no acotado.
        Ocurre cuando todos los elementos en columna pivote son <= 0.
        
        Args:
            pivot_col: Índice de columna pivote
            
        Returns:
            True si no acotado, False en caso contrario
        """
        for i in range(self.n_constraints):
            if self.tableau[i, pivot_col] > self.EPS:
                return False
        return True
    
    def phase_two(self) -> Dict[str, Any]:
        """
        Ejecuta Fase II: Optimizar objetivo original.
        
        Returns:
            Diccionario con resultado de Fase II
        """
        # Transición desde Fase I
        self.transition_to_phase2()
        
        iteration = 0
        
        # Guardar iteración inicial
        self.save_iteration_phase2(iteration, None, None, 'initial')
        print(f"\n  Iteración {iteration}: Z = {self._clean_small_values(self.tableau[-1, -1])}")
        
        max_iterations = 100  # Límite de seguridad
        
        while iteration < max_iterations:
            iteration += 1
            
            # Paso 1: Seleccionar columna pivote
            pivot_col = self.select_pivot_column_phase2()
            
            if pivot_col is None:
                # Ya es óptimo
                self.save_iteration_phase2(iteration, None, None, 'optimal')
                print(f"  Iteración {iteration}: ÓPTIMO alcanzado")
                break
            
            # Paso 2: Verificar si no acotado
            if self.check_unbounded_phase2(pivot_col):
                self.save_iteration_phase2(iteration, None, None, 'unbounded')
                print(f"  ⚠️ Problema NO ACOTADO")
                return {
                    'optimal': False,
                    'status': 'unbounded',
                    'reason': f'Columna {self.var_names[pivot_col]} no tiene elementos positivos'
                }
            
            # Paso 3: Seleccionar fila pivote
            pivot_row = self.select_pivot_row(pivot_col)
            
            if pivot_row is None:
                # No debería pasar si check_unbounded ya verificó
                self.save_iteration_phase2(iteration, None, None, 'unbounded')
                return {'optimal': False, 'status': 'unbounded'}
            
            # Paso 4: Realizar pivoteo
            entering_var = self.var_names[pivot_col]
            leaving_var = self.var_names[self.basic_vars[pivot_row]]
            
            print(f"  Iteración {iteration}: {entering_var} entra, {leaving_var} sale")
            
            self.perform_pivot(pivot_row, pivot_col)
            
            # Guardar iteración
            z_value = self._clean_small_values(self.tableau[-1, -1])
            self.save_iteration_phase2(iteration, pivot_row, pivot_col, 'iterating')
            
            print(f"    → Z = {z_value}")
        
        print(f"\n  ✅ ÓPTIMO: Z = {self._clean_small_values(self.tableau[-1, -1])}")
        return {
            'optimal': True,
            'status': 'optimal',
            'iterations': iteration
        }
    
    def build_result(self, phase2_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Construye el diccionario de resultado final.
        
        Args:
            phase2_result: Resultado de Fase II
            
        Returns:
            Diccionario completo con resultados
        """
        if not phase2_result.get('optimal', False):
            return {
                'success': False,
                'status': phase2_result.get('status', 'error'),
                'error': phase2_result.get('reason', 'No se alcanzó solución óptima'),
                'opt_type': self.opt_type,
                'iterations_phase1': self.iterations_phase1,
                'iterations_phase2': self.iterations_phase2,
                'total_iterations': len(self.iterations_phase1) + len(self.iterations_phase2)
            }
        
        # Obtener solución óptima
        solution = {}
        for i in range(self.n_vars):
            var_name = self.var_names[i]
            if i in self.basic_vars:
                row_idx = self.basic_vars.index(i)
                var_value = self._clean_small_values(self.tableau[row_idx, -1])
            else:
                var_value = 0.0
            solution[var_name] = var_value
        
        # Valor óptimo de Z
        z_value = self._clean_small_values(self.tableau[-1, -1])
        
        # Si era MIN, convertir Z de vuelta
        if self.opt_type == 'min':
            z_value = -z_value
        
        # Detectar degeneración (alguna variable básica = 0)
        is_degenerate = False
        for var_idx in self.basic_vars:
            row_idx = self.basic_vars.index(var_idx)
            if abs(self.tableau[row_idx, -1]) < self.EPS:
                is_degenerate = True
                break
        
        # Detectar soluciones múltiples
        # (variable no básica con coeficiente 0 en fila Z)
        has_multiple_solutions = False
        for j in range(len(self.var_names)):
            if j not in self.basic_vars:
                if abs(self.tableau[-1, j]) < self.EPS:
                    has_multiple_solutions = True
                    break
        
        result = {
            'success': True,
            'status': 'optimal',
            'opt_type': self.opt_type,
            'optimal_value': z_value,
            'solution': solution,
            'basic_variables': [self.var_names[i] for i in self.basic_vars],
            'iterations_phase1': self.iterations_phase1,
            'iterations_phase2': self.iterations_phase2,
            'total_iterations': len(self.iterations_phase1) + len(self.iterations_phase2),
            'is_degenerate': is_degenerate,
            'has_multiple_solutions': has_multiple_solutions,
            'final_tableau': self.tableau.copy()
        }
        
        return result


def solve_two_phase_simplex(objective: str, constraints: List[str]) -> Dict[str, Any]:
    """
    Función wrapper para resolver un problema con Dos Fases.
    
    Args:
        objective: Función objetivo como string (ej: "max z = 3x1 + 5x2")
        constraints: Lista de restricciones como strings
        
    Returns:
        Diccionario con resultados completos
    """
    # Detectar tipo de optimización
    opt_type = 'max'
    if 'min' in objective.lower():
        opt_type = 'min'
    
    solver = TwoPhaseSimplexSolver(objective, constraints, opt_type)
    return solver.solve()


if __name__ == '__main__':
    # Prueba con el caso de ejemplo del usuario
    print("\n" + "="*70)
    print("🧪 PRUEBA: Caso de ejemplo del usuario")
    print("="*70)
    
    objective = "max z = 3x1 + 5x2"
    constraints = [
        "4x1 + x2 >= 4",
        "-x1 + 2x2 >= 2",
        "x2 <= 3",
        "x1 >= 0",
        "x2 >= 0"
    ]
    
    result = solve_two_phase_simplex(objective, constraints)
    
    print("\n" + "="*70)
    print("📊 RESULTADO:")
    print("="*70)
    print(f"Success: {result.get('success')}")
    print(f"Status: {result.get('status', 'N/A')}")
    if 'error' in result:
        print(f"Error: {result['error']}")
