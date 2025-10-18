"""
Test para Dual-Simplex con MIN (verificar que no se rompió)
"""
from dual_simplex_tableau import solve_dual_simplex_tableau

# Test Case from previous success: min z = 3x1 + 2x2
# s.a.:
#   3x1 + x2 >= 3
#   4x1 + 3x2 >= 6
#   x1 + x2 <= 3

objective_str = "min z = 3x1 + 2x2"
constraints_list = [
    "3x1 + x2 >= 3",
    "4x1 + 3x2 >= 6",
    "x1 + x2 <= 3"
]

print("=" * 60)
print("Test: Dual-Simplex MIN (regresión)")
print("=" * 60)
print(f"Objetivo: {objective_str}")
print("Restricciones:")
for constraint in constraints_list:
    print(f"  {constraint}")
print()
print("Resultado esperado: Z = 4.2, x1 = 0.6, x2 = 1.2")
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
    
    # Verificar resultado esperado
    print("\n" + "=" * 60)
    if abs(result['optimal_value'] - 4.2) < 0.01:
        print("✅ CORRECTO: Z = 4.2")
    else:
        print(f"❌ ERROR: Z esperado 4.2, obtenido {result['optimal_value']}")
    
    if abs(result['solution']['x1'] - 0.6) < 0.01:
        print("✅ CORRECTO: x1 = 0.6")
    else:
        print(f"❌ ERROR: x1 esperado 0.6, obtenido {result['solution']['x1']}")
    
    if abs(result['solution']['x2'] - 1.2) < 0.01:
        print("✅ CORRECTO: x2 = 1.2")
    else:
        print(f"❌ ERROR: x2 esperado 1.2, obtenido {result['solution']['x2']}")
else:
    print(f"❌ ERROR: {result.get('error')}")

print("\n" + "=" * 60)
