# Instrucciones para la Sustentación del Parcial

## 📋 Checklist Antes de la Presentación

### Preparación Técnica
- [ ] Verificar que Python 3.x esté instalado
- [ ] Instalar dependencias: `pip install -r requirements.txt`
- [ ] Probar que la aplicación inicie correctamente: `python app.py`
- [ ] Verificar acceso a: `http://localhost:5000`

### Documentos para Imprimir
1. **README.md** - Documentación técnica completa
2. **DOCUMENTACION_COMPLETA.md** - Detalles técnicos del proyecto
3. **RESUMEN_SUSTENTACION.md** - Guía rápida de presentación
4. **Este archivo** - Checklist de sustentación

## 🚀 Demostración en Vivo

### Ejemplo 1: Primer Ejercicio del Taller
```
Función Objetivo: 3x + 2y (Maximizar)
Restricciones:
x + y <= 4
2x + y <= 6
```

### Ejemplo 2: Segundo Ejercicio del Taller
```
Función Objetivo: 2x + 3y (Maximizar)
Restricciones:
x + 2y <= 8
2x + y <= 6
```

### Ejemplo 3: Restricciones Variables (Funcionalidad Avanzada)
```
Función Objetivo: x + y (Maximizar)
Restricciones:
x + y <= 10
x <= y
y >= 2
```

## 🎯 Puntos Clave para Destacar

### Tecnologías Utilizadas
- **Backend**: Python + Flask
- **Frontend**: HTML5, CSS3, JavaScript + Bootstrap 5
- **Matemáticas**: NumPy para cálculos, Matplotlib para gráficos
- **UI/UX**: Modo oscuro, validación en tiempo real, símbolos matemáticos

### Características Técnicas Avanzadas
1. **Parseo de Restricciones Mejorado**: Soporta ≤, ≥, x≤y, y≥x
2. **Validación JavaScript**: 5 patrones RegEx diferentes
3. **Interfaz Responsiva**: Compatible con dispositivos móviles
4. **Modo Oscuro**: Persistente con localStorage

### Algoritmo Implementado
- **Método Gráfico** para programación lineal de 2 variables
- Cálculo de intersecciones de restricciones
- Evaluación de función objetivo en vértices
- Determinación de solución óptima

## 📊 Flujo de Demostración Sugerido

1. **Introducción** (2 min)
   - Explicar el propósito académico
   - Mostrar tecnologías utilizadas

2. **Demostración Básica** (5 min)
   - Resolver Primer Ejercicio del Taller
   - Mostrar gráfico y solución

3. **Características Avanzadas** (3 min)
   - Demostrar validación de entrada
   - Mostrar restricciones variables (x≤y)
   - Activar/desactivar modo oscuro

4. **Código Técnico** (5 min)
   - Mostrar parse_constraint() en lp_solver.py
   - Explicar validación JavaScript en app.js
   - Destacar estructura del proyecto

5. **Conclusiones** (2 min)
   - Aplicabilidad en investigación de operaciones
   - Potencial para extensiones futuras

## 🔗 Enlaces Importantes

- **Repositorio GitHub**: https://github.com/Eljosek/Investigacion-de-operaciones
- **Aplicación Local**: http://localhost:5000
- **Documentación Técnica**: README.md

## ⚡ Comandos Rápidos para la Demo

```bash
# Iniciar aplicación
python app.py

# Verificar dependencias
pip list

# Ver estructura del proyecto
dir /s
```

## 🎨 Tips de Presentación

- **Preparar ejemplos**: Tener los ejercicios del taller listos para copiar/pegar
- **Explicar decisiones técnicas**: Por qué Flask, por qué método gráfico
- **Mostrar responsividad**: Abrir en ventana pequeña para mostrar adaptabilidad
- **Destacar validación**: Intentar ingresar datos inválidos para mostrar retroalimentación
- **Código limpio**: Mencionar estructura organizada y comentarios

## 🏆 Fortalezas del Proyecto

1. **Completitud**: Solución end-to-end funcional
2. **Usabilidad**: Interfaz intuitiva y moderna
3. **Robustez**: Validación exhaustiva de entrada
4. **Escalabilidad**: Código modular y bien estructurado
5. **Documentación**: Completa y profesional
6. **Tecnología Moderna**: Stack actualizado y estándares web