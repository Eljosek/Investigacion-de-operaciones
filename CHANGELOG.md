# CHANGELOG - Optimización del Proyecto de Programación Lineal

**Fecha:** 17 de Octubre, 2025  
**Autor:** José Miguel Herrera Gutiérrez  
**Proyecto:** Investigación de Operaciones - Segundo Parcial UTP

---

## 📚 FASE 5: REESCRITURA COMPLETA DE SECCIÓN ABOUT ✅

### 🔧 Archivos Modificados

#### 1. **templates/about.html** (Reescritura completa)
   - **Cambios:**
     - **Contenido balanceado entre los 3 métodos:**
       - Eliminado sesgo hacia método gráfico únicamente
       - Secciones detalladas para Gráfico, Simplex, y Dual Simplex con igual profundidad
       - Cada método tiene: fundamento teórico, procedimiento paso a paso, ventajas, limitaciones, y casos de uso
     
     - **Estructura reorganizada:**
       - **Introducción a PL:** Componentes (variables, función objetivo, restricciones) y aplicaciones prácticas
       - **Tarjetas de métodos:** Cards visuales con colores distintivos (azul/verde/púrpura) y botones CTA
       - **Secciones detalladas por método:**
         - Método Gráfico: Procedimiento en 5 pasos, teorema fundamental, casos ideales
         - Método Simplex: Fundamento (vértices del poliedro), 6 fases del algoritmo, ventajas de escalabilidad
         - Dual Simplex: Concepto de dualidad, procedimiento con ratios zⱼ/aᵢⱼ, aplicaciones especiales
       - **Tabla comparativa:** Características lado a lado de los 3 métodos
       - **Características de la app:** Enfoque educativo, implementación técnica, sistema de diseño
     
     - **Contenido educativo mejorado:**
       - Explicación de teorema fundamental de PL (solución en vértices)
       - Diferencias clave entre Simplex (columna primero) y Dual (fila primero)
       - Highlighting de visualizaciones pedagógicas (pivotes, RHS negativo)
       - Casos de uso específicos por método
     
     - **Información técnica:**
       - Stack tecnológico: Python 3.13, Flask 3.1, NumPy, Matplotlib, Bootstrap 5
       - Algoritmos implementados manualmente (no solo wrappers)
       - Sistema de colores distintivos y modo oscuro
     
     - **Sección académica:**
       - Universidad Tecnológica de Pereira (UTP)
       - Profesora Bibiana Patricia Arias Villada
       - Desarrollador José Miguel Herrera Gutiérrez
       - Badges de tecnologías utilizadas
   
   - **Estadísticas:**
     - De ~386 líneas a ~450 líneas
     - 3 secciones detalladas (una por método)
     - 1 tabla comparativa con 6 características
     - Contenido académico y profesional balanceado
   
   - **Impacto:** 
     - Transforma la página de "solo gráfico" a "guía completa de 3 métodos"
     - Proporciona valor educativo para entender cuándo usar cada método
     - Mejora percepción de completitud y profesionalismo del proyecto

### ✨ Contenido Nuevo Destacado

**Método Gráfico - Detalle:**
- Procedimiento: graficar restricciones → región factible → vértices → evaluar Z → seleccionar óptimo
- Teorema: Si existe óptimo finito, está en un vértice
- Casos ideales: mezcla 2 productos, 2 recursos, enseñanza

**Método Simplex - Detalle:**
- Fundamento: Movimiento sistemático entre vértices del poliedro convexo
- 6 fases: forma estándar → tableau inicial → test optimalidad → selección pivote → operaciones fila → iterar
- Ventajas: escalable (cientos de variables), eficiente en práctica, robusto

**Método Dual Simplex - Detalle:**
- Concepto: Solución dual factible → factibilidad primal, manteniendo optimalidad dual
- Procedimiento: fila saliente (RHS más negativo) → columna entrante (ratio zⱼ/aᵢⱼ mínimo) → pivot
- Diferencia clave: Orden invertido vs Simplex (fila primero, columna después)
- Aplicaciones: post-optimización, sensibilidad, problemas con ≥, branch & bound

**Tabla Comparativa:**
| Característica | Gráfico | Simplex | Dual Simplex |
|---|---|---|---|
| Variables | 2 | 2 a n | 2 a n |
| Complejidad visual | Baja | Media | Media-Alta |
| Aprendizaje | Excelente | Muy bueno | Avanzado |
| Restricciones ideales | ≤, ≥, = | ≤ (max) | ≥ (min) |
| Visualización | Gráfica | Tableau | Tableau + ratios |

### 🎯 Resultado

La sección About ahora:
- **Educa completamente** sobre los 3 métodos con igual profundidad
- **Guía la selección** del método adecuado según el problema
- **Demuestra profesionalismo** académico y técnico
- **Usa colores distintivos** (azul/verde/púrpura) consistentes con el diseño
- **Proporciona contexto** académico completo (UTP, profesora, estudiante)

---

## 🎨 FASE 4: TEMATIZACIÓN UI/UX Y MODERNIZACIÓN VISUAL ✅

### 🎨 Diseño y Paleta de Colores

Se implementó un sistema de colores distintivo para cada método de LP:

- **Método Gráfico:** Azul (`#2563eb` - blue-600)
- **Método Simplex:** Verde (`#16a34a` - green-600)
- **Método Dual Simplex:** Púrpura (`#9333ea` - purple-600)

Cada color incluye variantes light y dark para gradientes y modo oscuro.

### 🔧 Archivos Modificados

#### 1. **static/css/styles.css** (Reescritura completa)
   - **Cambios:**
     - **Tipografía moderna:**
       - Importación de Google Fonts (Poppins para encabezados, Inter para texto)
       - Jerarquía tipográfica mejorada (h1-h6 con tamaños y pesos específicos)
       - Rendering optimizado con `-webkit-font-smoothing: antialiased`
     
     - **Sistema de variables CSS:**
       - Variables de color para cada método con variantes light/dark
       - Sistema de sombras (sm/md/lg/xl) para profundidad visual
       - Variables de transición (fast/base/slow) para animaciones consistentes
       - Soporte completo para modo oscuro con tema personalizado
     
     - **Clases específicas por método:**
       - `.method-grafico`, `.method-simplex`, `.method-dual` para contenedores
       - `.text-method-*` para textos con colores del método
       - `.badge-*` para badges temáticos
       - `.bg-*-simplex`, `.bg-*-dual` para fondos con gradientes
     
     - **Componentes rediseñados:**
       - **Navbar:** Gradiente oscuro, animaciones en hover con línea subrayado amarillo
       - **Cards:** Bordes redondeados (16px), hover con elevación y transform
       - **Botones:** Gradientes, efecto ripple con ::before, hover con elevación
       - **Formularios:** Bordes redondeados (12px), focus con glow sutil
       - **Tablas:** Headers temáticos, hover con transform, striped mejorado
       - **Accordions:** Para iteraciones de tableau con styling mejorado
     
     - **Animaciones añadidas:**
       - `slideInDown` para alertas
       - `fadeInUp` para cards al cargar
       - `spin` para estados de loading
       - `pulse` para elementos importantes
       - Transiciones suaves en hover y focus
     
     - **Clases de highlighting:**
       - `.pivot-row`, `.pivot-col`, `.pivot-element` para tableau
       - `.negative-rhs` para filas con RHS negativo en Dual Simplex
     
     - **Mejoras de UX:**
       - Scrollbar personalizado con gradientes
       - Efectos glass (backdrop-filter) para elementos flotantes
       - Estados de loading con spinner animado
       - Responsividad mejorada para mobile (768px, 576px)
       - Dark mode completo con variables actualizadas
   
   - **Impacto:** Transformación visual completa con identidad distintiva por método

#### 2. **templates/index.html**
   - **Cambios:**
     - Cards de métodos con clases `.method-grafico`, `.method-simplex`, `.method-dual`
     - Iconos más grandes (fa-3x) con colores temáticos
     - Botones actualizados con iconos y colores correctos
     - Sombras y bordes eliminados en favor de shadow utilities
   - **Impacto:** Homepage más atractivo con diferenciación clara de métodos

#### 3. **templates/simplex.html**
   - **Cambios:**
     - Botón actualizado a `btn-success` con gradiente verde
     - Clase contenedora `.method-simplex` aplicada
   - **Impacto:** Consistencia visual con tema verde Simplex

#### 4. **templates/dual_simplex.html**
   - **Cambios:**
     - Botón actualizado a `btn-info` (púrpura) en lugar de warning
     - Clase contenedora `.method-dual` aplicada
   - **Impacto:** Identidad visual púrpura para Dual Simplex

#### 5. **templates/simplex_results.html**
   - **Cambios:**
     - Headers de cards con `.bg-success-simplex` (gradiente verde)
     - Tabla con clase `.table-success` para header verde
     - Badge actualizado a `.badge-simplex`
     - Textos de título con `.text-simplex`
   - **Impacto:** Resultados temáticos con verde Simplex

#### 6. **templates/dual_simplex_results.html**
   - **Cambios:**
     - Headers de cards con `.bg-info-dual` (gradiente púrpura)
     - Tabla con clase `.table-info` para header púrpura
     - Badge actualizado a `.badge-dual`
     - Textos de título con `.text-dual`
   - **Impacto:** Resultados temáticos con púrpura Dual Simplex

### ✨ Características Nuevas

1. **Sistema de Diseño Coherente:**
   - Paleta de colores profesional con significado semántico
   - Espaciado y sizing consistentes
   - Jerarquía visual clara

2. **Animaciones Sutiles:**
   - Transiciones suaves en hover/focus (0.2s-0.4s)
   - Efectos de elevación en cards y botones
   - Loading states con spinner animado

3. **Accesibilidad Mejorada:**
   - Contraste adecuado en texto y fondos
   - Focus states visibles en formularios
   - Hover states claros en elementos interactivos

4. **Modo Oscuro Completo:**
   - Variables CSS actualizadas para dark theme
   - Fondos y bordes adaptados
   - Tablas y formularios con styling específico

5. **Pedagogía Visual:**
   - Colores distintivos ayudan a identificar método actual
   - Highlighting en tableaux para elementos clave (pivotes, RHS negativo)
   - Badges informativos sobre número de iteraciones

### 📊 Estadísticas

- **Líneas CSS totales:** ~700 (incremento de +300 desde original)
- **Variables CSS nuevas:** 25+ (colores, sombras, transiciones)
- **Animaciones CSS:** 4 (slideInDown, fadeInUp, spin, pulse)
- **Clases utilitarias nuevas:** 15+ (method-*, text-*, badge-*, bg-*)
- **Templates actualizados:** 5 archivos

### 🔍 Detalles Técnicos

**Gradientes implementados:**
```css
/* Simplex */
background: linear-gradient(135deg, #16a34a 0%, #4ade80 100%);

/* Dual Simplex */
background: linear-gradient(135deg, #9333ea 0%, #c084fc 100%);

/* Gráfico */
background: linear-gradient(135deg, #2563eb 0%, #60a5fa 100%);
```

**Sombras:**
```css
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
```

### 🎯 Resultado

La interfaz ahora presenta:
- **Identidad visual clara** por método con paleta profesional
- **Animaciones sutiles** que mejoran UX sin distraer
- **Tipografía moderna** con Google Fonts
- **Componentes consistentes** con design system coherente
- **Accesibilidad mejorada** con contraste y focus states
- **Modo oscuro completo** para preferencia de usuario

---

## 📋 FASE 3: VISUALIZACIÓN PASO A PASO MÉTODO DUAL SIMPLEX ✅

### ➕ Archivos Creados

#### 1. **dual_simplex_tableau.py**
   - **Razón:** Implementación manual del algoritmo Dual Simplex con registro de iteraciones
   - **Características:**
     - Clase `DualSimplexTableau` con construcción de tableau desde cero
     - Conversión automática de restricciones >= a <= (multiplicando por -1)
     - Identificación de fila saliente (RHS más negativo - solución no factible)
     - Cálculo de ratios z_j / a_ij para seleccionar columna entrante
     - Registro completo de cada iteración con ratios calculados
     - Documentación de operaciones de fila
     - Soporte para minimización (ideal para Dual Simplex)
     - Manejo de casos: óptimo, no factible, máximo de iteraciones
   - **Impacto:** Permite mostrar paso a paso el método Dual para propósitos educativos

### 🔧 Archivos Modificados

#### 1. **app.py**
   - **Cambios:**
     - Importado módulo `dual_simplex_tableau`
     - Ruta `/solve-dual-simplex` ahora usa `dual_simplex_tableau.solve_dual_simplex_tableau()`
     - Pasando `iterations` al template para mostrar paso a paso
   - **Líneas modificadas:** 15 (import), 134-152 (ruta dual-simplex)

#### 2. **templates/dual_simplex_results.html**
   - **Cambios:**
     - Iniciado reescritura del acordeón de iteraciones
     - Preparado para mostrar tableau completo por iteración
     - Header actualizado con badge de iteraciones
     - Alert informativo sobre método Dual Simplex
   - **Estado:** Parcialmente actualizado (estructura del acordeón definida)
   - **Pendiente:** Implementación completa del contenido de cada iteración con tableau

#### 3. **test_tableau.py**
   - **Cambios:**
     - Actualizado para probar el solver Dual Simplex
     - Test con problema de minimización: min z=2x1+3x2 s.a. x1+2x2>=6, 2x1+x2>=8

### 🐛 Correcciones de Bugs

#### 1. **Valor óptimo negativo en minimización (Dual Simplex)**
   - **Problema:** El solver retornaba -10.6667 cuando debía ser 10.6667
   - **Causa:** El RHS de Z en el tableau es negativo para minimización
   - **Solución:** Negar el valor al construir la solución: `optimal_value = -self.tableau[-1, -1]`
   - **Archivos afectados:** `dual_simplex_tableau.py` líneas 87, 257

### ✅ Pruebas Realizadas

- **Caso de prueba:** min z = 2x1 + 3x2 s.a. x1 + 2x2 ≥ 6, 2x1 + x2 ≥ 8
- **Resultado esperado:** Z = 10.6667, x1 = 3.3333, x2 = 1.3333
- **Resultado obtenido:** ✓ Correcto
- **Iteraciones:** 3 (inicial + 2 pivotes)
- **Verificación:** z = 2(3.3333) + 3(1.3333) = 6.6666 + 4 = 10.6666 ✓

### 📊 Estadísticas

- **Líneas de código añadidas:** ~424 (dual_simplex_tableau.py)
- **Líneas modificadas:** ~20 (app.py + imports)
- **Algoritmo:** Dual Simplex con selección de pivote por ratio mínimo
- **Funcionalidad educativa:** 100% - muestra cálculos de ratios y RHS negativos

### 🎯 Diferencias clave Dual Simplex vs Simplex Primal

1. **Selección de fila saliente:** RHS más negativo (en lugar de ratio mínimo)
2. **Selección de columna entrante:** Ratio z_j/a_ij con a_ij<0, elegir menos negativo
3. **Optimalidad:** Todos los RHS ≥ 0 (factibilidad primal alcanzada)
4. **Uso típico:** Problemas de minimización con restricciones >=

---

## 📋 FASE 2: VISUALIZACIÓN PASO A PASO MÉTODO SIMPLEX ✅

### ➕ Archivos Creados

#### 1. **simplex_tableau.py**
   - **Razón:** Implementación manual del algoritmo Simplex con registro de iteraciones
   - **Características:**
     - Clase `SimplexTableau` con construcción de tableau desde cero
     - Registro completo de cada iteración (tableau, variables básicas, pivotes)
     - Identificación automática de columna y fila pivote
     - Documentación de operaciones de fila realizadas
     - Soporte para maximización y minimización
     - Manejo de casos: óptimo, no acotado, máximo de iteraciones
   - **Impacto:** Permite mostrar paso a paso el algoritmo para propósitos educativos

#### 2. **test_tableau.py**
   - **Razón:** Script de prueba para verificar el solver tableau
   - **Impacto:** Testing temporal (será eliminado después)

### 🔧 Archivos Modificados

#### 1. **app.py**
   - **Cambios:**
     - Importado módulo `simplex_tableau`
     - Ruta `/solve-simplex` ahora usa `simplex_tableau.solve_simplex_tableau()`
     - Pasando `iterations` al template para mostrar paso a paso
   - **Líneas modificadas:** 14 (import), 103-119 (ruta simplex)

#### 2. **templates/simplex_results.html**
   - **Cambios:**
     - Reescrito completamente el acordeón de iteraciones
     - Tabla HTML con tableau completo por iteración
     - Resaltado de columna pivote (amarillo) y fila pivote (amarillo)
     - Elemento pivote resaltado en rojo
     - Identificación visual de variable entrante/saliente
     - Numeración de iteraciones (0, 1, 2, ... hasta óptimo)
     - Muestra valor de Z en cada iteración
     - Operaciones de fila documentadas
     - Variables básicas actuales por iteración
   - **Características visuales:**
     - Acordeón Bootstrap para navegación
     - Íconos para iteración inicial, en progreso y óptimo
     - Código de colores consistente (verde=success, amarillo=warning, rojo=pivot)
     - Responsivo y accesible

### 🐛 Correcciones de Bugs

#### 1. **Valor óptimo negativo en maximización**
   - **Problema:** El solver retornaba -9.0 cuando debía ser 9.0
   - **Causa:** Doble negación al convertir max→min y al leer el resultado
   - **Solución:** Simplificado la lógica, manteniendo -c en fila Z para max, leyendo RHS directamente
   - **Archivos afectados:** `simplex_tableau.py` líneas 28-29, 85, 218-219

### ✅ Pruebas Realizadas

- **Caso de prueba:** max z = 3x1 + 2x2 s.a. x1 + x2 ≤ 4, 2x1 + x2 ≤ 5
- **Resultado esperado:** Z = 9.0, x1 = 1.0, x2 = 3.0
- **Resultado obtenido:** ✓ Correcto
- **Iteraciones:** 3 (inicial + 2 pivotes)

### 📊 Estadísticas

- **Líneas de código añadidas:** ~420 (simplex_tableau.py + template)
- **Líneas modificadas:** ~30 (app.py + imports)
- **Complejidad temporal:** O(n×m) por iteración del Simplex
- **Funcionalidad educativa:** 100% - muestra TODAS las iteraciones con detalle

---

## 📋 FASE 1: LIMPIEZA DEL PROYECTO ✅

### ❌ Archivos Eliminados

#### 1. **Attached HTML and CSS Context.txt**
   - **Razón:** Archivo temporal de contexto HTML/CSS que no tiene utilidad funcional
   - **Tipo:** Temporal/Innecesario
   - **Impacto:** Ninguno - archivo de prueba

#### 2. **DOCUMENTACION_COMPLETA.md**
   - **Razón:** Documentación del primer parcial (solo método gráfico), ahora obsoleta
   - **Tipo:** Documentación desactualizada
   - **Impacto:** Ninguno - contenido duplicado en README.md actualizado

#### 3. **INSTRUCCIONES_SUSTENTACION.md**
   - **Razón:** Instrucciones específicas del primer parcial, ya no aplicables
   - **Tipo:** Documentación temporal
   - **Impacto:** Ninguno - información obsoleta

#### 4. **REPORTE_FINAL.md**
   - **Razón:** Reporte del primer parcial, no refleja el proyecto actual con 3 métodos
   - **Tipo:** Documentación desactualizada
   - **Impacto:** Ninguno - será reemplazado por documentación actualizada

#### 5. **RESUMEN_SUSTENTACION.md**
   - **Razón:** Resumen del primer parcial, contenido obsoleto
   - **Tipo:** Documentación temporal
   - **Impacto:** Ninguno - información no vigente

#### 6. **dual_simplex_enhanced.py**
   - **Razón:** Versión enhanced no utilizada en app.py, duplicado de dual_simplex_solver.py
   - **Tipo:** Código duplicado
   - **Impacto:** Ninguno - no se importa en la aplicación

#### 7. **simplex_enhanced.py**
   - **Razón:** Versión enhanced no utilizada en app.py, duplicado de simplex_solver.py
   - **Tipo:** Código duplicado
   - **Impacto:** Ninguno - no se importa en la aplicación

#### 8. **simplex_solver_improved.py**
   - **Razón:** Versión mejorada no integrada, genera conflictos de importación
   - **Tipo:** Código experimental/duplicado
   - **Impacto:** Ninguno - causaba errores de importación

#### 9. **metodo_grafico.py**
   - **Razón:** Archivo duplicado, funcionalidad contenida en lp_solver.py
   - **Tipo:** Código duplicado
   - **Impacto:** Ninguno - lp_solver.py ya tiene esta funcionalidad

#### 10. **test_api.py**
   - **Razón:** Archivo de pruebas temporales, no es testing formal
   - **Tipo:** Archivo de prueba temporal
   - **Impacto:** Ninguno - pruebas ad-hoc sin estructura

#### 11. **validate_system.py**
   - **Razón:** Script de validación temporal, no usado en producción
   - **Tipo:** Script de validación temporal
   - **Impacto:** Ninguno - validación ya integrada en los solvers

#### 12. **templates/about_new.html**
   - **Razón:** Template backup duplicado de about.html
   - **Tipo:** Backup/Duplicado
   - **Impacto:** Ninguno - versión de respaldo innecesaria

#### 13. **templates/about_old.html**
   - **Razón:** Template backup antiguo de about.html
   - **Tipo:** Backup/Duplicado
   - **Impacto:** Ninguno - versión antigua innecesaria

#### 14. **__pycache__/** (carpeta completa)
   - **Razón:** Archivos compilados de Python, se regeneran automáticamente
   - **Tipo:** Archivos temporales de compilación
   - **Impacto:** Ninguno - se regenera al ejecutar Python

---

## 📊 Resumen de Limpieza

- **Total archivos eliminados:** 14 archivos + 1 carpeta
- **Espacio liberado:** ~varios MB (incluye pycache)
- **Archivos Python eliminados:** 7 (duplicados y temporales)
- **Documentación eliminada:** 5 (obsoleta del primer parcial)
- **Templates eliminados:** 2 (backups innecesarios)

### ✅ Archivos Mantenidos (Esenciales)

#### Código Python:
- `app.py` - Aplicación Flask principal
- `lp_solver.py` - Método Gráfico
- `simplex_solver.py` - Método Simplex
- `dual_simplex_solver.py` - Método Dual Simplex

#### Templates:
- `base.html` - Template base
- `index.html` - Página principal
- `about.html` - Información
- `examples.html` - Ejemplos
- `results.html` - Resultados método gráfico
- `simplex.html`, `simplex_results.html` - Método Simplex
- `dual_simplex.html`, `dual_simplex_results.html` - Método Dual Simplex
- `404.html` - Página de error

#### Configuración:
- `requirements.txt` - Dependencias
- `.gitignore` - Archivos a ignorar en git
- `README.md` - Documentación principal

---

## 🎯 FASE 2: VISUALIZACIÓN PASO A PASO (En Progreso)

### Método Simplex - Tableau Iterativo
*Documentación pendiente de implementación*

### Método Dual Simplex - Tableau Iterativo
*Documentación pendiente de implementación*

---

## 🎨 FASE 3: MEJORAS DE INTERFAZ (Pendiente)

*Documentación pendiente*

---

## 📝 FASE 4: CONTENIDO Y DOCUMENTACIÓN (Pendiente)

*Documentación pendiente*
