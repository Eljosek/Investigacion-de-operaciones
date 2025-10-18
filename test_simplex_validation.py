"""
Test para validación de Simplex con restricciones >= o =
"""
from simplex_tableau import solve_simplex_tableau

print("=" * 70)
print("Test 1: Simplex con restricciones >= (debe rechazar)")
print("=" * 70)

objective_str = "max z = 3x1 + 2x2"
constraints_list = [
    "x1 + x2 >= 4",  # Restricción >=
    "2x1 + x2 <= 6"
]

result = solve_simplex_tableau(objective_str, constraints_list)

print(f"Success: {result.get('success')}")
print(f"Status: {result.get('status')}")
if not result['success']:
    print(f"Error (esperado): {result.get('error')}")

print("\n" + "=" * 70)
print("Test 2: Simplex con restricciones = (debe rechazar)")
print("=" * 70)

objective_str = "min z = 2x1 + 3x2"
constraints_list = [
    "x1 + x2 = 5",  # Restricción =
    "x1 + 2x2 <= 8"
]

result = solve_simplex_tableau(objective_str, constraints_list)

print(f"Success: {result.get('success')}")
print(f"Status: {result.get('status')}")
if not result['success']:
    print(f"Error (esperado): {result.get('error')}")

print("\n" + "=" * 70)
print("Test 3: Simplex con solo <= (debe funcionar)")
print("=" * 70)

objective_str = "max z = 3x1 + 2x2"
constraints_list = [
    "x1 + x2 <= 6",
    "2x1 + x2 <= 8"
]

result = solve_simplex_tableau(objective_str, constraints_list)

print(f"Success: {result.get('success')}")
print(f"Status: {result.get('status')}")
if result['success']:
    print(f"Z óptimo: {result.get('optimal_value')}")
    print(f"Solución: {result.get('solution')}")
    print("✅ CORRECTO: Simplex acepta restricciones <=")
else:
    print(f"❌ ERROR inesperado: {result.get('error')}")

print("\n" + "=" * 70)
