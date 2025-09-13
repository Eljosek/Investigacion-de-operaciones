# 📋 RESUMEN EJECUTIVO - SUSTENTACIÓN DEL PARCIAL

## 🎯 ¿QUÉ ES MI APLICACIÓN?
Una aplicación web que resuelve problemas de **programación lineal** usando el **método gráfico** para 2 variables.

## 🏗️ ARQUITECTURA (3 CAPAS)
1. **Frontend**: HTML + CSS + JavaScript (validación)
2. **Backend**: Flask (Python) - maneja solicitudes web  
3. **Motor**: NumPy + Matplotlib (cálculos + gráficas)

## 🧮 ALGORITMO DEL MÉTODO GRÁFICO (5 PASOS)
1. **Parsear** función objetivo y restricciones
2. **Convertir** restricciones a forma estándar (ax + by ≤ c)
3. **Calcular vértices** (intersecciones de líneas)
4. **Evaluar** función objetivo en cada vértice
5. **Seleccionar** el óptimo (max o min)

## 📁 ARCHIVOS PRINCIPALES
- **app.py**: Servidor web Flask (rutas y lógica)
- **lp_solver.py**: Algoritmo matemático (corazón del sistema)
- **app.js**: Validación frontend (formato de entrada)
- **templates/**: Páginas HTML (interfaz de usuario)

## 🔧 TECNOLOGÍAS USADAS
- **Flask**: Framework web Python (simple y educativo)
- **NumPy**: Cálculos matemáticos y álgebra lineal
- **Matplotlib**: Generación de gráficas dinámicas
- **Bootstrap**: Diseño responsivo y profesional

## 📊 FUNCIONALIDADES CLAVE
✅ **Validación inteligente**: Acepta x≥6, y≤10, etc.  
✅ **Restricciones automáticas**: Agrega x≥0, y≥0 si faltan  
✅ **Modo oscuro**: CSS variables dinámicas  
✅ **Gráficas dinámicas**: Matplotlib → Base64 → HTML  
✅ **Ejercicios del taller**: Los 2 ejercicios implementados  

## 🧪 EJERCICIOS DEL TALLER
**Ejercicio 1:** maximizar z = x + y, restricciones: x+3y≤26, 4x+3y≤44, 2x+3y≤28  
**Ejercicio 2:** minimizar z = 3x + 2y, restricciones: 3x+4y≤12, 3x+2y≥2

## 💡 PREGUNTAS PROBABLES Y RESPUESTAS

**P: ¿Por qué Flask y no otra cosa?**  
**R:** Ligero, educativo, ideal para proyectos académicos pequeños.

**P: ¿Cómo encuentra los vértices?**  
**R:** Intersecta cada par de líneas, verifica factibilidad con todas las restricciones.

**P: ¿Qué pasa si no hay solución?**  
**R:** El algoritmo detecta región vacía y retorna error descriptivo.

**P: ¿Por qué solo evaluar en vértices?**  
**R:** Teorema fundamental: la solución óptima siempre está en un vértice de la región factible.

**P: ¿Cómo valida las restricciones?**  
**R:** JavaScript con 3 patrones RegEx: completas (ax+by≤c), solo x, solo y.

## 🎓 PUNTOS FUERTES PARA DESTACAR
1. **Implementación propia** del algoritmo (no librerías externas)
2. **Validación robusta** (acepta múltiples formatos)
3. **Interfaz profesional** (Bootstrap + modo oscuro)
4. **Código limpio** (separación frontend/backend)
5. **Ejercicios específicos** del taller implementados

## 🚀 DEMOSTRACIÓN EN VIVO
1. Abrir http://localhost:5000
2. Mostrar Ejercicio 1 del taller
3. Explicar la gráfica generada
4. Mostrar modo oscuro
5. Explicar validación con entrada incorrecta

---
**TIEMPO DE SUSTENTACIÓN: 5-10 minutos**  
**ARCHIVOS PARA IMPRIMIR: app.py + lp_solver.py + app.js (13 páginas)**