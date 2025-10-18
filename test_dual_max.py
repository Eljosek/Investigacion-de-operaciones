"""
Test para Dual-Simplex con MAX
"""
from dual_simplex_tableau import solve_dual_simplex_tableau

# Test Case: max z = 5x1 + 4x2
# s.a.:
#   x1 + 2x2 >= 6
#   3x1 + x2 >= 9
#   x1, x2 >= 0

objective_str = "max z = 5x1 + 4x2"
constraints_list = [
    "x1 + 2x2 >= 6",
    "3x1 + x2 >= 9"
]

print("=" * 60)
print("Test: Dual-Simplex MAX")
print("=" * 60)
print(f"Objetivo: {objective_str}")
print("Restricciones:")
for constraint in constraints_list:
    print(f"  {constraint}")
print()

# Ejecutar Dual-Simplex
result = solve_dual_simplex_tableau(objective_str, constraints_list)

# Mostrar resultado
print("RESULTADO:")
print("-" * 60)
print(f"Success: {result.get('success')}")
print(f"Status: {result.get('status')}")

if result['success']:
    print(f"Valor Óptimo (Z): {result['optimal_value']}")
    print(f"Solución:")
    for var, val in result['solution'].items():
        print(f"  {var} = {val}")
    print(f"Factibilidad dual: {result.get('factibilidad_dual')}")
    print(f"Estado final: {result.get('estado_final')}")
    print(f"\nIteraciones: {len(result['iterations'])}")
    
    # Mostrar cada iteración
    for iter_data in result['iterations']:
        print(f"\n--- Iteración {iter_data['iteration']} ---")
        print(f"  Factible: {iter_data['is_feasible']}")
        print(f"  Óptimo: {iter_data['is_optimal']}")
        print(f"  Valor objetivo: {iter_data['objective_value']}")
        if iter_data['entering_var'] and iter_data['leaving_var']:
            print(f"  Entra: {iter_data['entering_var']}, Sale: {iter_data['leaving_var']}")
            print(f"  Pivot: {iter_data['pivot_element']}")
else:
    print(f"Error: {result.get('error')}")

print("\n" + "=" * 60)
