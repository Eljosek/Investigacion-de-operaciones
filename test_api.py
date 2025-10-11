"""
Script de prueba para validar los endpoints JSON de la aplicación.
Verifica que los solvers devuelvan el formato correcto y Z=24 para el caso crítico.
"""

import requests
import json


def test_simplex_api():
    """Prueba el endpoint JSON del Simplex"""
    url = "http://localhost:5000/api/solve-simplex"
    
    # Caso crítico que debe dar Z=24
    data = {
        "objective": "minimizar z = 5x1 + 4x2 + 3x3",
        "constraints": [
            "x1 + x2 + x3 >= 8",
            "2x1 + x2 <= 12", 
            "x2 + 2x3 >= 6"
        ]
    }
    
    print("🔬 PROBANDO ENDPOINT: /api/solve-simplex")
    print(f"📋 Enviando: {json.dumps(data, indent=2)}")
    print("-" * 60)
    
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Status Code: {response.status_code}")
            print(f"📊 Resultado:")
            print(json.dumps(result, indent=2))
            
            # Verificar Z=24
            if result.get('opt_value') == 24.0:
                print(f"\n🎉🎉🎉 PERFECTO: Z = 24.0 (CORRECTO) 🎉🎉🎉")
            else:
                print(f"\n❌ ERROR: Z = {result.get('opt_value')}, esperado 24.0")
            
            return result
        else:
            print(f"❌ Error HTTP {response.status_code}: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return None


def test_dual_simplex_api():
    """Prueba el endpoint JSON del Dual Simplex"""
    url = "http://localhost:5000/api/solve-dual-simplex"
    
    # Mismo caso crítico
    data = {
        "objective": "minimizar z = 5x1 + 4x2 + 3x3",
        "constraints": [
            "x1 + x2 + x3 >= 8",
            "2x1 + x2 <= 12",
            "x2 + 2x3 >= 6"
        ]
    }
    
    print(f"\n{'=' * 60}")
    print("🎯 PROBANDO ENDPOINT: /api/solve-dual-simplex")
    print(f"📋 Enviando: {json.dumps(data, indent=2)}")
    print("-" * 60)
    
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Status Code: {response.status_code}")
            print(f"📊 Resultado:")
            print(json.dumps(result, indent=2))
            
            # Verificar Z=24
            if result.get('opt_value') == 24.0:
                print(f"\n🎉🎉🎉 PERFECTO: Z = 24.0 (CORRECTO) 🎉🎉🎉")
            else:
                print(f"\n❌ ERROR: Z = {result.get('opt_value')}, esperado 24.0")
            
            return result
        else:
            print(f"❌ Error HTTP {response.status_code}: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return None


def main():
    print("=" * 80)
    print("🚀 VALIDACIÓN ENDPOINTS JSON - CASO CRÍTICO Z=24")
    print("=" * 80)
    
    # Probar ambos endpoints
    simplex_result = test_simplex_api()
    dual_result = test_dual_simplex_api()
    
    print(f"\n{'=' * 80}")
    print("📈 RESUMEN DE VALIDACIÓN")
    print("=" * 80)
    
    if simplex_result and simplex_result.get('opt_value') == 24.0:
        print("✅ Simplex API: CORRECTO (Z=24)")
    else:
        print("❌ Simplex API: ERROR")
    
    if dual_result and dual_result.get('opt_value') == 24.0:
        print("✅ Dual Simplex API: CORRECTO (Z=24)")
    else:
        print("❌ Dual Simplex API: ERROR")
    
    if (simplex_result and simplex_result.get('opt_value') == 24.0 and 
        dual_result and dual_result.get('opt_value') == 24.0):
        print(f"\n🎊🎊🎊 ¡AMBOS ENDPOINTS VALIDADOS EXITOSAMENTE! 🎊🎊🎊")
        print("✅ La aplicación está lista para uso en producción")
    else:
        print(f"\n⚠️ Revisar endpoints con errores")
    
    print("=" * 80)


if __name__ == "__main__":
    main()