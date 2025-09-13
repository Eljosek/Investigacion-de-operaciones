# 📚 DOCUMENTACIÓN COMPLETA DEL CÓDIGO
## Parcial de Investigación de Operaciones - Método Gráfico
**Estudiante:** José Herrera  
**Profesora:** Bibiana Patricia Arias Villada  
**Universidad:** Universidad Tecnológica de Pereira (UTP)

---

## 🎯 DESCRIPCIÓN DEL PARCIAL

Esta aplicación web implementa el **método gráfico** para resolver problemas de programación lineal con dos variables. Permite ingresar funciones objetivo y restricciones, y visualiza gráficamente la región factible junto con la solución óptima.

---

## 📁 ESTRUCTURA DEL PROYECTO

```
investigacion-de-operaciones/
├── app.py                  # Aplicación Flask principal
├── lp_solver.py           # Motor de resolución de programación lineal
├── metodo_grafico.py      # Versión original en terminal (referencia)
├── requirements.txt       # Dependencias de Python
├── README.md             # Documentación del proyecto
├── static/
│   ├── css/
│   │   └── styles.css    # Estilos personalizados y modo oscuro
│   ├── js/
│   │   └── app.js        # JavaScript para validación e interactividad
│   └── images/           # Directorio para imágenes (si las hubiera)
└── templates/
    ├── base.html         # Plantilla base con navegación
    ├── index.html        # Página principal con formulario
    ├── results.html      # Página de resultados con gráfica
    ├── examples.html     # Página con ejemplos del taller
    └── about.html        # Información sobre el método gráfico
```

---

## 🔧 ARCHIVOS PRINCIPALES Y SU FUNCIÓN

### 1. **app.py** - Aplicación Flask Principal
```python
# Configuración de Flask y rutas principales
from flask import Flask, render_template, request, flash, redirect, url_for
from lp_solver import solve_lp_problem
```

**Funciones principales:**
- `index()`: Muestra el formulario principal
- `solve()`: Procesa el problema de LP y muestra resultados
- `examples()`: Muestra los ejercicios del taller
- `about()`: Información sobre el método gráfico

### 2. **lp_solver.py** - Motor de Resolución
```python
# Funciones matemáticas para resolver programación lineal
import numpy as np
import matplotlib.pyplot as plt
```

**Funciones principales:**
- `parse_objective(obj_str)`: Analiza la función objetivo
- `parse_constraint(constraint_str)`: Analiza las restricciones
- `compute_vertices(constraints)`: Calcula vértices de la región factible
- `create_plot(...)`: Genera la gráfica del método gráfico
- `solve_lp_problem(...)`: Función principal que resuelve el problema

### 3. **static/js/app.js** - Validación Frontend
```javascript
// Validación en tiempo real del formulario
function validateConstraintsString(constraints) {
    // Valida formato de restricciones incluyendo x>=6, y>=4, etc.
}
```

**Funciones principales:**
- `validateForm()`: Validación completa del formulario
- `validateObjectiveString()`: Valida formato de función objetivo
- `validateConstraintsString()`: Valida formato de restricciones
- `toggleDarkMode()`: Cambia entre modo claro/oscuro

---

## 🧮 ALGORITMO DEL MÉTODO GRÁFICO

### Paso 1: Parseo
```python
def parse_objective(obj_str):
    # Busca "maximizar" o "minimizar"
    if 'max' in obj_str.lower():
        opt_type = 'max'
    else:
        opt_type = 'min'
    
    # Extrae coeficientes de x e y
    # Ejemplo: "maximizar z = 3x + 2y" → [3, 2]
```

### Paso 2: Análisis de Restricciones
```python
def parse_constraint(s):
    # Convierte "x + 2y <= 8" en:
    # a=1, b=2, op='<=', rhs=8
    
    # Maneja símbolos matemáticos: ≤ → <=, ≥ → >=
    s = s.replace('≤', '<=').replace('≥', '>=')
```

### Paso 3: Cálculo de Vértices
```python
def compute_vertices(constraints):
    # 1. Convierte restricciones a forma estándar
    # 2. Encuentra intersecciones de líneas
    # 3. Verifica factibilidad de cada punto
    # 4. Retorna vértices válidos
```

### Paso 4: Optimización
```python
# Evalúa función objetivo en cada vértice
for vertex in vertices:
    x, y = vertex
    value = obj_coeffs[0] * x + obj_coeffs[1] * y
    
    if opt_type == 'max':
        if value > best_value:
            best_value = value
            best_point = vertex
```

### Paso 5: Visualización
```python
def create_plot(...):
    # 1. Dibuja líneas de restricciones
    # 2. Sombreada región factible
    # 3. Marca vértices
    # 4. Dibuja líneas de nivel de función objetivo
    # 5. Resalta punto óptimo
```

---

## 📊 CARACTERÍSTICAS TÉCNICAS

### **Frontend (HTML/CSS/JavaScript):**
- **Bootstrap 5**: Framework CSS responsivo
- **Font Awesome**: Iconos vectoriales
- **Modo Oscuro**: Implementado con CSS variables
- **Validación en Tiempo Real**: JavaScript con RegEx avanzados
- **Diseño Responsivo**: Adaptable a móviles y escritorio

### **Backend (Python/Flask):**
- **Flask**: Framework web minimalista
- **NumPy**: Cálculos matemáticos y álgebra lineal
- **Matplotlib**: Generación de gráficas
- **Base64**: Codificación de imágenes para web

### **Matemáticas:**
- **Algebra Lineal**: Resolución de sistemas de ecuaciones
- **Geometría Computacional**: Cálculo de intersecciones
- **Optimización**: Evaluación de función objetivo en vértices

---

## 🎓 EJERCICIOS DEL TALLER IMPLEMENTADOS

### **Ejercicio 1 - Maximización:**
```
maximizar z = x + y
sujeto a:
x + 3y ≤ 26
4x + 3y ≤ 44  
2x + 3y ≤ 28
x ≥ 0, y ≥ 0
```

### **Ejercicio 2 - Minimización:**
```
minimizar z = 3x + 2y
sujeto a:
3x + 4y ≤ 12
3x + 2y ≥ 2
x ≥ 0, y ≥ 0
```

---

## 🔍 ASPECTOS TÉCNICOS AVANZADOS

### **1. Manejo de Restricciones Implícitas:**
```python
# El sistema agrega automáticamente x≥0, y≥0 si no están presentes
if not has_x_nonneg:
    ineqs.append((-1, 0, 0))  # -x ≤ 0 → x ≥ 0
if not has_y_nonneg:
    ineqs.append((0, -1, 0))  # -y ≤ 0 → y ≥ 0
```

### **2. Validación Robusta de Entrada:**
```javascript
// Acepta múltiples formatos de restricciones
const patterns = [
    /^[+-]?\s*\d*\.?\d*\s*x\s*[+-]\s*\d*\.?\d*\s*y\s*(<=|>=|=|≤|≥)\s*[+-]?\d+\.?\d*$/,
    /^[+-]?\s*\d*\.?\d*\s*x\s*(<=|>=|=|≤|≥)\s*[+-]?\d+\.?\d*$/,
    /^[+-]?\s*\d*\.?\d*\s*y\s*(<=|>=|=|≤|≥)\s*[+-]?\d+\.?\d*$/
];
```

### **3. Generación Dinámica de Gráficas:**
```python
# Código optimizado para generar visualizaciones claras
plt.style.use('default')
fig, ax = plt.subplots(figsize=(10, 8))

# Región factible con gradiente de color
ax.fill(region_x, region_y, alpha=0.3, color='lightblue', label='Región Factible')

# Punto óptimo destacado
ax.plot(best_x, best_y, 'ro', markersize=12, label=f'Óptimo: ({best_x}, {best_y})')
```

---

## 🚀 CÓMO EJECUTAR LA APLICACIÓN

### **Requisitos:**
- Python 3.7+
- Flask
- NumPy  
- Matplotlib

### **Instalación:**
```bash
# 1. Clonar repositorio
git clone https://github.com/Eljosek/Investigacion-de-operaciones.git

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar aplicación
python app.py

# 4. Abrir navegador en http://localhost:5000
```

---

## 💡 PREGUNTAS FRECUENTES PARA SUSTENTACIÓN

### **P: ¿Por qué usar Flask en lugar de Django?**
**R:** Flask es más ligero y apropiado para aplicaciones pequeñas como esta. Permite mayor control sobre la estructura y es ideal para prototipos académicos.

### **P: ¿Cómo maneja la aplicación restricciones inconsistentes?**
**R:** El algoritmo verifica la factibilidad de cada vértice candidato contra todas las restricciones. Si no encuentra vértices factibles, retorna un error informativo.

### **P: ¿Por qué no usar librerías como PuLP o SciPy?**
**R:** Para fines educativos, implementar el algoritmo desde cero permite entender mejor el método gráfico y sus fundamentos matemáticos.

### **P: ¿Cómo garantiza la precisión numérica?**
**R:** Usa tolerancias numéricas (ε = 1e-9) para comparaciones de flotantes y maneja casos especiales como líneas paralelas.

---

## 📝 CÓDIGO PARA IMPRIMIR

### **Recomendación de archivos a imprimir:**

1. **app.py** (principal) - 4 páginas
2. **lp_solver.py** (algoritmo) - 6 páginas  
3. **static/js/app.js** (validación) - 3 páginas
4. Esta documentación - 3 páginas

**Total: ~16 páginas**

### **Archivos NO necesarios para imprimir:**
- HTML templates (son principalmente estructura)
- CSS styles (son presentación)
- requirements.txt, README.md (archivos de configuración)

---

## 🎯 PUNTOS CLAVE PARA LA SUSTENTACIÓN

1. **Algoritmo**: Conocer los 5 pasos del método gráfico
2. **Matemáticas**: Entender intersección de líneas y evaluación de función objetivo
3. **Tecnología**: Explicar por qué Flask + NumPy + Matplotlib
4. **Validación**: Cómo maneja diferentes formatos de entrada
5. **Visualización**: Cómo genera las gráficas dinámicamente
6. **Optimización**: Por qué evaluar solo en vértices es suficiente

---

**¡Preparado para el parcial! 🎓✨**