import dual_simplex_tableau

# Test Dual Simplex
objective = "min z = 2x1 + 3x2"
constraints = [
    "x1 + 2x2 >= 6",
    "2x1 + x2 >= 8"
]

result = dual_simplex_tableau.solve_dual_simplex_tableau(objective, constraints)
print(f"Success: {result['success']}")
print(f"Status: {result['status']}")
print(f"Optimal: {result.get('optimal_value', 'N/A')}")
print(f"Solution: {result.get('solution', {})}")
print(f"Opt Type: {result.get('opt_type', 'unknown')}")
print(f"Iterations: {len(result.get('iterations', []))}")

# Verificar el tableau final
if result.get('iterations'):
    final_iter = result['iterations'][-1]
    print(f"\nTableau final:")
    print(final_iter['tableau'])
    print(f"\nValor en tableau[-1, -1]: {final_iter['tableau'][-1, -1]}")
    print(f"z_value calculado: {final_iter['z_value']}")
