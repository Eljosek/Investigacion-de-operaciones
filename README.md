# 📊 Solucionador de Programación Lineal - Aplicación Web Educativa

**Investigación de Operaciones - Segundo Parcial**  
**Universidad Tecnológica de Pereira (UTP)**  
**Desarrollado por:** José Miguel Herrera Gutiérrez  
**Profesora:** Bibiana Patricia Arias Villada

**Última actualización:** 18 de Octubre de 2025  
**Versión:** 2.0 - Con Método de Dos Fases Completo

---

Una aplicación web completa para resolver problemas de programación lineal con **tres métodos diferentes**: Gráfico, Simplex (con Dos Fases) y Dual Simplex. Diseñada con enfoque educativo para visualizar **paso a paso** cada iteración del algoritmo.

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
| **Simplex** | 2-5+ variables | **<=, >=, =** | Simplex con Método de Dos Fases |
| **Dual Simplex** | MAX/MIN con >= | >= | Dual Simplex para MAX y MIN |

### 🆕 Novedades Versión 2.0

#### ✅ Método de Dos Fases Completo
- **Fase I:** Eliminación de variables artificiales
- **Fase II:** Optimización de función objetivo original
- **Soporte para restricciones >=, =**
- **Detección de infactibilidad** en Fase I
- **Transición automática** entre fases

#### ✅ Dual-Simplex Mejorado
- **Soporte para MAX y MIN**
- **Selección correcta de pivotes** según tipo de optimización
- **Factibilidad dual verificada**
- **Cálculo correcto de valor objetivo** para ambos tipos

#### ✅ Validaciones Robustas
- **Detección de problemas no acotados**
- **Detección de infactibilidad**
- **Mensajes de error claros y educativos**
- **Bland's Rule** para evitar cycling

### 📚 Enfoque Educativo
- **Visualización paso a paso** de cada iteración
- **Tableau completo** con variables de holgura/exceso/artificiales
- **Pivotes identificados** con colores
- **Ratios calculados** (θ para Simplex, zⱼ/aᵢⱼ para Dual)
- **Explicaciones claras** de cada paso
- **Variables básicas/no básicas** marcadas
- **Indicadores de fase** (Fase I/II en Dos Fases)

### 🛠️ Implementación Manual
- **Sin librerías externas** de optimización (no PuLP, no SciPy)
- **NumPy puro** para operaciones matriciales
- **Algoritmos escritos desde cero** para fines educativos
- **Código bien documentado** y legible
- **Tolerancia numérica** (EPS = 1e-9)

## 🚀 Inicio Rápido

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno (Chrome, Firefox, Edge)

### Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Eljosek/Investigacion-de-operaciones.git
   cd "Investigacion de operaciones"
   ```

2. **Crear entorno virtual** (recomendado):
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

5. **Abrir en el navegador**: `http://localhost:5000`

## 📖 Guía de Uso

### Método Gráfico (2 Variables)

**Problema de Ejemplo:**
```
Maximizar: Z = 3x₁ + 5x₂
Sujeto a:
  2x₁ + 3x₂ ≤ 10
  1x₁ + 4x₂ ≤ 8
  3x₁ + 2x₂ ≤ 12
  x₁, x₂ ≥ 0
```

**Formato de Entrada:**
- Función objetivo: `3x1 + 5x2`
- Restricciones (una por línea):
  ```
  2 3 <= 10
  1 4 <= 8
  3 2 <= 12
  ```

**Resultado:**
- Gráfica con región factible sombreada
- Vértices del poliedro marcados
- Punto óptimo destacado
- Valor óptimo de Z
- Análisis de restricciones activas/inactivas

### Método Simplex (2-5+ Variables)

**Problema de Ejemplo:**
```
Maximizar: Z = 4x₁ + 3x₂ + 2x₃
Sujeto a:
  2x₁ + 1x₂ + 1x₃ ≤ 6
  1x₁ + 2x₂ + 3x₃ ≤ 9
  x₁, x₂, x₃ ≥ 0
```

**Formato de Entrada:**
- Tipo: Maximizar
- Variables: 3
- Restricciones: 2
- Coeficientes objetivo: `4 3 2`
- Restricciones:
  ```
  2 1 1 <= 6
  1 2 3 <= 9
  ```

**Resultado:**
- Tableau inicial con variables de holgura
- Iteraciones paso a paso
- Columna pivote (variable entrante) marcada en verde
- Fila pivote (variable saliente) marcada en naranja
- Ratios θ = b/a (mínimo ratio positivo)
- Tableau final con solución óptima
- Variables básicas y sus valores

### Método Dual Simplex (Problemas Duales)

**Problema de Ejemplo:**
```
Minimizar: Z = 2x₁ + 3x₂
Sujeto a:
  1x₁ + 2x₂ ≥ 4
  3x₁ + 1x₂ ≥ 6
  x₁, x₂ ≥ 0
```

**Formato de Entrada:**
- Tipo: Minimizar
- Variables: 2
- Restricciones: 2
- Coeficientes objetivo: `2 3`
- Restricciones:
  ```
  1 2 >= 4
  3 1 >= 6
  ```

**Resultado:**
- Tableau con restricciones ≥ (variables de exceso)
- Iteraciones del algoritmo dual
- Fila pivote (RHS negativo más negativo)
- Columna pivote (ratios zⱼ/aᵢⱼ)
- Ratios duales calculados y mostrados
- Solución óptima del problema dual

## 🔧 Stack Tecnológico

### Backend
- **Flask 3.1.2** - Framework web minimalista
- **Python 3.13.7** - Lenguaje de programación
- **NumPy 2.3.3** - Operaciones matriciales
- **Matplotlib 3.10.1** - Generación de gráficas (método gráfico)

### Frontend
- **Bootstrap 5.3** - Framework CSS responsivo
- **Font Awesome 6.6** - Iconos vectoriales
- **Google Fonts** - Poppins (títulos) e Inter (texto)
- **JavaScript ES6** - Interacciones del cliente
- **CSS Variables** - Sistema de tematización

### Características CSS
- **25+ variables CSS** para colores y tipografía
- **4 animaciones** (fade-in, slide-up, pulse, gradient-shift)
- **Clases por método** (.method-grafico, .method-simplex, .method-dual)
- **Modo oscuro** con prefers-color-scheme
- **Gradientes** para CTAs y hero section

## 📁 Estructura del Proyecto

```
Investigacion-de-operaciones/
├── app.py                      # 🌐 Aplicación Flask con routes
├── lp_solver.py                # 📈 Método Gráfico (2 variables)
├── simplex_tableau.py          # 🔢 Método Simplex (NumPy)
├── dual_simplex_tableau.py     # 🔄 Método Dual Simplex (NumPy)
├── requirements.txt            # 📦 Dependencias (Flask, NumPy, Matplotlib)
├── CHANGELOG.md                # 📝 Historial de cambios (8 fases)
├── README.md                   # 📖 Este archivo
├── .gitignore                  # 🚫 Archivos ignorados (venv, __pycache__)
│
├── static/
│   ├── css/
│   │   └── styles.css          # 🎨 ~700 líneas de CSS personalizado
│   ├── images/                 # 🖼️ (vacío, para futuras imágenes)
│   └── js/
│       └── app.js              # ⚡ JavaScript del cliente
│
└── templates/
    ├── base.html               # 📄 Layout base con navbar y footer
    ├── index.html              # 🏠 Homepage (~360 líneas)
    ├── simplex.html            # 📝 Formulario Simplex con tooltips
    ├── simplex_results.html    # 📊 Visualización Simplex (401 líneas)
    ├── dual_simplex.html       # 📝 Formulario Dual con tooltips
    ├── dual_simplex_results.html  # 📊 Visualización Dual (424 líneas)
    ├── about.html              # 📚 Acerca de (~450 líneas)
    ├── examples.html           # 💡 Ejemplos de problemas
    └── 404.html                # ❌ Página de error
```

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
- `=` : Igualdad

## 🐛 Solución de Problemas

### Error: "Import flask could not be resolved"
**Solución:** Activa el entorno virtual antes de ejecutar:
```bash
.venv\Scripts\activate  # Windows
python app.py
```

### Error: "No module named numpy"
**Solución:** Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Gráfica no se muestra (Método Gráfico)
**Causa:** Problema con matplotlib backend  
**Solución:** Asegúrate de tener matplotlib instalado correctamente

### Servidor no arranca en puerto 5000
**Solución:** Cambia el puerto en `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

### Tooltips no funcionan
**Solución:** Verifica que Bootstrap JS esté cargado correctamente (requiere internet para CDN)

## 📊 Algoritmos Implementados

### Método Gráfico
1. **Parsing de restricciones** con regex
2. **Cálculo de intersecciones** entre rectas
3. **Determinación de región factible** con desigualdades
4. **Evaluación en vértices** de la función objetivo
5. **Generación de gráfica** con matplotlib

### Método Simplex
1. **Construcción del tableau inicial** con variables de holgura
2. **Criterio de optimalidad**: zⱼ - cⱼ ≤ 0 para maximización
3. **Selección de variable entrante**: zⱼ - cⱼ más positivo
4. **Selección de variable saliente**: mínimo ratio θ = bᵢ/aᵢⱼ
5. **Operaciones de pivote** (Gauss-Jordan)
6. **Iteración** hasta optimalidad o unboundedness

### Método Dual Simplex
1. **Verificación de factibilidad dual**: zⱼ - cⱼ ≤ 0
2. **Selección de fila pivote**: RHS más negativo
3. **Selección de columna pivote**: mínimo ratio zⱼ/aᵢⱼ (negativo)
4. **Operaciones de pivote** para restaurar factibilidad primal
5. **Iteración** hasta factibilidad y optimalidad

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

This application was developed as part of a university parcial in Operations Research, demonstrating practical implementation of linear programming concepts with modern web technologies.

## License

This project is developed for educational purposes. Feel free to use and modify for academic work.