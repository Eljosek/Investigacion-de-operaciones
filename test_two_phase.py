"""
Test para depurar el problema de Dos Fases con "unbounded"
"""
from simplex_tableau_new import SimplexTableau
import numpy as np

# Test Case: min z = 10x1 + 30x2
# s.a.:
#   x1 + 5x2 >= 15
#   5x1 + x2 >= 15
#   x1, x2 >= 0
# Solución esperada: x1=2.5, x2=2.5, Z=100

print("=" * 70)
print("Test: Simplex Dos Fases - MIN con >=")
print("=" * 70)
print("min Z = 10x1 + 30x2")
print("Restricciones:")
print("  x1 + 5x2 >= 15")
print("  5x1 + x2 >= 15")
print()
print("Solución esperada: x1=2.5, x2=2.5, Z=100")
print()

# Configurar problema
c = [10, 30]  # MIN, ya se convertirá internamente
A = [[1, 5], [5, 1]]
b = [15, 15]
constraint_types = ['>=', '>=']
opt_type = 'min'

# Crear tableau
print("CREANDO TABLEAU...")
tableau = SimplexTableau(c, A, b, constraint_types, opt_type)

print(f"Fase inicial: {tableau.phase}")
print(f"Variables originales: {tableau.n_original_vars}")
print(f"Variables de holgura: {tableau.n_slack}")
print(f"Variables de exceso: {tableau.n_surplus}")
print(f"Variables artificiales: {tableau.n_artificial}")
print(f"Variables artificiales indices: {tableau.artificial_vars}")
print(f"Variables básicas iniciales: {tableau.basic_vars}")
print()

print("TABLEAU INICIAL:")
print(np.array2string(tableau.tableau, precision=2, suppress_small=True, max_line_width=100))
print()

# Resolver
print("RESOLVIENDO...")
result = tableau.solve()

print("\n" + "=" * 70)
print("RESULTADO:")
print("=" * 70)
print(f"Success: {result.get('success')}")
print(f"Status: {result.get('status')}")

if result['success']:
    print(f"Valor Óptimo (Z): {result['optimal_value']}")
    print(f"Solución:")
    for var, val in result['solution'].items():
        print(f"  {var} = {val}")
    print(f"\nIteraciones totales: {len(result['iterations'])}")
    
    # Mostrar fases
    phase_1_iters = [it for it in result['iterations'] if it.get('phase') == 1]
    phase_2_iters = [it for it in result['iterations'] if it.get('phase') == 2]
    print(f"Fase I: {len(phase_1_iters)} iteraciones")
    print(f"Fase II: {len(phase_2_iters)} iteraciones")
    
    # Verificar resultado esperado
    print("\n" + "=" * 70)
    if abs(result['optimal_value'] - 100.0) < 0.1:
        print("✅ CORRECTO: Z = 100")
    else:
        print(f"❌ ERROR: Z esperado 100, obtenido {result['optimal_value']}")
else:
    print(f"❌ ERROR: {result.get('error')}")
    if 'iterations' in result:
        print(f"\nIteraciones ejecutadas: {len(result['iterations'])}")
        for it in result['iterations']:
            print(f"\nIteración {it['iteration']} (Fase {it.get('phase', '?')}):")
            print(f"  Descripción: {it.get('description', 'N/A')}")
            print(f"  Objetivo: {it['objective_value']}")
            print(f"  Entra: {it.get('entering_var', 'None')}, Sale: {it.get('leaving_var', 'None')}")
            print(f"  Óptimo: {it['is_optimal']}")
            if it.get('phase') == 2 and it['iteration'] == 3:
                # Mostrar tableau después de transición a Fase II
                print(f"  Z-row: {np.array2string(it['tableau'][-1], precision=3, suppress_small=True)}")
                print(f"  Variables básicas: {it['tableau_info']['basic_vars']}")

print("\n" + "=" * 70)
