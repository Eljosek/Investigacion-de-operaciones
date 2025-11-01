# 📊 Programación Lineal - Aplicación Web Educativa# 📊 Solucionador de Programación Lineal - Aplicación Web Educativa



<div align="center">**Investigación de Operaciones - Proyecto**  

**Universidad Tecnológica de Pereira (UTP)**

![Python](https://img.shields.io/badge/Python-3.13.7-blue?logo=python&logoColor=white)

![Flask](https://img.shields.io/badge/Flask-3.1.2-green?logo=flask&logoColor=white)**Desarrollado por:** José Miguel Herrera Gutiérrez  

![NumPy](https://img.shields.io/badge/NumPy-2.3.3-orange?logo=numpy&logoColor=white)**Profesora:** Bibiana Patricia Arias Villada  

![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)**Versión:** 3.0  

![License](https://img.shields.io/badge/License-MIT-yellow)**Fecha:** Octubre 2025



**Investigación de Operaciones**  ---

Universidad Tecnológica de Pereira (UTP)

## 📋 Descripción

Desarrollado por **José Miguel Herrera Gutiérrez**  

Profesora: **Bibiana Patricia Arias Villada**Aplicación web completa para resolver problemas de **Programación Lineal** con tres métodos diferentes:



</div>1. **Método Gráfico** - Para problemas con 2 variables

2. **Método Simplex** - Para múltiples variables con restricciones <=

---3. **Método Dual-Simplex** - Optimizado para problemas con restricciones >=



## 🎯 DescripciónLa aplicación está diseñada con **enfoque educativo**, mostrando paso a paso cada iteración del algoritmo con tablas (tableau) completas, variables básicas, operaciones de pivoteo y valores objetivo.



Aplicación web educativa completa para resolver problemas de **Programación Lineal** con **4 métodos diferentes**, cada uno con visualización paso a paso de iteraciones y tableaux completos.## ✨ Características Principales



### 🔢 Métodos Implementados### 🎨 Interfaz Moderna

- **Diseño responsivo** con Bootstrap 5

| Método | Variables | Restricciones | Características |- **Modo oscuro** con variables CSS personalizadas

|--------|-----------|---------------|-----------------|- **Colores distintivos** por método (Azul/Verde/Púrpura)

| 🟢 **Método Gráfico** | 2 | ≤, ≥ | Visualización con Matplotlib, región factible |- **Iconos Font Awesome** para mejor UX

| 🟡 **Simplex Estándar** | 2+ | ≤ | Tableau manual, variables de holgura |- **Tooltips interactivos** en formularios

| 🔵 **Dual Simplex** | 2+ | ≥ | Ratios duales, minimización/maximización |- **Navegación fluida** con smooth scroll

| 🟠 **Simplex Dos Fases** | 2+ | ≤, ≥, = | Variables artificiales, Fase I y II |

### 🔢 Tres Métodos de Solución

---

| Método | Ideal Para | Restricciones | Algoritmo |

## ✨ Funcionalidades|--------|------------|---------------|-----------|

| **Gráfico** | 2 variables | <= | Intersecciones y vértices |

### 🎨 Interfaz de Usuario| **Simplex** | 2-5+ variables | <= | Simplex estándar con tableau |

- ✅ **Diseño moderno** con Bootstrap 5 y CSS personalizado| **Dual Simplex** | MIN con >= | >= | Dual Simplex para MAX y MIN |

- ✅ **Responsive design** - Compatible con móviles y tablets

- ✅ **Colores distintivos** por método (Verde, Amarillo, Azul, Naranja)### 🎯 Funcionalidades

- ✅ **Animaciones suaves** y transiciones fluidas

- ✅ **Iconos Font Awesome** para mejor UX- ✅ **Tres métodos de solución** con algoritmos optimizados

- ✅ **Visualización paso a paso** de iteraciones

### 📊 Visualización Educativa- ✅ **Tablas (tableau) interactivas** con resaltado de pivotes

- ✅ **Tableaux completos** con todas las variables- ✅ **Soporte para restricciones** `<=`, `>=`

- ✅ **Pivotes resaltados** en color amarillo- ✅ **Detección automática** de infactibilidad y no acotamiento

- ✅ **Variables básicas** identificadas en cada iteración- ✅ **Exportación a PDF** de resultados (función de impresión)

- ✅ **Valores de Z/W** actualizados paso a paso- ✅ **Ejemplos precargados** para cada método

- ✅ **Acordeones expandibles** para navegación fácil- ✅ **Interfaz responsiva** con Bootstrap 5



### 🧮 Algoritmos Matemáticos### 📚 Enfoque Educativo

- ✅ **Sin librerías de optimización externas** (implementación desde cero)

- ✅ **NumPy para operaciones matriciales**- **Visualización paso a paso** de cada iteración

- ✅ **Tolerancia numérica** (EPS = 1e-9)- **Tableau completo** con variables de holgura/exceso

- ✅ **Detección de infactibilidad** y problemas no acotados- **Pivotes identificados** con colores

- ✅ **Formato inteligente de números** (enteros sin decimales)- **Ratios calculados** (θ para Simplex, zⱼ/aᵢⱼ para Dual)

- **Explicaciones claras** de cada paso

### 📚 Contenido Educativo- **Variables básicas/no básicas** marcadas

- ✅ **Página "Acerca de"** con teoría de cada método

- ✅ **10 ejemplos precargados** (2-3 por cada método)### 🛠️ Implementación Manual

- ✅ **Explicaciones detalladas** del procedimiento

- ✅ **Comparaciones** entre métodos (ej. Dos Fases vs Big M)- **Sin librerías externas** de optimización (no PuLP, no SciPy)

- **NumPy puro** para operaciones matriciales

---- **Algoritmos escritos desde cero** para fines educativos

- **Código bien documentado** y legible

## 🛠️ Tecnologías- **Tolerancia numérica** (EPS = 1e-9)



### Backend---

```python

Python 3.13.7## 🛠️ Tecnologías Utilizadas

Flask 3.1.2        # Framework web

NumPy 2.3.3        # Operaciones matriciales### Backend

Matplotlib 3.10.1  # Gráficos (método gráfico)- **Python 3.13.7**

```- **Flask 3.1.2** - Framework web

- **NumPy 2.3.3** - Operaciones matriciales

### Frontend- **Matplotlib 3.10.1** - Gráficos del método gráfico

```html

HTML5 + Jinja2     # Templates dinámicos### Frontend

CSS3               # Variables personalizadas + animaciones- **HTML5** con plantillas Jinja2

JavaScript ES6+    # Interactividad- **CSS3** con variables personalizadas

Bootstrap 5.3      # Framework CSS- **JavaScript ES6+**

Font Awesome 6.6   # Iconografía- **Bootstrap 5.3** - Framework CSS

```- **Font Awesome 6.6** - Iconos

- **Google Fonts** - Poppins (títulos) e Inter (texto)

---

### Características CSS

## 📁 Estructura del Proyecto- **25+ variables CSS** para colores y tipografía

- **4 animaciones** (fade-in, slide-up, pulse, gradient-shift)

```- **Clases por método** (.method-grafico, .method-simplex, .method-dual)

Investigacion-de-operaciones/- **Modo oscuro** con prefers-color-scheme

│- **Gradientes** para CTAs y hero section

├── app.py                          # Aplicación Flask principal

├── lp_solver.py                    # Método Gráfico---

├── simplex_tableau.py              # Método Simplex

├── dual_simplex_tableau.py         # Método Dual Simplex## 📁 Estructura del Proyecto

├── two_phase_simplex.py            # Método Simplex Dos Fases

├── requirements.txt                # Dependencias Python```

├── README.md                       # Este archivoInvestigacion-de-operaciones/

│├── app.py                      # 🌐 Aplicación Flask con routes

├── static/├── lp_solver.py                # 📈 Método Gráfico (2 variables)

│   ├── css/├── simplex_tableau.py          # 🔢 Método Simplex (NumPy)

│   │   └── styles.css              # Estilos personalizados (1100+ líneas)├── dual_simplex_tableau.py     # 🔄 Método Dual Simplex (NumPy)

│   ├── js/├── requirements.txt            # 📦 Dependencias (Flask, NumPy, Matplotlib)

│   │   └── app.js                  # JavaScript interactivo├── README.md                   # 📖 Este archivo

│   └── images/                     # Imágenes generadas (gráficos)├── .gitignore                  # 🚫 Archivos ignorados (venv, __pycache__)

││

└── templates/├── static/

    ├── base.html                   # Plantilla base con navegación│   ├── css/

    ├── index.html                  # Página principal│   │   └── styles.css          # 🎨 ~700 líneas de CSS personalizado

    ├── about.html                  # Teoría y documentación│   ├── images/                 # 🖼️ (para futuras imágenes)

    ├── examples.html               # Ejemplos precargados│   └── js/

    ├── 404.html                    # Página de error│       └── app.js              # ⚡ JavaScript del cliente

    ││

    ├── results.html                # Método Gráfico - Resultados├── templates/

    ├── simplex.html                # Método Simplex - Formulario│   ├── base.html               # 📄 Layout base con navbar y footer

    ├── simplex_results.html        # Método Simplex - Resultados│   ├── index.html              # 🏠 Homepage

    ├── dual_simplex.html           # Dual Simplex - Formulario│   ├── about.html              # 📚 Acerca de

    ├── dual_simplex_results.html   # Dual Simplex - Resultados│   ├── examples.html           # 💡 Ejemplos de problemas

    ├── two_phase_simplex.html      # Dos Fases - Formulario│   ├── simplex.html            # 📝 Formulario Simplex

    └── two_phase_simplex_results.html  # Dos Fases - Resultados│   ├── simplex_results.html    # 📊 Visualización Simplex

```│   ├── dual_simplex.html       # 📝 Formulario Dual Simplex

│   ├── dual_simplex_results.html  # 📊 Visualización Dual Simplex

---│   └── 404.html                # ❌ Página de error

│

## 🚀 Instalación└── test_*.py                   # 🧪 Scripts de prueba

```

### Requisitos Previos

- Python 3.13+ instalado---

- pip (gestor de paquetes Python)

## 🚀 Instalación y Configuración

### Pasos de Instalación

### Prerrequisitos

1. **Clonar el repositorio**- Python 3.10 o superior

```bash- pip (gestor de paquetes de Python)

git clone https://github.com/Eljosek/Investigacion-de-operaciones.git- Git

cd Investigacion-de-operaciones

```### Paso 1: Clonar el repositorio



2. **Crear entorno virtual** (recomendado)```bash

```bashgit clone https://github.com/Eljosek/Investigacion-de-operaciones.git

python -m venv .venvcd Investigacion-de-operaciones

``````



3. **Activar entorno virtual**### Paso 2: Crear entorno virtual



Windows:**Windows:**

```bash```powershell

.venv\Scripts\activatepython -m venv .venv

```.venv\Scripts\Activate.ps1

```

macOS/Linux:

```bash**Linux/Mac:**

source .venv/bin/activate```bash

```python3 -m venv .venv

source .venv/bin/activate

4. **Instalar dependencias**```

```bash

pip install -r requirements.txt### Paso 3: Instalar dependencias

```

```bash

5. **Ejecutar la aplicación**pip install -r requirements.txt

```bash```

python app.py

```### Paso 4: Ejecutar la aplicación



6. **Abrir en navegador**```bash

```python app.py

http://localhost:5000```

```

La aplicación estará disponible en: **http://localhost:5000**

---

---

## 📖 Uso de la Aplicación

## 📚 Uso de la Aplicación

### 1️⃣ Método Gráfico (2 variables)

### Método Gráfico

**Cuándo usar:** Problemas con exactamente 2 variables de decisión.

**Ideal para:** Problemas con 2 variables

**Entrada:**

```**Ejemplo:**

Maximizar: z = 3x + 5y```

Función Objetivo: maximizar z = 3x + 5y

Restricciones:Restricciones:

x + 3y <= 26  x + y <= 4

4x + 3y <= 44  2x + y <= 6

2x + 3y <= 28  x >= 0

x >= 0  y >= 0

y >= 0```

```

### Método Simplex

**Salida:**

- Gráfico con región factible**Ideal para:** Problemas con múltiples variables y restricciones <=

- Coordenadas de vértices

- Valor óptimo en cada vértice**Ejemplo:**

- Solución óptima destacada```

Función Objetivo: maximizar z = 3x1 + 2x2 + x3

---Restricciones:

  x1 + x2 + x3 <= 10

### 2️⃣ Método Simplex (múltiples variables, restricciones ≤)  2x1 + x2 <= 8

  x1 + 2x3 <= 6

**Cuándo usar:** 3+ variables con restricciones de tipo "menor o igual".  x1 >= 0

  x2 >= 0

**Entrada:**  x3 >= 0

``````

Maximizar: z = 3x1 + 2x2 + x3

**Características:**

Restricciones:- Tableau inicial con variables de holgura

x1 + x2 + x3 <= 10- Iteraciones paso a paso mostradas

2x1 + x2 <= 8- Columna pivote (variable entrante) marcada en verde

x1 + 2x3 <= 6- Fila pivote (variable saliente) marcada en naranja

x1, x2, x3 >= 0- Ratios θ = b/a calculados

```- Solución óptima con variables básicas



**Salida:**### Método Dual-Simplex

- Tableau inicial con variables de holgura

- Iteraciones con pivotes resaltados**Ideal para:** Problemas de minimización con restricciones >=

- Variables básicas en cada paso

- Solución óptima final**Ejemplo:**

```

---Función Objetivo: minimizar z = 3x1 + 2x2

Restricciones:

### 3️⃣ Método Dual Simplex (restricciones ≥)  3x1 + x2 >= 3

  4x1 + 3x2 >= 6

**Cuándo usar:** Problemas de minimización con restricciones "mayor o igual".  x1 + x2 <= 3

  x1 >= 0

**Entrada:**  x2 >= 0

``````

Minimizar: z = 2x1 + 3x2

---

Restricciones:

x1 + 2x2 >= 6## 🎓 Algoritmos Implementados

2x1 + x2 >= 8

x1, x2 >= 0### 1. Método Gráfico

```1. Graficar todas las restricciones

2. Identificar la región factible

**Salida:**3. Encontrar vértices (puntos de intersección)

- Tableau dual con variables de exceso4. Evaluar función objetivo en cada vértice

- Ratios duales calculados5. Seleccionar el vértice con mejor valor

- Iteraciones hasta optimalidad

- Valor mínimo alcanzado### 2. Método Simplex

1. **Construcción del tableau inicial** con variables de holgura

---2. **Criterio de optimalidad**: zⱼ - cⱼ ≤ 0 para maximización

3. **Selección de variable entrante**: zⱼ - cⱼ más positivo

### 4️⃣ Método Simplex Dos Fases (restricciones ≥, =, mixtas)4. **Selección de variable saliente**: mínimo ratio θ = bᵢ/aᵢⱼ

5. **Operaciones de pivote** (Gauss-Jordan)

**Cuándo usar:** Problemas con restricciones de igualdad o mayor-igual.6. **Iteración** hasta optimalidad o unboundedness



**Entrada:**### 3. Método Dual Simplex

```1. **Verificación de factibilidad dual**: zⱼ - cⱼ ≤ 0

Maximizar: z = 3x1 + 5x22. **Selección de fila pivote**: RHS más negativo

3. **Selección de columna pivote**: mínimo ratio zⱼ/aᵢⱼ (negativo)

Restricciones:4. **Operaciones de pivote** para restaurar factibilidad primal

4x1 + x2 >= 45. **Iteración** hasta factibilidad y optimalidad

-x1 + 2x2 >= 2

x2 <= 3---

x1, x2 >= 0

```## 💡 Ejemplos de Problemas



**Salución:**### Ejemplo 1: Maximización Simple (Gráfico)

- **Fase I:** Minimización de W (suma de artificiales)```

- **Fase II:** Optimización de Z (función original)Maximizar Z = 40x₁ + 30x₂

- Tableaux completos de ambas fasesRestricciones:

  2x₁ + 1x₂ ≤ 8   (Recurso A)

---  1x₁ + 2x₂ ≤ 10  (Recurso B)

  x₁, x₂ ≥ 0

## 🎓 Conceptos Clave```

**Solución:** x₁=2, x₂=4, Z=200

### Variables Agregadas

### Ejemplo 2: Problema Multivariable (Simplex)

| Tipo | Símbolo | Cuándo se usa | Restricción original |```

|------|---------|---------------|---------------------|Maximizar Z = 5x₁ + 4x₂ + 3x₃

| **Holgura** | s | ≤ | ax + by ≤ c → ax + by + s = c |Restricciones:

| **Exceso** | e | ≥ | ax + by ≥ c → ax + by - e = c |  2x₁ + 3x₂ + 1x₃ ≤ 5

| **Artificial** | A | ≥, = | ax + by ≥ c → ax + by - e + A = c |  4x₁ + 1x₂ + 2x₃ ≤ 11

  3x₁ + 4x₂ + 2x₃ ≤ 8

### Detección de Casos Especiales  x₁, x₂, x₃ ≥ 0

```

| Situación | Indicador | Método |**Solución:** x₁=2, x₂=0, x₃=1, Z=13

|-----------|-----------|--------|

| **Infactible** | W > 0 al final de Fase I | Dos Fases |### Ejemplo 3: Minimización con ≥ (Dual Simplex)

| **No acotado** | Todos ratios ≤ 0 | Simplex/Dual |```

| **Degenerado** | Variable básica = 0 | Todos |Minimizar Z = 8x₁ + 12x₂

| **Múltiples soluciones** | Coef. 0 en variable no básica | Todos |Restricciones:

  1x₁ + 2x₂ ≥ 10  (Demanda mínima)

---  2x₁ + 1x₂ ≥ 12  (Producción mínima)

  x₁, x₂ ≥ 0

## 🎨 Personalización de Colores```

**Solución:** x₁=4.67, x₂=2.67, Z=69.33

Cada método tiene su propio esquema de colores definido en `styles.css`:

---

```css

/* Método Gráfico - Verde */## 🧪 Testing

--color-grafico: #10b981;

### Ejecutar Tests

/* Método Simplex - Amarillo/Naranja */

--color-simplex: #f59e0b;```bash

# Test Ejemplo 1 (Dual-Simplex)

/* Método Dual Simplex - Azul/Púrpura */python test_ejemplo1.py

--color-dual: #8b5cf6;

# Test Ejemplo 2 (Simplex)

/* Método Dos Fases - Naranja Coral */python test_ejemplo2.py

--color-two-phase: #f97316;

```# Test Ejemplo 3 (Restricciones mixtas)

python test_ejemplo3.py

---

# Test de Petición Web

## 🧪 Ejemplos Precargadospython test_web_request.py

```

La aplicación incluye **10 ejemplos** distribuidos así:

### Resultados Esperados

- **Método Gráfico:** 2 ejemplos

- **Método Simplex:** 2 ejemplosTodos los tests deben pasar mostrando:

- **Método Dual Simplex:** 2 ejemplos- ✅ Valor óptimo correcto

- **Método Dos Fases:** 2 ejemplos- ✅ Variables con valores correctos

- ✅ Número correcto de iteraciones

Accede a ellos desde la página **"Ejemplos"** en el menú de navegación.- ✅ Sin errores de arrays NumPy

- ✅ Sin notación científica (e-16)

---

---

## 🐛 Solución de Problemas

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'flask'"

```bash### El servidor no inicia

pip install -r requirements.txt

``````bash

# Verificar puerto ocupado

### El servidor no inicianetstat -ano | findstr :5000

Verifica que el puerto 5000 esté libre:

```bash# Matar proceso si es necesario (Windows)

# Windowstaskkill /F /PID <número_de_pid>

netstat -ano | findstr :5000

# O cambiar puerto en app.py

# Linux/Macapp.run(debug=True, port=5001)

lsof -i :5000```

```

### Error de importación de módulos

### Los números no se formatean correctamente

El filtro `smart_number` convierte automáticamente:```bash

- `-6.0` → `-6`# Reinstalar dependencias

- `8.666666` → `8.67`pip install -r requirements.txt --force-reinstall

```

Si persiste el problema, limpia la caché del navegador.

### Errores con NumPy

---

```bash

## 🤝 Contribuciones# Actualizar NumPy

pip install --upgrade numpy

Este es un proyecto educativo de la Universidad Tecnológica de Pereira. Si deseas contribuir:```



1. Fork el repositorio### Gráfica no se muestra (Método Gráfico)

2. Crea una rama (`git checkout -b feature/mejora`)

3. Commit tus cambios (`git commit -m 'Agregar mejora'`)**Causa:** Problema con matplotlib backend  

4. Push a la rama (`git push origin feature/mejora`)**Solución:** Asegúrate de tener matplotlib instalado correctamente

5. Abre un Pull Request

### Servidor no arranca en puerto 5000

---

**Solución:** Cambia el puerto en `app.py`:

## 📝 Licencia```python

app.run(debug=True, host='0.0.0.0', port=8080)

Este proyecto es de uso educativo para la Universidad Tecnológica de Pereira (UTP).```



**Autor:** José Miguel Herrera Gutiérrez  ---

**Materia:** Investigación de Operaciones  

**Profesora:** Bibiana Patricia Arias Villada  ## 🔧 Mejoras Técnicas Implementadas

**Año:** 2025

### Corrección de Valores Numéricos

---

**Problema:** Aparecían valores como `4.441e-16` (notación científica para números muy pequeños)

## 🙏 Agradecimientos

**Causa:** Errores de precisión en operaciones de punto flotante

- **Universidad Tecnológica de Pereira** por la formación académica

- **Profesora Bibiana Patricia Arias Villada** por la guía en Investigación de Operaciones**Solución implementada:**

- **Bootstrap Team** por el framework CSS```python

- **Flask Community** por el excelente framework webdef _clean_small_values(self, value: float, tolerance: float = 1e-10) -> float:

- **NumPy Developers** por las herramientas matemáticas    """Redondea valores muy pequeños a 0"""

    if abs(value) < tolerance:

---        return 0.0

    return value

## 📧 Contacto```



Para preguntas o sugerencias sobre el proyecto:Todos los valores menores a `1e-10` (0.0000000001) se redondean a 0, eliminando la notación científica innecesaria.



- **Estudiante:** José Miguel Herrera Gutiérrez### Manejo de Tipos de Datos

- **Universidad:** Universidad Tecnológica de Pereira (UTP)

- **Repositorio:** [github.com/Eljosek/Investigacion-de-operaciones](https://github.com/Eljosek/Investigacion-de-operaciones)- Uso correcto de `float()` para elementos individuales de arrays NumPy

- Uso de `np.all()` y `np.any()` para comparaciones de arrays completos

---- Evita el error: "The truth value of an array with more than one element is ambiguous"



<div align="center">### Variables de Template



**Hecho con ❤️ para Investigación de Operaciones - UTP 2025**- Backend envía `solution` (no `variables`)

- Backend envía `objective_value` (no `z_value`)

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub- Campo `opt_type` agregado para distinguir MAX/MIN

- Estructura consistente entre todos los métodos

</div>

---

## 🎓 Contexto Académico

Este proyecto fue desarrollado para el curso de **Investigación de Operaciones** en la Universidad Tecnológica de Pereira (UTP), específicamente para el **Segundo Parcial** de la materia.

### Objetivos del Proyecto

1. ✅ Implementar algoritmos de PL **sin librerías externas de optimización**
2. ✅ Visualizar **paso a paso** el funcionamiento de cada método
3. ✅ Crear interfaz **educativa y moderna** para estudiantes
4. ✅ Comparar **tres enfoques diferentes** de resolución
5. ✅ Documentar **exhaustivamente** el desarrollo

### Profesora

**Bibiana Patricia Arias Villada**  
Facultad de Ingeniería Industrial  
Universidad Tecnológica de Pereira

### Estudiante

**José Miguel Herrera Gutiérrez**  
Ingeniería de Sistemas y Computación  
Fecha de Entrega: Octubre 2025

---

## 📝 Formato de Entrada Detallado

### Coeficientes de Función Objetivo
- Separados por espacios: `3 5 2`
- Negativos permitidos: `-2 4 -1`

### Restricciones (Método Gráfico)
```
coef1 coef2 operador valor
```
Ejemplo:
```
2 3 <= 10
1 4 >= 5
3 2 = 8
```

### Restricciones (Simplex/Dual Simplex)
```
coef1 coef2 ... coefN operador valor
```
Ejemplo (3 variables):
```
2 1 3 <= 15
1 2 1 >= 8
```

### Operadores Soportados
- `<=` o `≤` : Menor o igual
- `>=` o `≥` : Mayor o igual
- `=` : Igualdad (aún en desarrollo)

---

## 🚀 Despliegue (Producción)

### Usando Gunicorn (Linux/Mac)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Usando Waitress (Windows)
```bash
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

### Variables de Entorno
```bash
# .env file
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
PORT=5000
```

---

## 🤝 Contribución

Este es un proyecto académico, pero si deseas contribuir:

1. Fork el repositorio
2. Crea una branch (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -m 'Agregar mejora'`)
4. Push a la branch (`git push origin feature/mejora`)
5. Abre un Pull Request

### Áreas de Mejora

- [ ] Método de Big M para variables artificiales
- [ ] Análisis de sensibilidad
- [ ] Exportación de resultados a PDF/Excel
- [ ] Modo offline (sin CDNs)
- [ ] Tests automatizados (pytest)
- [ ] Soporte para más de 5 variables (Simplex Revisado)

---

## 📄 Licencia

Este proyecto fue desarrollado con fines **educativos** para la Universidad Tecnológica de Pereira. El código es de libre uso para estudiantes y académicos.

## 📧 Contacto

**José Miguel Herrera Gutiérrez**  
Universidad Tecnológica de Pereira  
Ingeniería de Sistemas y Computación

---

**⭐ Si este proyecto te fue útil, dale una estrella en GitHub!**

---

## 📚 Referencias

- Winston, W. L. (2004). *Operations Research: Applications and Algorithms*. Thomson Brooks/Cole.
- Hillier, F. S., & Lieberman, G. J. (2015). *Introduction to Operations Research*. McGraw-Hill Education.
- Taha, H. A. (2017). *Operations Research: An Introduction*. Pearson Education.
- Documentación de NumPy: https://numpy.org/doc/
- Documentación de Flask: https://flask.palletsprojects.com/

---

## 🔄 Historial de Versiones

### Versión 3.0 (Octubre 2025) - ACTUAL
- ✅ Corrección de notación científica (e-16 → 0)
- ✅ Limpieza de documentación (Markdown unificado)
- ✅ README completo y profesional
- ✅ Estructura de proyecto limpia
- ✅ URL de localhost siempre visible

### Versión 2.0 (Octubre 2025)
- ✅ Dual-Simplex optimizado para MAX/MIN
- ✅ Corrección de errores de arrays NumPy
- ✅ Templates Jinja2 corregidos

### Versión 1.0 (Octubre 2025)
- ✅ Implementación inicial de tres métodos
- ✅ Interfaz web con Flask
- ✅ Visualización básica de resultados

---

**¡Listo para usar!** 🚀

Para iniciar: `python app.py` y navega a `http://localhost:5000`
