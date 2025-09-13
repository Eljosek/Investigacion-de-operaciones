# archivo: lp_solver.py
"""
Módulo para resolver problemas de programación lineal con el método gráfico.
Contiene las funciones necesarias para parsear, calcular y graficar problemas de LP.
"""

import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import base64
from io import BytesIO

# Configurar matplotlib para no mostrar ventanas (modo backend)
matplotlib.use('Agg')

def parse_objective(s):
    """
    Parsea la función objetivo desde texto.
    
    Ejemplos de entrada:
      "maximizar z = 1x + 3y"
      "min z = x - 2y"
      
    Returns:
        tuple: (tipo_optimización, [coeficiente_x, coeficiente_y])
        tipo_optimización: 'max' o 'min'
    """
    s_low = s.lower()
    if 'max' in s_low:
        opt_type = 'max'
    elif 'min' in s_low:
        opt_type = 'min'
    else:
        raise ValueError("No se encontró 'max' o 'min' en la función objetivo.")
    
    # Extraer la parte después del signo =
    if '=' in s:
        rhs = s.split('=')[1]
    else:
        rhs = s
    
    def get_coeff(var, text):
        """Extrae el coeficiente de una variable del texto"""
        t = text.replace(' ', '')
        m = re.search(r'([+-]?\d*\.?\d*)' + var, t)
        if not m:
            return 0.0
        num = m.group(1)
        if num in ['', '+', None]:
            return 1.0
        if num == '-':
            return -1.0
        return float(num)
    
    # Obtener coeficientes de x e y
    a = get_coeff('x', rhs)
    b = get_coeff('y', rhs)
    
    return opt_type, [a, b]

def parse_constraint(s):
    """
    Parsea una restricción individual desde texto.
    
    Ejemplos de entrada:
      "1x + 3y <= 26"
      "3x+4y>=12"
      "x + y = 10"
      "x ≥ 0"  (símbolos matemáticos)
      "y ≤ 5"
      
    Returns:
        tuple: (coef_x, coef_y, operador, valor_derecho)
    """
    s = s.strip()
    
    # Reemplazar símbolos matemáticos por equivalentes ASCII
    s = s.replace('≤', '<=').replace('≥', '>=').replace('≠', '!=')
    
    # Buscar el operador de comparación (después de normalizar símbolos)
    m = re.search(r'(<=|>=|=)', s)
    if not m:
        raise ValueError(f"No se encontró operador en la restricción: {s}")
    
    op = m.group(1)
    
    parts = re.split(r'(<=|>=|=)', s)
    lhs = parts[0]  # lado izquierdo
    rhs = parts[-1]  # lado derecho
    rhs_val = float(rhs)
    
    def get_coeff(var, text):
        """Extrae el coeficiente de una variable del texto"""
        t = text.replace(' ', '').lower()  # Normalizar texto
        
        # Buscar patrones como: x, 1x, -x, 2x, 3.5x, +x, etc.
        patterns = [
            r'([+-]?\d*\.?\d*)' + var + r'(?!\w)',  # Patrón general
            r'^' + var + r'(?!\w)',  # Variable sola al inicio
            r'([+-])' + var + r'(?!\w)'  # Variable con signo
        ]
        
        for pattern in patterns:
            mm = re.search(pattern, t)
            if mm:
                if len(mm.groups()) == 0:  # Variable sola
                    return 1.0
                
                num = mm.group(1)
                if num in ['', '+', None]:
                    return 1.0
                if num == '-':
                    return -1.0
                try:
                    return float(num)
                except (ValueError, TypeError):
                    continue
        
        return 0.0  # Variable no encontrada
    
    # Obtener coeficientes de x e y
    a = get_coeff('x', lhs)
    b = get_coeff('y', lhs)
    
    return a, b, op, rhs_val

def compute_vertices(constraints):
    """
    Calcula los vértices de la región factible.
    
    Args:
        constraints: lista de diccionarios con claves 'a','b','op','rhs'
        
    Returns:
        list: lista de tuplas (x, y) representando los vértices factibles
    """
    lines = []  # líneas para intersecciones
    ineqs = []  # desigualdades para verificar factibilidad
    
    # Verificar si el usuario ya especificó restricciones de no-negatividad
    has_x_nonneg = False
    has_y_nonneg = False
    
    # Procesar cada restricción
    for c in constraints:
        a, b, op, rhs = c['a'], c['b'], c['op'], c['rhs']
        lines.append((a, b, rhs))  # línea para intersección
        
        # Verificar si son restricciones de no-negatividad explícitas
        if abs(a - 1) < 1e-9 and abs(b) < 1e-9 and abs(rhs) < 1e-9 and op == '>=':
            has_x_nonneg = True
        if abs(b - 1) < 1e-9 and abs(a) < 1e-9 and abs(rhs) < 1e-9 and op == '>=':
            has_y_nonneg = True
        
        # Convertir a desigualdad estándar (ax + by <= rhs)
        if op == '<=':
            ineqs.append((a, b, rhs))
        elif op == '>=':
            ineqs.append((-a, -b, -rhs))  # convertir >= a <=
        else:  # op == '='
            # Igualdad se convierte en dos desigualdades
            ineqs.append((a, b, rhs))
            ineqs.append((-a, -b, -rhs))
    
    # Agregar líneas de los ejes para intersecciones (siempre necesarias)
    lines.append((1, 0, 0))  # x = 0
    lines.append((0, 1, 0))  # y = 0
    
    # Solo agregar restricciones de no-negatividad si el usuario no las especificó
    if not has_x_nonneg:
        ineqs.append((-1, 0, 0))  # -x <= 0 => x >= 0
    if not has_y_nonneg:
        ineqs.append((0, -1, 0))  # -y <= 0 => y >= 0

    vertices = []
    n = len(lines)
    
    # Encontrar intersecciones de cada par de líneas
    for i in range(n):
        a1, b1, r1 = lines[i]
        for j in range(i+1, n):
            a2, b2, r2 = lines[j]
            
            # Resolver sistema de ecuaciones lineales
            A = np.array([[a1, b1], [a2, b2]], dtype=float)
            det = np.linalg.det(A)
            
            # Saltar si las líneas son paralelas
            if abs(det) < 1e-9:
                continue
                
            rhs = np.array([r1, r2], dtype=float)
            sol = np.linalg.solve(A, rhs)
            x, y = sol[0], sol[1]
            
            # Verificar que la solución sea válida
            if not np.isfinite(x) or not np.isfinite(y):
                continue
            
            # Verificar que el punto satisfaga todas las restricciones
            feasible = True
            for ai, bi, ri in ineqs:
                if ai * x + bi * y > ri + 1e-7:  # tolerancia numérica
                    feasible = False
                    break
            
            # Agregar vértice si es factible y único
            if feasible:
                rx = round(float(x), 9)
                ry = round(float(y), 9)
                if (rx, ry) not in vertices:
                    vertices.append((rx, ry))
    
    return vertices

def create_plot(constraints, vertices, obj_coeffs, opt_type, x_max=20, y_max=20):
    """
    Crea la gráfica del problema de programación lineal con mejor visualización.
    
    Args:
        constraints: lista de restricciones
        vertices: vértices de la región factible
        obj_coeffs: coeficientes de la función objetivo
        opt_type: 'max' o 'min'
        x_max, y_max: límites de la gráfica
        
    Returns:
        tuple: (resultados, punto_óptimo, valor_óptimo, imagen_base64)
    """
    # Configurar la figura con mejor resolución
    plt.figure(figsize=(12, 9))
    plt.style.use('default')  # Estilo limpio
    
    # Colores para las restricciones
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
    
    # Dominio extendido para líneas
    x_extended = np.linspace(-2, x_max + 2, 1000)
    
    # Graficar cada restricción
    for i, c in enumerate(constraints):
        a, b, op, rhs = c['a'], c['b'], c['op'], c['rhs']
        color = colors[i % len(colors)]
        
        # Formatear etiqueta de restricción más clara
        if abs(a) < 1e-9 and abs(b) < 1e-9:
            continue  # Restricción inválida
        
        # Crear etiqueta limpia
        label_parts = []
        if abs(a) > 1e-9:
            if abs(a - 1) < 1e-9:
                label_parts.append("x")
            elif abs(a + 1) < 1e-9:
                label_parts.append("-x")
            else:
                label_parts.append(f"{a:.1f}x")
        
        if abs(b) > 1e-9:
            if label_parts:  # Ya hay términos
                if b > 0:
                    if abs(b - 1) < 1e-9:
                        label_parts.append(" + y")
                    else:
                        label_parts.append(f" + {b:.1f}y")
                else:
                    if abs(b + 1) < 1e-9:
                        label_parts.append(" - y")
                    else:
                        label_parts.append(f" - {abs(b):.1f}y")
            else:
                if abs(b - 1) < 1e-9:
                    label_parts.append("y")
                elif abs(b + 1) < 1e-9:
                    label_parts.append("-y")
                else:
                    label_parts.append(f"{b:.1f}y")
        
        constraint_label = f"{''.join(label_parts)} {op} {rhs}"
        
        # Graficar línea de restricción
        if abs(b) < 1e-9:  # Línea vertical
            if abs(a) > 1e-9:
                xv = rhs / a
                if 0 <= xv <= x_max:
                    plt.axvline(x=xv, color=color, linestyle='--', alpha=0.8, linewidth=2,
                              label=constraint_label)
        elif abs(a) < 1e-9:  # Línea horizontal
            if abs(b) > 1e-9:
                yv = rhs / b
                if 0 <= yv <= y_max:
                    plt.axhline(y=yv, color=color, linestyle='--', alpha=0.8, linewidth=2,
                              label=constraint_label)
        else:  # Línea general: ax + by = rhs
            y_vals = (rhs - a * x_extended) / b
            # Solo mostrar la parte visible
            mask = (y_vals >= -2) & (y_vals <= y_max + 2)
            plt.plot(x_extended[mask], y_vals[mask], color=color, linestyle='--', 
                    alpha=0.8, linewidth=2, label=constraint_label)
    
    # Crear malla más fina para mejor sombreado
    xx = np.linspace(0, x_max, 800)
    yy = np.linspace(0, y_max, 800)
    X, Y = np.meshgrid(xx, yy)
    feasible = np.ones_like(X, dtype=bool)
    
    # Aplicar cada restricción a la malla
    for c in constraints:
        a, b, op, rhs = c['a'], c['b'], c['op'], c['rhs']
        constraint_values = a * X + b * Y
        
        if op == '<=':
            feasible &= (constraint_values <= rhs + 1e-9)
        elif op == '>=':
            feasible &= (constraint_values >= rhs - 1e-9)
        else:  # op == '='
            # Para igualdades, crear una banda estrecha
            feasible &= (np.abs(constraint_values - rhs) <= 0.1)
    
    # Verificar si el usuario especificó restricciones de no-negatividad explícitamente
    has_x_nonneg = any(abs(c['a'] - 1) < 1e-9 and abs(c['b']) < 1e-9 and 
                       abs(c['rhs']) < 1e-9 and c['op'] == '>=' for c in constraints)
    has_y_nonneg = any(abs(c['b'] - 1) < 1e-9 and abs(c['a']) < 1e-9 and 
                       abs(c['rhs']) < 1e-9 and c['op'] == '>=' for c in constraints)
    
    # Solo aplicar restricciones de no-negatividad si el usuario no las especificó
    if not has_x_nonneg:
        feasible &= (X >= -1e-9)
    if not has_y_nonneg:
        feasible &= (Y >= -1e-9)
    
    # Sombrear región factible con mejor visualización
    plt.contourf(X, Y, feasible.astype(int), levels=[0.5, 1.5], 
                colors=['lightgreen'], alpha=0.4)
    plt.contour(X, Y, feasible.astype(int), levels=[0.5], 
               colors=['darkgreen'], linewidths=2, alpha=0.7)

    # Marcar vértices con mejor visualización
    if vertices:
        vx = [v[0] for v in vertices]
        vy = [v[1] for v in vertices]
        plt.scatter(vx, vy, c='darkred', s=120, zorder=10, 
                   label='Vértices', edgecolors='white', linewidth=2)
        
        # Anotar coordenadas de vértices con mejor formato
        for i, (x_v, y_v) in enumerate(vertices):
            plt.annotate(f'V{i+1}: ({x_v:.2f}, {y_v:.2f})', 
                        (x_v, y_v), xytext=(10, 10), 
                        textcoords='offset points', fontsize=10,
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8),
                        ha='left')

    # Calcular función objetivo en cada vértice
    a_obj, b_obj = obj_coeffs
    best_val = None
    best_pt = None
    results = []
    
    for (xv, yv) in vertices:
        val = a_obj * xv + b_obj * yv
        results.append(((xv, yv), val))
        
        if best_val is None:
            best_val = val
            best_pt = (xv, yv)
        else:
            if opt_type == 'max' and val > best_val:
                best_val = val
                best_pt = (xv, yv)
            elif opt_type == 'min' and val < best_val:
                best_val = val
                best_pt = (xv, yv)

    # Resaltar punto óptimo con mejor visualización
    if best_pt is not None:
        plt.scatter(best_pt[0], best_pt[1], c='gold', s=300, zorder=15,
                   marker='*', edgecolors='darkred', linewidth=3,
                   label=f'★ Óptimo: ({best_pt[0]:.2f}, {best_pt[1]:.2f})')
        
        # Agregar línea de función objetivo en el punto óptimo
        if abs(b_obj) > 1e-9:  # Evitar división por cero
            x_obj = np.linspace(0, x_max, 100)
            y_obj = (best_val - a_obj * x_obj) / b_obj
            mask = (y_obj >= 0) & (y_obj <= y_max)
            plt.plot(x_obj[mask], y_obj[mask], 'k-', alpha=0.5, linewidth=2,
                    label=f'z = {best_val:.2f}')
    
    # Configurar gráfica con mejor formato
    plt.xlim(-0.5, x_max)
    plt.ylim(-0.5, y_max)
    plt.xlabel('x', fontsize=14, fontweight='bold')
    plt.ylabel('y', fontsize=14, fontweight='bold')
    
    # Título más informativo
    obj_str = f"z = {obj_coeffs[0]:.1f}x"
    if obj_coeffs[1] >= 0:
        obj_str += f" + {obj_coeffs[1]:.1f}y"
    else:
        obj_str += f" - {abs(obj_coeffs[1]):.1f}y"
        
    plt.title(f'Método Gráfico - Programación Lineal\n'
              f'{"Maximizar" if opt_type == "max" else "Minimizar"}: {obj_str}', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Mejorar leyenda y grid
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=10)
    plt.grid(True, alpha=0.4, linestyle='-', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Convertir gráfica a imagen base64 para mostrar en web
    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()  # Cerrar figura para liberar memoria
    
    # Codificar imagen en base64
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    
    return results, best_pt, best_val, graphic

def solve_lp_problem(objective_str, constraints_list):
    """
    Función principal para resolver un problema de programación lineal.
    
    Args:
        objective_str: string con la función objetivo
        constraints_list: lista de strings con las restricciones
        
    Returns:
        dict: diccionario con los resultados del problema
    """
    try:
        # Parsear función objetivo
        opt_type, obj_coeffs = parse_objective(objective_str)
        
        # Parsear restricciones
        constraints = []
        for constraint_str in constraints_list:
            constraint_str = constraint_str.strip()
            if constraint_str:  # ignorar líneas vacías
                a, b, op, rhs = parse_constraint(constraint_str)
                constraints.append({'a': a, 'b': b, 'op': op, 'rhs': rhs})
        
        # Calcular vértices
        vertices = compute_vertices(constraints)
        
        if not vertices:
            return {
                'success': False,
                'error': 'No se encontró región factible. Verifica las restricciones.'
            }
        
        # Crear gráfica y calcular resultados
        results, best_pt, best_val, graphic = create_plot(
            constraints, vertices, obj_coeffs, opt_type
        )
        
        return {
            'success': True,
            'opt_type': opt_type,
            'obj_coeffs': obj_coeffs,
            'vertices': vertices,
            'results': results,
            'best_point': best_pt,
            'best_value': best_val,
            'graphic': graphic,
            'constraints': constraints
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f'Error al procesar el problema: {str(e)}'
        }