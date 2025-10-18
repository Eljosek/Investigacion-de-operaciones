"""
Test de Integración Completa - Todos los Métodos
Verifica que Simplex (con Dos Fases) y Dual-Simplex (MIN/MAX) funcionen
"""

print("=" * 80)
print("🧪 TEST DE INTEGRACIÓN COMPLETA")
print("=" * 80)
print()

# Test 1: Simplex estándar (MAX con <=)
print("📝 TEST 1: Simplex Estándar (MAX con <=)")
print("-" * 80)
from simplex_tableau import solve_simplex_tableau

objective = "max z = 3x1 + 2x2"
constraints = ["x1 + x2 <= 6", "2x1 + x2 <= 8"]
result = solve_simplex_tableau(objective, constraints)

print(f"Objetivo: {objective}")
print(f"Restricciones: {constraints}")
print(f"✅ Success: {result['success']}")
if result['success']:
    print(f"✅ Z óptimo: {result['optimal_value']}")
    print(f"✅ Solución: {result['solution']}")
    print(f"✅ Iteraciones: {len(result['iterations'])}")
else:
    print(f"❌ Error: {result.get('error')}")
print()

# Test 2: Simplex con >= (debe rechazar y sugerir Dual-Simplex)
print("📝 TEST 2: Simplex con >= (validación)")
print("-" * 80)

objective = "max z = 3x1 + 2x2"
constraints = ["x1 + x2 >= 4"]
result = solve_simplex_tableau(objective, constraints)

print(f"Objetivo: {objective}")
print(f"Restricciones: {constraints}")
print(f"✅ Success: {result['success']} (esperado: False)")
if not result['success']:
    print(f"✅ Mensaje: {result.get('error')[:60]}...")
print()

# Test 3: Simplex Dos Fases (MIN con >=)
print("📝 TEST 3: Simplex Dos Fases (MIN con >=)")
print("-" * 80)

objective = "min z = 10x1 + 30x2"
constraints = ["x1 + 5x2 >= 15", "5x1 + x2 >= 15"]
result = solve_simplex_tableau(objective, constraints)

print(f"Objetivo: {objective}")
print(f"Restricciones: {constraints}")
print(f"Resultado esperado: x1=2.5, x2=2.5, Z=100")

if result['success']:
    print(f"✅ Success: {result['success']}")
    print(f"✅ Z óptimo: {result['optimal_value']} (esperado: 100)")
    print(f"✅ Solución: {result['solution']}")
    print(f"✅ Iteraciones: {len(result['iterations'])}")
    
    # Validación
    x1_ok = abs(result['solution']['x1'] - 2.5) < 0.01
    x2_ok = abs(result['solution']['x2'] - 2.5) < 0.01
    z_ok = abs(result['optimal_value'] - 100.0) < 0.1
    
    if x1_ok and x2_ok and z_ok:
        print("✅✅✅ TODAS LAS VALIDACIONES PASARON")
    else:
        print(f"❌ Validación fallida: x1={x1_ok}, x2={x2_ok}, Z={z_ok}")
else:
    print(f"❌ Error: {result.get('error')}")
print()

# Test 4: Dual-Simplex MIN
print("📝 TEST 4: Dual-Simplex MIN")
print("-" * 80)
from dual_simplex_tableau import solve_dual_simplex_tableau

objective = "min z = 3x1 + 2x2"
constraints = ["3x1 + x2 >= 3", "4x1 + 3x2 >= 6", "x1 + x2 <= 3"]
result = solve_dual_simplex_tableau(objective, constraints)

print(f"Objetivo: {objective}")
print(f"Restricciones: {constraints}")
print(f"Resultado esperado: x1=0.6, x2=1.2, Z=4.2")

if result['success']:
    print(f"✅ Success: {result['success']}")
    print(f"✅ Z óptimo: {result['optimal_value']} (esperado: 4.2)")
    print(f"✅ Solución: {result['solution']}")
    print(f"✅ Iteraciones: {len(result['iterations'])}")
    
    # Validación
    x1_ok = abs(result['solution']['x1'] - 0.6) < 0.01
    x2_ok = abs(result['solution']['x2'] - 1.2) < 0.01
    z_ok = abs(result['optimal_value'] - 4.2) < 0.1
    
    if x1_ok and x2_ok and z_ok:
        print("✅✅✅ TODAS LAS VALIDACIONES PASARON")
    else:
        print(f"❌ Validación fallida: x1={x1_ok}, x2={x2_ok}, Z={z_ok}")
else:
    print(f"❌ Error: {result.get('error')}")
print()

# Test 5: Dual-Simplex MAX
print("📝 TEST 5: Dual-Simplex MAX")
print("-" * 80)

objective = "max z = 5x1 + 4x2"
constraints = ["x1 + 2x2 >= 6", "3x1 + x2 >= 9"]
result = solve_dual_simplex_tableau(objective, constraints)

print(f"Objetivo: {objective}")
print(f"Restricciones: {constraints}")
print(f"Resultado esperado: Z=19.2, x1=2.4, x2=1.8")

if result['success']:
    print(f"✅ Success: {result['success']}")
    print(f"✅ Z óptimo: {result['optimal_value']} (esperado: 19.2)")
    print(f"✅ Solución: {result['solution']}")
    print(f"✅ Iteraciones: {len(result['iterations'])}")
    
    # Validación
    x1_ok = abs(result['solution']['x1'] - 2.4) < 0.01
    x2_ok = abs(result['solution']['x2'] - 1.8) < 0.01
    z_ok = abs(result['optimal_value'] - 19.2) < 0.1
    
    if x1_ok and x2_ok and z_ok:
        print("✅✅✅ TODAS LAS VALIDACIONES PASARON")
    else:
        print(f"❌ Validación fallida: x1={x1_ok}, x2={x2_ok}, Z={z_ok}")
else:
    print(f"❌ Error: {result.get('error')}")
print()

print("=" * 80)
print("🎉 TEST DE INTEGRACIÓN COMPLETADO")
print("=" * 80)
