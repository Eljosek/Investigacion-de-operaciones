# Prueba rápida para verificar que las restricciones x >= 0, y >= 0 funcionen
from lp_solver import solve_lp_problem

def test_constraints():
    print("🧪 Probando restricciones x >= 0, y >= 0...")
    print("=" * 50)
    
    # Problema de prueba
    objective = "maximizar z = 3x + 2y"
    constraints = [
        "x + 2y <= 8",
        "2x + y <= 10", 
        "x >= 0",
        "y >= 0"
    ]
    
    print(f"Función objetivo: {objective}")
    print("Restricciones:")
    for i, constraint in enumerate(constraints, 1):
        print(f"  {i}. {constraint}")
    
    print("\n🔄 Resolviendo...")
    
    try:
        result = solve_lp_problem(objective, constraints)
        
        if result['success']:
            print("✅ ¡ÉXITO! El problema se resolvió correctamente.")
            print(f"📍 Punto óptimo: {result['best_point']}")
            print(f"🎯 Valor óptimo: {result['best_value']:.4f}")
            print(f"📐 Vértices encontrados: {len(result['vertices'])}")
            
            print("\n📊 Vértices de la región factible:")
            for i, vertex in enumerate(result['vertices'], 1):
                print(f"  V{i}: ({vertex[0]:.2f}, {vertex[1]:.2f})")
            
            print("\n🎉 Las restricciones x >= 0, y >= 0 funcionan correctamente!")
            
        else:
            print(f"❌ Error: {result['error']}")
            
    except Exception as e:
        print(f"💥 Error inesperado: {e}")
    
    print("=" * 50)

if __name__ == "__main__":
    test_constraints()