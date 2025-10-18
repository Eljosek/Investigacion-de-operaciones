# Correcciones al Método Simplex - Resumen Técnico

## Problema Crítico Identificado
**Error:** `can only concatenate str (not "int") to str`

### Causa Raíz
En el archivo `simplex_tableau.py`, líneas 174-175, la función `_pivot_operation()` intentaba concatenar tipos incompatibles al generar strings de operaciones de pivoteo:

```python
# ❌ CÓDIGO PROBLEMÁTICO (antes)
operations.append(f"F{i + 1 if i < self.n_constraints else 'Z'} = ...")
```

Cuando `i >= self.n_constraints`, la expresión ternaria devolvía el string `'Z'`, pero Python intentaba sumarlo con enteros en ciertas condiciones.

### Solución Implementada
Se separó la lógica de nomenclatura en variables explícitas:

```python
# ✅ CÓDIGO CORREGIDO (ahora)
row_name = f"F{i + 1}" if i < self.n_constraints else "FZ"
pivot_row_name = f"F{pivot_row + 1}"

if multiplier > 0:
    operations.append(f"{row_name} = {row_name} - {multiplier:.4g} × {pivot_row_name}")
else:
    operations.append(f"{row_name} = {row_name} + {abs(multiplier):.4g} × {pivot_row_name}")
```

---

## Mejoras en la Visualización de Tablas Iterativas

### 1. Variables Formateadas
**Archivo:** `simplex_tableau.py` - Método `_save_iteration()`

Se agregó formato consistente para nombres de variables:

```python
# Variables entrantes/salientes ahora son strings legibles
entering_var_name = f'x{entering_var+1}' if entering_var < self.n_vars else f'S{entering_var-self.n_vars+1}'
leaving_var_name = f'x{leaving_var+1}' if leaving_var < self.n_vars else f'S{leaving_var-self.n_vars+1}'
```

### 2. Información del Pivote
Se agregó el diccionario `pivot_info` con detalles del elemento pivote:

```python
'pivot_info': {
    'row': pivot_row,
    'col': pivot_col,
    'element': float(self.tableau[pivot_row, pivot_col])
} if pivot_row is not None and pivot_col is not None else None
```

### 3. Actualización del Template HTML
**Archivo:** `templates/simplex_results.html`

#### Cambio 1: Variables Entrante/Saliente
```html
<!-- ❌ ANTES: Usaba índices numéricos -->
<span class="badge bg-success ms-2">x{{ iter.entering_var + 1 }}</span>

<!-- ✅ AHORA: Usa strings formateados directamente -->
<span class="badge bg-success ms-2">{{ iter.entering_var }}</span>
```

#### Cambio 2: Sección de Información del Pivote
Se agregó una nueva sección similar al Dual-Simplex:

```html
{% if iter.pivot_info %}
<div class="alert alert-primary">
    <h6><i class="fas fa-crosshairs"></i> Información del Pivote:</h6>
    <ul class="mb-0">
        <li><strong>Fila:</strong> {{ iter.pivot_info.row + 1 }}</li>
        <li><strong>Columna:</strong> {{ iter.pivot_info.col + 1 }}</li>
        <li><strong>Elemento Pivote:</strong> {{ "%.4g"|format(iter.pivot_info.element) }}</li>
    </ul>
</div>
{% endif %}
```

#### Cambio 3: Variables Básicas Actuales
```html
<!-- ✅ AHORA: Usa nombres formateados del tableau_info -->
{% if iter.tableau_info and iter.tableau_info.basic_vars %}
    {% for var_name in iter.tableau_info.basic_vars %}
        <span class="badge bg-primary me-2 mb-2">{{ var_name }}</span>
    {% endfor %}
{% endif %}
```

---

## Estructura de Datos de Iteración (Actualizada)

Cada iteración ahora contiene:

```python
{
    'iteration': 0,                    # Número de iteración
    'description': 'Tableau Inicial',  # Descripción del paso
    'tableau': np.array(...),          # Matriz del tableau
    'basic_vars': [2, 3],              # Índices de variables básicas
    'pivot_col': None,                 # Columna pivote (o None)
    'pivot_row': None,                 # Fila pivote (o None)
    'entering_var': 'x1',              # ✅ STRING formateado
    'leaving_var': 'S2',               # ✅ STRING formateado
    'operation': 'F2 = F2 / 2 | ...',  # Operaciones realizadas
    'objective_value': -0.0,           # Valor de Z (ajustado por max/min)
    'is_optimal': False,               # ¿Es solución óptima?
    'z_value': 0.0,                    # Valor directo de la fila Z
    'tableau_info': {                  # Información estructural
        'n_rows': 2,
        'n_cols': 4,
        'basic_vars': ['S1', 'S2']     # ✅ STRINGS formateados
    },
    'pivot_info': {                    # ✅ NUEVO
        'row': 1,
        'col': 0,
        'element': 2.0
    }
}
```

---

## Pruebas Realizadas

### Test 1: Maximización con restricciones ≤
```python
Problema: max z = 3x1 + 2x2
Restricciones:
  - x1 + x2 ≤ 6
  - 2x1 + x2 ≤ 8

Resultado: ✅ CORRECTO
  - Success: True
  - Iterations: 3
  - Z: 14.0
  - Solution: x1 = 2.0, x2 = 4.0
```

### Test 2: Maximización simple
```python
Problema: max z = 3x1 + 2x2
Restricciones:
  - x1 + x2 ≤ 4
  - 2x1 + x2 ≤ 5

Resultado: ✅ CORRECTO
  - Z: 9.0
  - Solution: x1 = 1.0, x2 = 3.0
  - Iteraciones: 2
```

---

## Limitaciones Conocidas

### Restricciones ≥ con Simplex Estándar
El método Simplex estándar implementado **no maneja correctamente problemas con restricciones ≥** porque requiere:

1. Variables de exceso
2. Variables artificiales
3. Método de penalización (Big M) o Dos Fases

**Recomendación:** Para problemas con restricciones ≥, usar el **Método Dual-Simplex** que está correctamente implementado.

---

## Consistencia con Dual-Simplex

Ahora ambos métodos tienen estructura similar:

| Característica | Simplex | Dual-Simplex | Estado |
|---|---|---|---|
| Variables formateadas (x1, S1) | ✅ | ✅ | Consistente |
| Información del pivote | ✅ | ✅ | Consistente |
| Descripción de operaciones | ✅ | ✅ | Consistente |
| Valor objetivo (Z) | ✅ | ✅ | Consistente |
| Bandera is_optimal | ✅ | ✅ | Consistente |
| tableau_info con basic_vars | ✅ | ✅ | Consistente |

---

## Archivos Modificados

### Commit: `450094c`
```
- simplex_tableau.py (18 líneas modificadas)
- templates/simplex_results.html (33 inserciones, 15 eliminaciones)
```

**Mensaje del commit:**
```
fix: Corregir error de concatenación string en Simplex y mejorar visualización de tablas iterativas

- Solucionado error 'can only concatenate str (not int) to str' en _pivot_operation
- Mejorado template simplex_results.html para mostrar variables formateadas (x1, S1)
- Agregada sección de información del pivote similar al Dual-Simplex
- Variables entrante/saliente ahora se muestran correctamente
- Variables básicas actuales usan nombres formateados del tableau_info
- Interfaz ahora es consistente entre Simplex y Dual-Simplex
```

---

## Interfaz Visual Mejorada

### Elementos Visuales Agregados

1. **Badge de Variables Entrante/Saliente**
   - Color verde para entrante
   - Color amarillo para saliente
   - Nombres formateados (x1, x2, S1, S2)

2. **Caja de Información del Pivote**
   - Fondo azul (alert-primary)
   - Muestra fila, columna y elemento pivote
   - Solo aparece cuando hay pivoteo

3. **Variables Básicas Actuales**
   - Badges azules para variables originales
   - Badges secundarios para variables de holgura
   - Nombres legibles y consistentes

---

## Cómo Usar

### En el Navegador
1. Abrir http://localhost:5000
2. Navegar a "Método Simplex"
3. Ingresar función objetivo y restricciones
4. Ver resultados con **tablas iterativas completas**

### Ejemplo de Entrada Válido
```
Función Objetivo: max z = 3x1 + 2x2

Restricciones:
x1 + x2 <= 6
2x1 + x2 <= 8
x1 >= 0
x2 >= 0
```

### Salida Esperada
- ✅ Solución óptima con Z correcto
- ✅ Valores de variables x1, x2
- ✅ Tablas iterativas con acordeón expandible
- ✅ Información del pivote en cada iteración
- ✅ Variables entrante/saliente claramente identificadas

---

## Fecha de Corrección
**18 de Octubre de 2025**

**Desarrollado por:** José Miguel Herrera Gutiérrez  
**Curso:** Investigación de Operaciones - Segundo Parcial  
**Profesora:** Bibiana Patricia Arias Villada  
**Universidad:** UTP
