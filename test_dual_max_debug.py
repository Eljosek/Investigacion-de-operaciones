"""
Test detallado para Dual-Simplex con MAX
"""
from dual_simplex_tableau import DualSimplexTableau

# Test Case: max z = 5x1 + 4x2
# s.a.:
#   x1 + 2x2 >= 6  →  -x1 - 2x2 <= -6
#   3x1 + x2 >= 9  →  -3x1 - x2 <= -9

import numpy as np

c = [5, 4]  # Coeficientes originales MAX
A = [
    [-1, -2],  # >= 6 convertido a <= -6
    [-3, -1]   # >= 9 convertido a <= -9
]
b = [-6, -9]

print("=" * 70)
print("Test DIRECTO: Dual-Simplex MAX")
print("=" * 70)
print(f"Problema original: max Z = {c[0]}x1 + {c[1]}x2")
print(f"  x1 + 2x2 >= 6")
print(f"  3x1 + x2 >= 9")
print()
print(f"Problema convertido (forma estándar Dual-Simplex):")
print(f"  max Z = {c[0]}x1 + {c[1]}x2")
print(f"  {A[0][0]}x1 + {A[0][1]}x2 + s1 = {b[0]}")
print(f"  {A[1][0]}x1 + {A[1][1]}x2 + s2 = {b[1]}")
print()

# Crear tableau directamente
tableau = DualSimplexTableau(c, A, b, 'max')

print("TABLEAU INICIAL:")
print("-" * 70)
print(f"Variables: x1, x2, s1, s2, RHS")
print(np.array2string(tableau.tableau, precision=2, suppress_small=True))
print(f"Variables básicas: {tableau.basic_vars}")
print(f"Número de variables: {tableau.n_vars}")
print(f"Número de restricciones: {tableau.n_constraints}")
print()

# Verificar dual-factibilidad inicial
z_row = tableau.tableau[-1, :-1]
print(f"Fila Z (dual-factibilidad): {z_row}")
print(f"¿Dual-factible? (todos >= 0): {all(z_row >= -1e-10)}")
print()

# Verificar primal-factibilidad inicial
rhs_values = [tableau.tableau[i, -1] for i in range(tableau.n_constraints)]
print(f"RHS (primal-factibilidad): {rhs_values}")
print(f"¿Primal-factible? (todos >= 0): {all(rhs >= -1e-10 for rhs in rhs_values)}")
print()

# Resolver
result = tableau.solve()

print("=" * 70)
print("RESULTADO:")
print("=" * 70)
print(f"Success: {result.get('success')}")
print(f"Status: {result.get('status')}")

if result['success']:
    print(f"Valor Óptimo (Z): {result['optimal_value']}")
    print(f"Solución:")
    for var, val in result['solution'].items():
        print(f"  {var} = {val}")
    print(f"\nIteraciones: {len(result['iterations'])}")
else:
    print(f"Error: {result.get('error')}")
    if 'iterations' in result:
        print(f"\nSe ejecutaron {len(result['iterations'])} iteraciones antes del error")
        for iter_data in result['iterations']:
            print(f"\n--- Iteración {iter_data['iteration']} ---")
            print(f"  RHS values: {[round(tableau.tableau[i, -1], 2) for i in range(tableau.n_constraints)]}")
            print(f"  Factible: {iter_data['is_feasible']}")
            if iter_data['entering_var']:
                print(f"  Entra: {iter_data['entering_var']}, Sale: {iter_data['leaving_var']}")

print("\n" + "=" * 70)
