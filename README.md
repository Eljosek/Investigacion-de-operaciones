# 📊 Programación Lineal - Método Gráfico

Una aplicación web desarrollada en Flask para resolver problemas de programación lineal con dos variables usando el método gráfico. 

**Desarrollado por José Herrera para la profesora Bibiana Patricia Arias Villada**  
**Universidad Tecnológica de Pereira (UTP) - Investigación de Operaciones - 2025**

## 🎯 Características

- **Interfaz web intuitiva** con formularios fáciles de usar
- **Visualización gráfica mejorada** de la región factible y punto óptimo
- **Cálculo automático** de vértices y evaluación de función objetivo
- **Soporte completo** para símbolos matemáticos (≥, ≤, =)
- **Rectas que pasan por el origen** correctamente manejadas
- **Modo oscuro** con persistencia en localStorage
- **Ejemplos incluidos** para practicar
- **Diseño responsivo** que funciona en móviles y escritorio
- **Explicaciones educativas** sobre el método gráfico
- **Región factible sombreada** con mejor visualización
- **Soporte para n restricciones** sin límites

## 🚀 Instalación y Uso

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 2: Ejecutar la aplicación

```bash
python app.py
```

### Paso 3: Abrir en navegador

Abre tu navegador web y ve a: `http://localhost:5000`

## 📁 Estructura del Proyecto

```
investigacion-de-operaciones/
│
├── app.py                 # Aplicación Flask principal
├── lp_solver.py          # Módulo con funciones de programación lineal
├── metodo_grafico.py     # Código original (versión terminal)
├── requirements.txt      # Dependencias de Python
├── README.md            # Este archivo
│
├── templates/           # Plantillas HTML
│   ├── base.html       # Plantilla base
│   ├── index.html      # Página principal
│   ├── results.html    # Página de resultados
│   ├── examples.html   # Página de ejemplos
│   └── about.html      # Página informativa
│
└── static/             # Archivos estáticos
    ├── css/
    │   └── styles.css  # Estilos personalizados
    ├── js/
    │   └── app.js      # JavaScript para interactividad
    └── images/         # Directorio para imágenes
```

## 🎮 Cómo Usar la Aplicación

### 1. Función Objetivo
Ingresa la función que quieres optimizar:
- **Maximización:** `maximizar z = 3x + 2y`
- **Minimización:** `minimizar z = 2x + 3y`

### 2. Restricciones
Ingresa una restricción por línea:
```
x + 2y <= 8
2x + y <= 10
x ≥ 0
y ≥ 0
```

### 3. Operadores Válidos
- `<=` o `≤` (menor o igual que)
- `>=` o `≥` (mayor o igual que)  
- `=` (igual a)

**¡Ahora soporta símbolos matemáticos reales!**

### 4. Resolver
Haz clic en "Resolver Problema" y la aplicación:
- Graficará las restricciones
- Mostrará la región factible sombreada
- Calculará los vértices
- Encontrará el punto óptimo
- Mostrará todos los resultados

## 📚 Ejemplos Incluidos

La aplicación incluye varios ejemplos predefinidos:

### Ejemplo 1: Maximización Básica
```
Objetivo: maximizar z = 3x + 2y
Restricciones:
x + 2y <= 8
2x + y <= 10
x >= 0
y >= 0
```

### Ejemplo 2: Minimización
```
Objetivo: minimizar z = 2x + 3y
Restricciones:
x + y >= 4
2x + y >= 6
x >= 0
y >= 0
```

### Ejemplo 3: Problema Mixto
```
Objetivo: maximizar z = x + 4y
Restricciones:
x + 2y <= 12
2x + y <= 16
x + y >= 5
x >= 0
y >= 0
```

## 🔧 Tecnologías Utilizadas

- **Backend:** Python + Flask
- **Cálculos:** NumPy
- **Gráficas:** Matplotlib
- **Frontend:** HTML5 + CSS3 + JavaScript
- **Diseño:** Bootstrap 5
- **Iconos:** Font Awesome

## 📖 Método Gráfico - Explicación

El método gráfico es ideal para problemas de programación lineal con dos variables:

1. **Graficar restricciones:** Cada restricción se representa como una línea
2. **Identificar región factible:** Área que satisface todas las restricciones
3. **Encontrar vértices:** Puntos de intersección de las líneas
4. **Evaluar función objetivo:** El óptimo siempre está en un vértice
5. **Seleccionar solución:** El vértice con mejor valor objetivo

## 🎓 Para Estudiantes

Esta aplicación es perfecta para:
- Aprender programación lineal visualmente
- Practicar con diferentes tipos de problemas
- Verificar soluciones de tareas
- Entender el concepto de región factible
- Prepararse para exámenes de Investigación de Operaciones

## ⚠️ Limitaciones

- Solo funciona con **2 variables** (x, y)
- Todas las restricciones deben ser **lineales**
- Los problemas deben tener **región factible acotada**
- Para problemas grandes, usar métodos como Simplex

## 🛠️ Desarrollo

### Agregar nuevas funcionalidades

1. **Nuevas rutas:** Edita `app.py`
2. **Funciones de cálculo:** Modifica `lp_solver.py`
3. **Interfaz:** Actualiza templates en `/templates/`
4. **Estilos:** Edita `/static/css/styles.css`

### Personalización

- Cambia colores en las variables CSS de `styles.css`
- Agrega nuevos ejemplos en la ruta `/examples` de `app.py`
- Modifica límites de gráfica en `create_plot()` de `lp_solver.py`

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
```bash
pip install flask
```

### Error: "No se encontró región factible"
- Verifica que las restricciones sean consistentes
- Asegúrate de incluir restricciones de no-negatividad
- Revisa el formato de las restricciones

### Gráfica no se muestra
- Verifica que matplotlib esté instalado
- Revisa que el backend de matplotlib esté configurado correctamente

## 📞 Soporte

Si encuentras problemas o tienes sugerencias:
1. Revisa este README
2. Verifica que todas las dependencias estén instaladas
3. Comprueba la sintaxis de tu problema de LP
4. Consulta los ejemplos incluidos

## � Despliegue Web

La aplicación está preparada para desplegarse en plataformas como:

- **Render** (recomendado) - Gratuito y fácil
- **Heroku** - Robusto y confiable  
- **Railway** - Moderno y rápido
- **Vercel** - Para versiones estáticas

Ver `DEPLOYMENT.md` para instrucciones detalladas.

## 🌟 Funcionalidades Implementadas

- ✅ **Símbolos matemáticos** (≥, ≤) funcionando perfectamente
- ✅ **Modo oscuro** con toggle persistente
- ✅ **Región factible** sombreada correctamente
- ✅ **Rectas por el origen** soportadas
- ✅ **n restricciones** sin límites
- ✅ **Diseño responsivo** para todos los dispositivos
- ✅ **Información institucional** UTP actualizada

## 🎓 Información Académica

**Universidad:** Universidad Tecnológica de Pereira (UTP)  
**Materia:** Investigación de Operaciones  
**Profesora:** Bibiana Patricia Arias Villada  
**Estudiante:** José Herrera  
**Año:** 2025  

---

**¡Perfecto para tu parcial de Investigación de Operaciones!** 🎓

*"Esta web fue creada por José Herrera para la profesora Bibiana Patricia Arias Villada en la materia de Investigación de Operaciones."*

*Desarrollado con ❤️ para estudiantes de la UTP*