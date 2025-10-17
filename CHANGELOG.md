# CHANGELOG - Optimización del Proyecto de Programación Lineal

**Fecha:** 17 de Octubre, 2025  
**Autor:** José Miguel Herrera Gutiérrez  
**Proyecto:** Investigación de Operaciones - Segundo Parcial UTP

---

## 📋 FASE 1: LIMPIEZA DEL PROYECTO

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
