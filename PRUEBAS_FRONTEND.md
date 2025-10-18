# 🧪 Guía de Pruebas Exhaustivas - Frontend

## Servidor
- ✅ URL: http://localhost:5000
- ✅ Estado: Ejecutándose

## 📋 CASOS DE PRUEBA NAVEGADOR

### TEST 1: Simplex Estándar (MAX con <=)
**Navegar a:** http://localhost:5000/simplex

**Datos de entrada:**
```
Función objetivo: max z = 3x1 + 2x2
Restricciones:
x1 + x2 <= 6
2x1 + x2 <= 8
```

**Resultado esperado:**
- ✅ Success
- ✅ Z óptimo: 14.0
- ✅ x1 = 2.0, x2 = 4.0
- ✅ 3 iteraciones mostradas
- ✅ Tableaus visibles en acordeón

---

### TEST 2: Simplex Dos Fases (MIN con >=)
**Navegar a:** http://localhost:5000/simplex

**Datos de entrada:**
```
Función objetivo: min z = 10x1 + 30x2
Restricciones:
x1 + 5x2 >= 15
5x1 + x2 >= 15
```

**Resultado esperado:**
- ✅ Success
- ✅ Z óptimo: 100.0
- ✅ x1 = 2.5, x2 = 2.5
- ✅ 4 iteraciones (3 Fase I + 1 Fase II)
- ✅ Transición visible entre fases
- ✅ Variables artificiales eliminadas

---

### TEST 3: Simplex con Restricción = (Dos Fases)
**Navegar a:** http://localhost:5000/simplex

**Datos de entrada:**
```
Función objetivo: max z = 2x1 + 3x2
Restricciones:
x1 + x2 = 4
x1 <= 3
x2 <= 3
```

**Resultado esperado:**
- ✅ Success
- ✅ Solución óptima encontrada
- ✅ Dos fases ejecutadas

---

### TEST 4: Dual-Simplex MIN
**Navegar a:** http://localhost:5000/dual-simplex

**Datos de entrada:**
```
Función objetivo: min z = 3x1 + 2x2
Restricciones:
3x1 + x2 >= 3
4x1 + 3x2 >= 6
x1 + x2 <= 3
```

**Resultado esperado:**
- ✅ Success
- ✅ Z óptimo: 4.2
- ✅ x1 = 0.6, x2 = 1.2
- ✅ 3 iteraciones
- ✅ Factibilidad dual: Verificada
- ✅ Estado final: Óptimo

---

### TEST 5: Dual-Simplex MAX
**Navegar a:** http://localhost:5000/dual-simplex

**Datos de entrada:**
```
Función objetivo: max z = 5x1 + 4x2
Restricciones:
x1 + 2x2 >= 6
3x1 + x2 >= 9
```

**Resultado esperado:**
- ✅ Success
- ✅ Z óptimo: 19.2
- ✅ x1 = 2.4, x2 = 1.8
- ✅ 3 iteraciones
- ✅ Factibilidad dual: Verificada

---

### TEST 6: Caso Unbounded (Simplex)
**Navegar a:** http://localhost:5000/simplex

**Datos de entrada:**
```
Función objetivo: max z = 3x1 + 2x2
Restricciones:
x1 + x2 >= 4
```

**Resultado esperado:**
- ❌ Failure
- ❌ Mensaje: "Problema no acotado"
- ✅ Sin crash del sistema

---

### TEST 7: Caso Infactible (Dual-Simplex)
**Navegar a:** http://localhost:5000/dual-simplex

**Datos de entrada:**
```
Función objetivo: min z = x1 + x2
Restricciones:
x1 + x2 >= 10
x1 + x2 <= 5
```

**Resultado esperado:**
- ❌ Failure
- ❌ Mensaje: "No factible" o "Infeasible"
- ✅ Sin crash del sistema

---

## ✅ CHECKLIST DE VALIDACIÓN

### Funcionalidad
- [ ] Simplex acepta <= correctamente
- [ ] Simplex con Dos Fases maneja >= y =
- [ ] Dual-Simplex MIN funciona
- [ ] Dual-Simplex MAX funciona
- [ ] Casos unbounded detectados
- [ ] Casos infactibles detectados

### Visualización
- [ ] Iteraciones se muestran en acordeón
- [ ] Tableaus se renderizan correctamente
- [ ] Variables entrantes/salientes visibles
- [ ] Valores objetivo mostrados en cada iteración
- [ ] Información de pivoteo visible

### UX
- [ ] Mensajes de error claros
- [ ] Navegación fluida entre métodos
- [ ] Formularios se limpian apropiadamente
- [ ] Sin errores en consola del navegador

---

## 🎯 Resultado Final Esperado
- **7/7 casos funcionando correctamente**
- **0 errores en consola**
- **UX fluida y clara**
