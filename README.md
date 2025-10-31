# 📊 Solucionador de Programación Lineal - Aplicación Web Educativa

**Investigación de Operaciones - Segundo Parcial**  
**Universidad Tecnológica de Pereira (UTP)**

**Desarrollado por:** José Miguel Herrera Gutiérrez  
**Profesora:** Bibiana Patricia Arias Villada  
**Versión:** 3.0  
**Fecha:** Octubre 2025

---

## 📋 Descripción

Aplicación web completa para resolver problemas de **Programación Lineal** con tres métodos diferentes:

1. **Método Gráfico** - Para problemas con 2 variables
2. **Método Simplex** - Para múltiples variables con restricciones <=
3. **Método Dual-Simplex** - Optimizado para problemas con restricciones >=

La aplicación está diseñada con **enfoque educativo**, mostrando paso a paso cada iteración del algoritmo con tablas (tableau) completas, variables básicas, operaciones de pivoteo y valores objetivo.

## ✨ Características Principales

### 🎨 Interfaz Moderna
- **Diseño responsivo** con Bootstrap 5
- **Modo oscuro** con variables CSS personalizadas
- **Colores distintivos** por método (Azul/Verde/Púrpura)
- **Iconos Font Awesome** para mejor UX
- **Tooltips interactivos** en formularios
- **Navegación fluida** con smooth scroll

### 🔢 Tres Métodos de Solución

| Método | Ideal Para | Restricciones | Algoritmo |
|--------|------------|---------------|-----------|
| **Gráfico** | 2 variables | <= | Intersecciones y vértices |
| **Simplex** | 2-5+ variables | <= | Simplex estándar con tableau |
| **Dual Simplex** | MIN con >= | >= | Dual Simplex para MAX y MIN |

### 🎯 Funcionalidades

- ✅ **Tres métodos de solución** con algoritmos optimizados
- ✅ **Visualización paso a paso** de iteraciones
- ✅ **Tablas (tableau) interactivas** con resaltado de pivotes
- ✅ **Soporte para restricciones** `<=`, `>=`
- ✅ **Detección automática** de infactibilidad y no acotamiento
- ✅ **Exportación a PDF** de resultados (función de impresión)
- ✅ **Ejemplos precargados** para cada método
- ✅ **Interfaz responsiva** con Bootstrap 5

### 📚 Enfoque Educativo

- **Visualización paso a paso** de cada iteración
- **Tableau completo** con variables de holgura/exceso
- **Pivotes identificados** con colores
- **Ratios calculados** (θ para Simplex, zⱼ/aᵢⱼ para Dual)
- **Explicaciones claras** de cada paso
- **Variables básicas/no básicas** marcadas

### 🛠️ Implementación Manual

- **Sin librerías externas** de optimización (no PuLP, no SciPy)
- **NumPy puro** para operaciones matriciales
- **Algoritmos escritos desde cero** para fines educativos
- **Código bien documentado** y legible
- **Tolerancia numérica** (EPS = 1e-9)

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.13.7**
- **Flask 3.1.2** - Framework web
- **NumPy 2.3.3** - Operaciones matriciales
- **Matplotlib 3.10.1** - Gráficos del método gráfico

### Frontend
- **HTML5** con plantillas Jinja2
- **CSS3** con variables personalizadas
- **JavaScript ES6+**
- **Bootstrap 5.3** - Framework CSS
- **Font Awesome 6.6** - Iconos
- **Google Fonts** - Poppins (títulos) e Inter (texto)

### Características CSS
- **25+ variables CSS** para colores y tipografía
- **4 animaciones** (fade-in, slide-up, pulse, gradient-shift)
- **Clases por método** (.method-grafico, .method-simplex, .method-dual)
- **Modo oscuro** con prefers-color-scheme
- **Gradientes** para CTAs y hero section

---

## 📁 Estructura del Proyecto

```
Investigacion-de-operaciones/
├── app.py                      # 🌐 Aplicación Flask con routes
├── lp_solver.py                # 📈 Método Gráfico (2 variables)
├── simplex_tableau.py          # 🔢 Método Simplex (NumPy)
├── dual_simplex_tableau.py     # 🔄 Método Dual Simplex (NumPy)
├── requirements.txt            # 📦 Dependencias (Flask, NumPy, Matplotlib)
├── README.md                   # 📖 Este archivo
├── .gitignore                  # 🚫 Archivos ignorados (venv, __pycache__)
│
├── static/
│   ├── css/
│   │   └── styles.css          # 🎨 ~700 líneas de CSS personalizado
│   ├── images/                 # 🖼️ (para futuras imágenes)
│   └── js/
│       └── app.js              # ⚡ JavaScript del cliente
│
├── templates/
│   ├── base.html               # 📄 Layout base con navbar y footer
│   ├── index.html              # 🏠 Homepage
│   ├── about.html              # 📚 Acerca de
│   ├── examples.html           # 💡 Ejemplos de problemas
│   ├── simplex.html            # 📝 Formulario Simplex
│   ├── simplex_results.html    # 📊 Visualización Simplex
│   ├── dual_simplex.html       # 📝 Formulario Dual Simplex
│   ├── dual_simplex_results.html  # 📊 Visualización Dual Simplex
│   └── 404.html                # ❌ Página de error
│
└── test_*.py                   # 🧪 Scripts de prueba
```

---

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/Eljosek/Investigacion-de-operaciones.git
cd Investigacion-de-operaciones
```

### Paso 2: Crear entorno virtual

**Windows:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

---

## 📚 Uso de la Aplicación

### Método Gráfico

**Ideal para:** Problemas con 2 variables

**Ejemplo:**
```
Función Objetivo: maximizar z = 3x + 5y
Restricciones:
  x + y <= 4
  2x + y <= 6
  x >= 0
  y >= 0
```

### Método Simplex

**Ideal para:** Problemas con múltiples variables y restricciones <=

**Ejemplo:**
```
Función Objetivo: maximizar z = 3x1 + 2x2 + x3
Restricciones:
  x1 + x2 + x3 <= 10
  2x1 + x2 <= 8
  x1 + 2x3 <= 6
  x1 >= 0
  x2 >= 0
  x3 >= 0
```

**Características:**
- Tableau inicial con variables de holgura
- Iteraciones paso a paso mostradas
- Columna pivote (variable entrante) marcada en verde
- Fila pivote (variable saliente) marcada en naranja
- Ratios θ = b/a calculados
- Solución óptima con variables básicas

### Método Dual-Simplex

**Ideal para:** Problemas de minimización con restricciones >=

**Ejemplo:**
```
Función Objetivo: minimizar z = 3x1 + 2x2
Restricciones:
  3x1 + x2 >= 3
  4x1 + 3x2 >= 6
  x1 + x2 <= 3
  x1 >= 0
  x2 >= 0
```

---

## 🎓 Algoritmos Implementados

### 1. Método Gráfico
1. Graficar todas las restricciones
2. Identificar la región factible
3. Encontrar vértices (puntos de intersección)
4. Evaluar función objetivo en cada vértice
5. Seleccionar el vértice con mejor valor

### 2. Método Simplex
1. **Construcción del tableau inicial** con variables de holgura
2. **Criterio de optimalidad**: zⱼ - cⱼ ≤ 0 para maximización
3. **Selección de variable entrante**: zⱼ - cⱼ más positivo
4. **Selección de variable saliente**: mínimo ratio θ = bᵢ/aᵢⱼ
5. **Operaciones de pivote** (Gauss-Jordan)
6. **Iteración** hasta optimalidad o unboundedness

### 3. Método Dual Simplex
1. **Verificación de factibilidad dual**: zⱼ - cⱼ ≤ 0
2. **Selección de fila pivote**: RHS más negativo
3. **Selección de columna pivote**: mínimo ratio zⱼ/aᵢⱼ (negativo)
4. **Operaciones de pivote** para restaurar factibilidad primal
5. **Iteración** hasta factibilidad y optimalidad

---

## 💡 Ejemplos de Problemas

### Ejemplo 1: Maximización Simple (Gráfico)
```
Maximizar Z = 40x₁ + 30x₂
Restricciones:
  2x₁ + 1x₂ ≤ 8   (Recurso A)
  1x₁ + 2x₂ ≤ 10  (Recurso B)
  x₁, x₂ ≥ 0
```
**Solución:** x₁=2, x₂=4, Z=200

### Ejemplo 2: Problema Multivariable (Simplex)
```
Maximizar Z = 5x₁ + 4x₂ + 3x₃
Restricciones:
  2x₁ + 3x₂ + 1x₃ ≤ 5
  4x₁ + 1x₂ + 2x₃ ≤ 11
  3x₁ + 4x₂ + 2x₃ ≤ 8
  x₁, x₂, x₃ ≥ 0
```
**Solución:** x₁=2, x₂=0, x₃=1, Z=13

### Ejemplo 3: Minimización con ≥ (Dual Simplex)
```
Minimizar Z = 8x₁ + 12x₂
Restricciones:
  1x₁ + 2x₂ ≥ 10  (Demanda mínima)
  2x₁ + 1x₂ ≥ 12  (Producción mínima)
  x₁, x₂ ≥ 0
```
**Solución:** x₁=4.67, x₂=2.67, Z=69.33

---

## 🧪 Testing

### Ejecutar Tests

```bash
# Test Ejemplo 1 (Dual-Simplex)
python test_ejemplo1.py

# Test Ejemplo 2 (Simplex)
python test_ejemplo2.py

# Test Ejemplo 3 (Restricciones mixtas)
python test_ejemplo3.py

# Test de Petición Web
python test_web_request.py
```

### Resultados Esperados

Todos los tests deben pasar mostrando:
- ✅ Valor óptimo correcto
- ✅ Variables con valores correctos
- ✅ Número correcto de iteraciones
- ✅ Sin errores de arrays NumPy
- ✅ Sin notación científica (e-16)

---

## 🐛 Solución de Problemas

### El servidor no inicia

```bash
# Verificar puerto ocupado
netstat -ano | findstr :5000

# Matar proceso si es necesario (Windows)
taskkill /F /PID <número_de_pid>

# O cambiar puerto en app.py
app.run(debug=True, port=5001)
```

### Error de importación de módulos

```bash
# Reinstalar dependencias
pip install -r requirements.txt --force-reinstall
```

### Errores con NumPy

```bash
# Actualizar NumPy
pip install --upgrade numpy
```

### Gráfica no se muestra (Método Gráfico)

**Causa:** Problema con matplotlib backend  
**Solución:** Asegúrate de tener matplotlib instalado correctamente

### Servidor no arranca en puerto 5000

**Solución:** Cambia el puerto en `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

---

## 🔧 Mejoras Técnicas Implementadas

### Corrección de Valores Numéricos

**Problema:** Aparecían valores como `4.441e-16` (notación científica para números muy pequeños)

**Causa:** Errores de precisión en operaciones de punto flotante

**Solución implementada:**
```python
def _clean_small_values(self, value: float, tolerance: float = 1e-10) -> float:
    """Redondea valores muy pequeños a 0"""
    if abs(value) < tolerance:
        return 0.0
    return value
```

Todos los valores menores a `1e-10` (0.0000000001) se redondean a 0, eliminando la notación científica innecesaria.

### Manejo de Tipos de Datos

- Uso correcto de `float()` para elementos individuales de arrays NumPy
- Uso de `np.all()` y `np.any()` para comparaciones de arrays completos
- Evita el error: "The truth value of an array with more than one element is ambiguous"

### Variables de Template

- Backend envía `solution` (no `variables`)
- Backend envía `objective_value` (no `z_value`)
- Campo `opt_type` agregado para distinguir MAX/MIN
- Estructura consistente entre todos los métodos

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
