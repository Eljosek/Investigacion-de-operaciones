# Prueba con símbolos matemáticos ≥ y ≤
from lp_solver import solve_lp_problem

def test_mathematical_symbols():
    print("🧪 Probando símbolos matemáticos ≥ y ≤...")
    print("=" * 50)
    
    # Problema de prueba con símbolos matemáticos
    objective = "maximizar z = 2x + 3y"
    constraints = [
        "x + y ≤ 6",
        "2x + y ≤ 8", 
        "x ≥ 0",
        "y ≥ 0"
    ]
    
    print(f"Función objetivo: {objective}")
    print("Restricciones con símbolos matemáticos:")
    for i, constraint in enumerate(constraints, 1):
        print(f"  {i}. {constraint}")
    
    print("\n🔄 Resolviendo...")
    
    try:
        result = solve_lp_problem(objective, constraints)
        
        if result['success']:
            print("✅ ¡ÉXITO! Los símbolos matemáticos funcionan correctamente.")
            print(f"📍 Punto óptimo: {result['best_point']}")
            print(f"🎯 Valor óptimo: {result['best_value']:.4f}")
            print(f"📐 Vértices encontrados: {len(result['vertices'])}")
            
            print("\n📊 Vértices de la región factible:")
            for i, vertex in enumerate(result['vertices'], 1):
                print(f"  V{i}: ({vertex[0]:.2f}, {vertex[1]:.2f})")
            
            print("\n🎉 Los símbolos ≥ y ≤ funcionan perfectamente!")
            
        else:
            print(f"❌ Error: {result['error']}")
            
    except Exception as e:
        print(f"💥 Error inesperado: {e}")
    
    print("=" * 50)

if __name__ == "__main__":
    test_mathematical_symbols()