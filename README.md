# 📊 Solucionador de Programación Lineal# 📊 Solucionador de Programación Lineal - Aplicación Web Educativa



**Aplicación Web Educativa - Investigación de Operaciones****Investigación de Operaciones - Segundo Parcial**  

**Universidad Tecnológica de Pereira (UTP)**  

---**Desarrollado por:** José Miguel Herrera Gutiérrez  

**Profesora:** Bibiana Patricia Arias Villada

## 👨‍💻 Información del Proyecto

**Última actualización:** 18 de Octubre de 2025  

- **Universidad:** Universidad Tecnológica de Pereira (UTP)**Versión:** 2.0 - Con Método de Dos Fases Completo

- **Materia:** Investigación de Operaciones - Segundo Parcial

- **Estudiante:** José Miguel Herrera Gutiérrez---

- **Profesora:** Bibiana Patricia Arias Villada

- **Fecha:** Octubre 2025Una aplicación web completa para resolver problemas de programación lineal con **tres métodos diferentes**: Gráfico, Simplex (con Dos Fases) y Dual Simplex. Diseñada con enfoque educativo para visualizar **paso a paso** cada iteración del algoritmo.

- **Versión:** 3.0

## ✨ Características Principales

---

### 🎨 Interfaz Moderna

## 📋 Descripción- **Diseño responsivo** con Bootstrap 5

- **Modo oscuro** con variables CSS personalizadas

Aplicación web completa para resolver problemas de **Programación Lineal** con tres métodos diferentes:- **Colores distintivos** por método (Azul/Verde/Púrpura)

- **Iconos Font Awesome** para mejor UX

1. **Método Gráfico** - Para problemas con 2 variables- **Tooltips interactivos** en formularios

2. **Método Simplex** - Con algoritmo de Dos Fases para múltiples variables- **Navegación fluida** con smooth scroll

3. **Método Dual-Simplex** - Optimizado para problemas con restricciones >=

### 🔢 Tres Métodos de Solución

La aplicación está diseñada con **enfoque educativo**, mostrando paso a paso cada iteración del algoritmo con tablas (tableau) completas, variables básicas, operaciones de pivoteo y valores objetivo.

| Método | Ideal Para | Restricciones | Algoritmo |

---|--------|------------|---------------|-----------|

| **Gráfico** | 2 variables | <= | Intersecciones y vértices |

## ✨ Características Principales| **Simplex** | 2-5+ variables | **<=, >=, =** | Simplex con Método de Dos Fases |

| **Dual Simplex** | MAX/MIN con >= | >= | Dual Simplex para MAX y MIN |

### 🎯 Funcionalidades

### 🆕 Novedades Versión 2.0

- ✅ **Tres métodos de solución** con algoritmos optimizados

- ✅ **Visualización paso a paso** de iteraciones#### ✅ Método de Dos Fases Completo

- ✅ **Tablas (tableau) interactivas** con resaltado de pivotes- **Fase I:** Eliminación de variables artificiales

- ✅ **Soporte para restricciones** `<=`, `>=`, `=`- **Fase II:** Optimización de función objetivo original

- ✅ **Detección automática** de infactibilidad y no acotamiento- **Soporte para restricciones >=, =**

- ✅ **Exportación a PDF** de resultados (función de impresión)- **Detección de infactibilidad** en Fase I

- ✅ **Ejemplos precargados** para cada método- **Transición automática** entre fases

- ✅ **Interfaz responsiva** con Bootstrap 5

#### ✅ Dual-Simplex Mejorado

### 🎨 Diseño- **Soporte para MAX y MIN**

- **Selección correcta de pivotes** según tipo de optimización

- **Tema moderno** con colores distintivos por método:- **Factibilidad dual verificada**

  - 🔵 Azul para Método Gráfico- **Cálculo correcto de valor objetivo** para ambos tipos

  - 🟢 Verde para Método Simplex

  - 🟣 Púrpura para Dual-Simplex#### ✅ Validaciones Robustas

- **Iconos Font Awesome** para mejor experiencia visual- **Detección de problemas no acotados**

- **Tooltips informativos** en formularios- **Detección de infactibilidad**

- **Acordeones interactivos** para navegación de iteraciones- **Mensajes de error claros y educativos**

- **Responsive design** para móviles y tablets- **Bland's Rule** para evitar cycling



---### 📚 Enfoque Educativo

- **Visualización paso a paso** de cada iteración

## 🛠️ Tecnologías Utilizadas- **Tableau completo** con variables de holgura/exceso/artificiales

- **Pivotes identificados** con colores

### Backend- **Ratios calculados** (θ para Simplex, zⱼ/aᵢⱼ para Dual)

- **Python 3.13.7**- **Explicaciones claras** de cada paso

- **Flask 3.1.2** - Framework web- **Variables básicas/no básicas** marcadas

- **NumPy 2.3.3** - Operaciones matriciales- **Indicadores de fase** (Fase I/II en Dos Fases)

- **Matplotlib 3.9.4** - Gráficos del método gráfico

### 🛠️ Implementación Manual

### Frontend- **Sin librerías externas** de optimización (no PuLP, no SciPy)

- **HTML5** con plantillas Jinja2- **NumPy puro** para operaciones matriciales

- **CSS3** con variables personalizadas- **Algoritmos escritos desde cero** para fines educativos

- **JavaScript ES6+**- **Código bien documentado** y legible

- **Bootstrap 5.3** - Framework CSS- **Tolerancia numérica** (EPS = 1e-9)

- **Font Awesome 6.0** - Iconos

## 🚀 Inicio Rápido

### Herramientas

- **Git** para control de versiones### Requisitos Previos

- **Virtual Environment** para aislamiento de dependencias- Python 3.8 o superior

- pip (gestor de paquetes de Python)

---- Navegador web moderno (Chrome, Firefox, Edge)



## 📁 Estructura del Proyecto### Instalación



```1. **Clonar el repositorio**:

Investigacion-de-operaciones/   ```bash

│   git clone https://github.com/Eljosek/Investigacion-de-operaciones.git

├── app.py                      # Aplicación Flask principal   cd "Investigacion de operaciones"

├── requirements.txt            # Dependencias Python   ```

├── README.md                   # Este archivo

│2. **Crear entorno virtual** (recomendado):

├── lp_solver.py               # Método Gráfico   ```bash

├── simplex_tableau.py         # Método Simplex con Dos Fases   python -m venv .venv

├── dual_simplex_tableau.py    # Método Dual-Simplex   

│   # Windows

├── templates/                 # Plantillas HTML Jinja2   .venv\Scripts\activate

│   ├── base.html             # Plantilla base con navegación   

│   ├── index.html            # Página de inicio   # Linux/Mac

│   ├── about.html            # Información del proyecto   source .venv/bin/activate

│   ├── examples.html         # Galería de ejemplos   ```

│   │

│   ├── grafico.html          # Formulario Método Gráfico3. **Instalar dependencias**:

│   ├── grafico_results.html  # Resultados Método Gráfico   ```bash

│   │   pip install -r requirements.txt

│   ├── simplex.html          # Formulario Método Simplex   ```

│   ├── simplex_results.html  # Resultados Método Simplex

│   │4. **Ejecutar la aplicación**:

│   ├── dual_simplex.html     # Formulario Dual-Simplex   ```bash

│   └── dual_simplex_results.html  # Resultados Dual-Simplex   python app.py

│   ```

├── static/                    # Archivos estáticos

│   ├── css/5. **Abrir en el navegador**: `http://localhost:5000`

│   │   └── styles.css        # Estilos personalizados

│   ├── js/## 📖 Guía de Uso

│   │   └── app.js            # JavaScript de la aplicación

│   └── images/               # Imágenes (si las hay)### Método Gráfico (2 Variables)

│

└── test_*.py                  # Scripts de prueba**Problema de Ejemplo:**

``````

Maximizar: Z = 3x₁ + 5x₂

---Sujeto a:

  2x₁ + 3x₂ ≤ 10

## 🚀 Instalación y Configuración  1x₁ + 4x₂ ≤ 8

  3x₁ + 2x₂ ≤ 12

### Prerrequisitos  x₁, x₂ ≥ 0

```

- Python 3.10 o superior

- pip (gestor de paquetes de Python)**Formato de Entrada:**

- Git- Función objetivo: `3x1 + 5x2`

- Restricciones (una por línea):

### Paso 1: Clonar el repositorio  ```

  2 3 <= 10

```bash  1 4 <= 8

git clone https://github.com/Eljosek/Investigacion-de-operaciones.git  3 2 <= 12

cd Investigacion-de-operaciones  ```

```

**Resultado:**

### Paso 2: Crear entorno virtual- Gráfica con región factible sombreada

- Vértices del poliedro marcados

**Windows:**- Punto óptimo destacado

```powershell- Valor óptimo de Z

python -m venv .venv- Análisis de restricciones activas/inactivas

.venv\Scripts\Activate.ps1

```### Método Simplex (2-5+ Variables)



**Linux/Mac:****Problema de Ejemplo:**

```bash```

python3 -m venv .venvMaximizar: Z = 4x₁ + 3x₂ + 2x₃

source .venv/bin/activateSujeto a:

```  2x₁ + 1x₂ + 1x₃ ≤ 6

  1x₁ + 2x₂ + 3x₃ ≤ 9

### Paso 3: Instalar dependencias  x₁, x₂, x₃ ≥ 0

```

```bash

pip install -r requirements.txt**Formato de Entrada:**

```- Tipo: Maximizar

- Variables: 3

### Paso 4: Ejecutar la aplicación- Restricciones: 2

- Coeficientes objetivo: `4 3 2`

```bash- Restricciones:

python app.py  ```

```  2 1 1 <= 6

  1 2 3 <= 9

La aplicación estará disponible en: **http://localhost:5000**  ```



---**Resultado:**

- Tableau inicial con variables de holgura

## 📚 Uso de la Aplicación- Iteraciones paso a paso

- Columna pivote (variable entrante) marcada en verde

### Método Gráfico- Fila pivote (variable saliente) marcada en naranja

- Ratios θ = b/a (mínimo ratio positivo)

**Ideal para:** Problemas con 2 variables- Tableau final con solución óptima

- Variables básicas y sus valores

**Ejemplo:**

```### Método Dual Simplex (Problemas Duales)

Función Objetivo: maximizar z = 3x + 5y

Restricciones:**Problema de Ejemplo:**

  x + y <= 4```

  2x + y <= 6Minimizar: Z = 2x₁ + 3x₂

  x >= 0Sujeto a:

  y >= 0  1x₁ + 2x₂ ≥ 4

```  3x₁ + 1x₂ ≥ 6

  x₁, x₂ ≥ 0

### Método Simplex (con Dos Fases)```



**Ideal para:** Problemas con múltiples variables y restricciones mixtas**Formato de Entrada:**

- Tipo: Minimizar

**Ejemplo:**- Variables: 2

```- Restricciones: 2

Función Objetivo: maximizar z = 3x1 + 2x2 + x3- Coeficientes objetivo: `2 3`

Restricciones:- Restricciones:

  x1 + x2 + x3 <= 10  ```

  2x1 + x2 >= 8  1 2 >= 4

  x1 + 2x3 = 6  3 1 >= 6

  x1 >= 0  ```

  x2 >= 0

  x3 >= 0**Resultado:**

```- Tableau con restricciones ≥ (variables de exceso)

- Iteraciones del algoritmo dual

**Características:**- Fila pivote (RHS negativo más negativo)

- **Fase I:** Elimina variables artificiales- Columna pivote (ratios zⱼ/aᵢⱼ)

- **Fase II:** Optimiza la función objetivo original- Ratios duales calculados y mostrados

- Detecta infactibilidad automáticamente- Solución óptima del problema dual



### Método Dual-Simplex## 🔧 Stack Tecnológico



**Ideal para:** Problemas de minimización con restricciones >=### Backend

- **Flask 3.1.2** - Framework web minimalista

**Ejemplo:**- **Python 3.13.7** - Lenguaje de programación

```- **NumPy 2.3.3** - Operaciones matriciales

Función Objetivo: minimizar z = 3x1 + 2x2- **Matplotlib 3.10.1** - Generación de gráficas (método gráfico)

Restricciones:

  3x1 + x2 >= 3### Frontend

  4x1 + 3x2 >= 6- **Bootstrap 5.3** - Framework CSS responsivo

  x1 + x2 <= 3- **Font Awesome 6.6** - Iconos vectoriales

  x1 >= 0- **Google Fonts** - Poppins (títulos) e Inter (texto)

  x2 >= 0- **JavaScript ES6** - Interacciones del cliente

```- **CSS Variables** - Sistema de tematización



---### Características CSS

- **25+ variables CSS** para colores y tipografía

## 🎓 Algoritmos Implementados- **4 animaciones** (fade-in, slide-up, pulse, gradient-shift)

- **Clases por método** (.method-grafico, .method-simplex, .method-dual)

### 1. Método Gráfico- **Modo oscuro** con prefers-color-scheme

- **Gradientes** para CTAs y hero section

1. Graficar todas las restricciones

2. Identificar la región factible## 📁 Estructura del Proyecto

3. Encontrar vértices (puntos de intersección)

4. Evaluar función objetivo en cada vértice```

5. Seleccionar el vértice con mejor valorInvestigacion-de-operaciones/

├── app.py                      # 🌐 Aplicación Flask con routes

### 2. Método Simplex con Dos Fases├── lp_solver.py                # 📈 Método Gráfico (2 variables)

├── simplex_tableau.py          # 🔢 Método Simplex (NumPy)

**Fase I:**├── dual_simplex_tableau.py     # 🔄 Método Dual Simplex (NumPy)

1. Agregar variables artificiales para restricciones >= y =├── requirements.txt            # 📦 Dependencias (Flask, NumPy, Matplotlib)

2. Minimizar suma de variables artificiales├── CHANGELOG.md                # 📝 Historial de cambios (8 fases)

3. Si suma > 0 al final: problema infactible├── README.md                   # 📖 Este archivo

4. Si suma = 0: continuar a Fase II├── .gitignore                  # 🚫 Archivos ignorados (venv, __pycache__)

│

**Fase II:**├── static/

1. Eliminar variables artificiales│   ├── css/

2. Restaurar función objetivo original│   │   └── styles.css          # 🎨 ~700 líneas de CSS personalizado

3. Aplicar algoritmo Simplex estándar:│   ├── images/                 # 🖼️ (vacío, para futuras imágenes)

   - Seleccionar columna pivote (coeficiente más negativo en fila Z)│   └── js/

   - Seleccionar fila pivote (prueba del cociente mínimo)│       └── app.js              # ⚡ JavaScript del cliente

   - Realizar operaciones de fila (pivoteo)│

   - Repetir hasta que todos los coeficientes en fila Z sean no-negativos└── templates/

    ├── base.html               # 📄 Layout base con navbar y footer

### 3. Método Dual-Simplex    ├── index.html              # 🏠 Homepage (~360 líneas)

    ├── simplex.html            # 📝 Formulario Simplex con tooltips

1. Convertir restricciones >= multiplicando por -1    ├── simplex_results.html    # 📊 Visualización Simplex (401 líneas)

2. Buscar fila con RHS más negativo (variable saliente)    ├── dual_simplex.html       # 📝 Formulario Dual con tooltips

3. Calcular ratios duales: z_j / a_ij para a_ij < 0    ├── dual_simplex_results.html  # 📊 Visualización Dual (424 líneas)

4. Seleccionar columna con ratio mínimo (variable entrante)    ├── about.html              # 📚 Acerca de (~450 líneas)

5. Realizar pivoteo    ├── examples.html           # 💡 Ejemplos de problemas

6. Repetir hasta que todos RHS >= 0    └── 404.html                # ❌ Página de error

```

---

## 💡 Ejemplos de Problemas

## 🔧 Mejoras Técnicas Implementadas

### Ejemplo 1: Maximización Simple (Gráfico)

### Corrección de Valores Numéricos```

Maximizar Z = 40x₁ + 30x₂

**Problema:** Aparecían valores como `4.441e-16` (notación científica para números muy pequeños)Restricciones:

  2x₁ + 1x₂ ≤ 8   (Recurso A)

**Causa:** Errores de precisión en operaciones de punto flotante  1x₁ + 2x₂ ≤ 10  (Recurso B)

  x₁, x₂ ≥ 0

**Solución implementada:**```

```python**Solución:** x₁=2, x₂=4, Z=200

def _clean_small_values(self, value: float, tolerance: float = 1e-10) -> float:

    """Redondea valores muy pequeños a 0"""### Ejemplo 2: Problema Multivariable (Simplex)

    if abs(value) < tolerance:```

        return 0.0Maximizar Z = 5x₁ + 4x₂ + 3x₃

    return valueRestricciones:

```  2x₁ + 3x₂ + 1x₃ ≤ 5

  4x₁ + 1x₂ + 2x₃ ≤ 11

Todos los valores menores a `1e-10` (0.0000000001) se redondean a 0, eliminando la notación científica innecesaria.  3x₁ + 4x₂ + 2x₃ ≤ 8

  x₁, x₂, x₃ ≥ 0

### Manejo de Tipos de Datos```

**Solución:** x₁=2, x₂=0, x₃=1, Z=13

- Uso correcto de `float()` para elementos individuales de arrays NumPy

- Uso de `np.all()` y `np.any()` para comparaciones de arrays completos### Ejemplo 3: Minimización con ≥ (Dual Simplex)

- Evita el error: "The truth value of an array with more than one element is ambiguous"```

Minimizar Z = 8x₁ + 12x₂

### Variables de TemplateRestricciones:

  1x₁ + 2x₂ ≥ 10  (Demanda mínima)

- Backend envía `solution` (no `variables`)  2x₁ + 1x₂ ≥ 12  (Producción mínima)

- Backend envía `objective_value` (no `z_value`)  x₁, x₂ ≥ 0

- Campo `opt_type` agregado para distinguir MAX/MIN```

- Estructura consistente entre todos los métodos**Solución:** x₁=4.67, x₂=2.67, Z=69.33



---## 🎓 Contexto Académico



## 📊 Ejemplos de UsoEste proyecto fue desarrollado para el curso de **Investigación de Operaciones** en la Universidad Tecnológica de Pereira (UTP), específicamente para el **Segundo Parcial** de la materia.



### Ejemplo 1: Maximización Simple### Objetivos del Proyecto

1. ✅ Implementar algoritmos de PL **sin librerías externas de optimización**

**Entrada:**2. ✅ Visualizar **paso a paso** el funcionamiento de cada método

```3. ✅ Crear interfaz **educativa y moderna** para estudiantes

max z = 3x1 + 2x24. ✅ Comparar **tres enfoques diferentes** de resolución

x1 + x2 <= 45. ✅ Documentar **exhaustivamente** el desarrollo

2x1 + x2 <= 6

x1, x2 >= 0### Profesora

```**Bibiana Patricia Arias Villada**  

Facultad de Ingeniería Industrial  

**Resultado esperado:**Universidad Tecnológica de Pereira

- Z óptimo = 12

- x1 = 2, x2 = 2### Estudiante

**José Miguel Herrera Gutiérrez**  

### Ejemplo 2: Minimización con >=Ingeniería de Sistemas y Computación  

Fecha de Entrega: Octubre 2025

**Entrada:**

```## 📝 Formato de Entrada Detallado

min z = 3x1 + 2x2

3x1 + x2 >= 3### Coeficientes de Función Objetivo

4x1 + 3x2 >= 6- Separados por espacios: `3 5 2`

x1 + x2 <= 3- Negativos permitidos: `-2 4 -1`

x1, x2 >= 0

```### Restricciones (Método Gráfico)

```

**Resultado esperado:**coef1 coef2 operador valor

- Z óptimo = 4.2```

- x1 = 0.6, x2 = 1.2Ejemplo:

```

### Ejemplo 3: Problema con Restricciones =2 3 <= 10

1 4 >= 5

**Entrada:**3 2 = 8

``````

max z = 3x1 + 2x2 + x3

x1 + x2 + x3 <= 10### Restricciones (Simplex/Dual Simplex)

2x1 + x2 = 8```

x1 + 2x3 <= 6coef1 coef2 ... coefN operador valor

x1, x2, x3 >= 0```

```Ejemplo (3 variables):

```

**Resultado:** Método Simplex con Dos Fases encuentra solución óptima2 1 3 <= 15

1 2 1 >= 8

---```



## 🧪 Testing### Operadores Soportados

- `<=` o `≤` : Menor o igual

### Ejecutar Tests- `>=` o `≥` : Mayor o igual

- `=` : Igualdad

```bash

# Test Ejemplo 1 (Dual-Simplex)## 🐛 Solución de Problemas

python test_ejemplo1.py

### Error: "Import flask could not be resolved"

# Test Ejemplo 2 (Simplex)**Solución:** Activa el entorno virtual antes de ejecutar:

python test_ejemplo2.py```bash

.venv\Scripts\activate  # Windows

# Test Ejemplo 3 (Restricciones mixtas)python app.py

python test_ejemplo3.py```



# Test de Petición Web### Error: "No module named numpy"

python test_web_request.py**Solución:** Instala las dependencias:

``````bash

pip install -r requirements.txt

### Resultados Esperados```



Todos los tests deben pasar mostrando:### Gráfica no se muestra (Método Gráfico)

- ✅ Valor óptimo correcto**Causa:** Problema con matplotlib backend  

- ✅ Variables con valores correctos**Solución:** Asegúrate de tener matplotlib instalado correctamente

- ✅ Número correcto de iteraciones

- ✅ Sin errores de arrays NumPy### Servidor no arranca en puerto 5000

- ✅ Sin notación científica (e-16)**Solución:** Cambia el puerto en `app.py`:

```python

---app.run(debug=True, host='0.0.0.0', port=8080)

```

## 🐛 Solución de Problemas

### Tooltips no funcionan

### El servidor no inicia**Solución:** Verifica que Bootstrap JS esté cargado correctamente (requiere internet para CDN)



```bash## 📊 Algoritmos Implementados

# Verificar puerto ocupado

netstat -ano | findstr :5000### Método Gráfico

1. **Parsing de restricciones** con regex

# Matar proceso si es necesario (Windows)2. **Cálculo de intersecciones** entre rectas

taskkill /F /PID <número_de_pid>3. **Determinación de región factible** con desigualdades

4. **Evaluación en vértices** de la función objetivo

# O cambiar puerto en app.py5. **Generación de gráfica** con matplotlib

app.run(debug=True, port=5001)

```### Método Simplex

1. **Construcción del tableau inicial** con variables de holgura

### Error de importación de módulos2. **Criterio de optimalidad**: zⱼ - cⱼ ≤ 0 para maximización

3. **Selección de variable entrante**: zⱼ - cⱼ más positivo

```bash4. **Selección de variable saliente**: mínimo ratio θ = bᵢ/aᵢⱼ

# Reinstalar dependencias5. **Operaciones de pivote** (Gauss-Jordan)

pip install -r requirements.txt --force-reinstall6. **Iteración** hasta optimalidad o unboundedness

```

### Método Dual Simplex

### Errores con NumPy1. **Verificación de factibilidad dual**: zⱼ - cⱼ ≤ 0

2. **Selección de fila pivote**: RHS más negativo

```bash3. **Selección de columna pivote**: mínimo ratio zⱼ/aᵢⱼ (negativo)

# Actualizar NumPy4. **Operaciones de pivote** para restaurar factibilidad primal

pip install --upgrade numpy5. **Iteración** hasta factibilidad y optimalidad

```

## 🚀 Despliegue (Producción)

---

### Usando Gunicorn (Linux/Mac)

## 📝 Notas de Desarrollo```bash

pip install gunicorn

### Commitsgunicorn -w 4 -b 0.0.0.0:5000 app:app

```

El proyecto usa Git para control de versiones. Commits principales:

### Usando Waitress (Windows)

1. **Implementación inicial** de métodos básicos```bash

2. **Corrección de Simplex** con Dos Fasespip install waitress

3. **Corrección de Dual-Simplex** para MAX y MINwaitress-serve --host=0.0.0.0 --port=5000 app:app

4. **Limpieza de valores numéricos** (eliminación de e-16)```

5. **Documentación completa** y estructura final

### Variables de Entorno

### Buenas Prácticas Aplicadas```bash

# .env file

- ✅ Código modularizado en archivos separados por métodoSECRET_KEY=tu-clave-secreta-aqui

- ✅ Funciones con docstrings explicativosDEBUG=False

- ✅ Manejo robusto de errores con try/exceptPORT=5000

- ✅ Validación de entradas del usuario```

- ✅ Mensajes informativos con `flash()` de Flask

- ✅ Separación de lógica (backend) y presentación (frontend)## 🤝 Contribución



---Este es un proyecto académico, pero si deseas contribuir:



## 📄 Licencia1. Fork el repositorio

2. Crea una branch (`git checkout -b feature/mejora`)

Este proyecto fue desarrollado con fines educativos para la materia de Investigación de Operaciones en la Universidad Tecnológica de Pereira.3. Commit tus cambios (`git commit -m 'Agregar mejora'`)

4. Push a la branch (`git push origin feature/mejora`)

---5. Abre un Pull Request



## 🙏 Agradecimientos### Áreas de Mejora

- [ ] Método de Big M para variables artificiales

- **Profesora Bibiana Patricia Arias Villada** por la guía en la materia- [ ] Análisis de sensibilidad

- **Universidad Tecnológica de Pereira** por la formación académica- [ ] Exportación de resultados a PDF/Excel

- Comunidad de Stack Overflow y documentación oficial de Flask/NumPy- [ ] Modo offline (sin CDNs)

- [ ] Tests automatizados (pytest)

---- [ ] Soporte para más de 5 variables (Simplex Revisado)



## 📞 Contacto## 📄 Licencia



**José Miguel Herrera Gutiérrez**  Este proyecto fue desarrollado con fines **educativos** para la Universidad Tecnológica de Pereira. El código es de libre uso para estudiantes y académicos.

Universidad Tecnológica de Pereira  

Investigación de Operaciones - 2025## 📧 Contacto



---**José Miguel Herrera Gutiérrez**  

Universidad Tecnológica de Pereira  

## 🔄 Historial de VersionesIngeniería de Sistemas y Computación



### Versión 3.0 (Octubre 2025) - ACTUAL---

- ✅ Corrección de notación científica (e-16 → 0)

- ✅ Limpieza de documentación (Markdown unificado)**⭐ Si este proyecto te fue útil, dale una estrella en GitHub!**

- ✅ README completo y profesional

- ✅ Estructura de proyecto limpia---



### Versión 2.0 (Octubre 2025)## 📚 Referencias

- ✅ Método Simplex con Dos Fases completo

- ✅ Dual-Simplex optimizado para MAX/MIN- Winston, W. L. (2004). *Operations Research: Applications and Algorithms*. Thomson Brooks/Cole.

- ✅ Corrección de errores de arrays NumPy- Hillier, F. S., & Lieberman, G. J. (2015). *Introduction to Operations Research*. McGraw-Hill Education.

- ✅ Templates Jinja2 corregidos- Taha, H. A. (2017). *Operations Research: An Introduction*. Pearson Education.

- Documentación de NumPy: https://numpy.org/doc/

### Versión 1.0 (Octubre 2025)- Documentación de Flask: https://flask.palletsprojects.com/

- ✅ Implementación inicial de tres métodos

- ✅ Interfaz web con FlaskThis application was developed as part of a university parcial in Operations Research, demonstrating practical implementation of linear programming concepts with modern web technologies.

- ✅ Visualización básica de resultados

## License

---

This project is developed for educational purposes. Feel free to use and modify for academic work.
**¡Listo para usar!** 🚀

Para iniciar: `python app.py` y navega a `http://localhost:5000`
