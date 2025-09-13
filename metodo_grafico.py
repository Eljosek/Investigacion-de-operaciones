# archivo: metodo_grafico_io.py
import re
import numpy as np
import matplotlib.pyplot as plt

def parse_objective(s):
    """
    Parse objective like:
      "maximizar z = 1x + 3y"
      "min z = x - 2y"
    Returns ('max' or 'min', [coef_x, coef_y])
    """
    s_low = s.lower()
    if 'max' in s_low:
        opt_type = 'max'
    elif 'min' in s_low:
        opt_type = 'min'
    else:
        raise ValueError("No se encontró 'max' o 'min' en la función objetivo.")
    if '=' in s:
        rhs = s.split('=')[1]
    else:
        rhs = s
    def get_coeff(var, text):
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
    a = get_coeff('x', rhs)
    b = get_coeff('y', rhs)
    return opt_type, [a, b]

def parse_constraint(s):
    """
    Parse a single constraint like "1x + 3y <= 26" or "3x+4y>=12"
    Returns a tuple (a, b, op, rhs)
    """
    s = s.strip()
    m = re.search(r'(<=|>=|=)', s)
    if not m:
        raise ValueError(f"No se encontró operador en la restricción: {s}")
    op = m.group(1)
    parts = re.split(r'(<=|>=|=)', s)
    lhs = parts[0]
    rhs = parts[-1]
    rhs_val = float(rhs)
    def get_coeff(var, text):
        t = text.replace(' ', '')
        mm = re.search(r'([+-]?\d*\.?\d*)' + var, t)
        if not mm:
            return 0.0
        num = mm.group(1)
        if num in ['', '+', None]:
            return 1.0
        if num == '-':
            return -1.0
        return float(num)
    a = get_coeff('x', lhs)
    b = get_coeff('y', lhs)
    return a, b, op, rhs_val

def compute_vertices(constraints):
    """
    constraints: list of dicts {'a':a,'b':b,'op':op,'rhs':rhs}
    Returns list of feasible vertices (x,y)
    """
    lines = []
    ineqs = []
    for c in constraints:
        a, b, op, rhs = c['a'], c['b'], c['op'], c['rhs']
        lines.append((a, b, rhs))
        if op == '<=':
            ineqs.append((a, b, rhs))
        elif op == '>=':
            ineqs.append((-a, -b, -rhs))
        else: # '='
            ineqs.append((a, b, rhs))
            ineqs.append((-a, -b, -rhs))
    # axis lines for x=0, y=0 (equalities for intersections)
    lines.append((1, 0, 0))
    lines.append((0, 1, 0))
    # non-negativity as inequalities (-x <= 0, -y <= 0)
    ineqs.append((-1, 0, 0))
    ineqs.append((0, -1, 0))

    vertices = []
    n = len(lines)
    for i in range(n):
        a1, b1, r1 = lines[i]
        for j in range(i+1, n):
            a2, b2, r2 = lines[j]
            A = np.array([[a1, b1],[a2, b2]], dtype=float)
            det = np.linalg.det(A)
            if abs(det) < 1e-9:
                continue
            rhs = np.array([r1, r2], dtype=float)
            sol = np.linalg.solve(A, rhs)
            x, y = sol[0], sol[1]
            if not np.isfinite(x) or not np.isfinite(y):
                continue
            feasible = True
            for ai, bi, ri in ineqs:
                if ai * x + bi * y > ri + 1e-7:
                    feasible = False
                    break
            if feasible:
                rx = round(float(x), 9)
                ry = round(float(y), 9)
                if (rx, ry) not in vertices:
                    vertices.append((rx, ry))
    return vertices

def plot_problem(constraints, vertices, obj_coeffs, opt_type, x_max=20, y_max=20):
    x = np.linspace(0, x_max, 400)
    plt.figure(figsize=(8,6))
    for c in constraints:
        a, b, op, rhs = c['a'], c['b'], c['op'], c['rhs']
        if abs(b) < 1e-9:
            if abs(a) < 1e-9:
                continue
            xv = rhs / a
            plt.axvline(x=xv, label=f"{a}x + {b}y {op} {rhs}")
        else:
            y_vals = (rhs - a * x) / b
            plt.plot(x, y_vals, label=f"{a}x + {b}y {op} {rhs}")
    # shade feasible region
    xx = np.linspace(0, x_max, 400)
    yy = np.linspace(0, y_max, 400)
    X, Y = np.meshgrid(xx, yy)
    feasible = np.ones_like(X, dtype=bool)
    for a,b,op,rhs in [(c['a'],c['b'],c['op'],c['rhs']) for c in constraints]:
        if op == '<=':
            feasible &= (a*X + b*Y <= rhs + 1e-7)
        elif op == '>=':
            feasible &= (a*X + b*Y >= rhs - 1e-7)
        else:
            feasible &= (np.isclose(a*X + b*Y, rhs, atol=1e-6))
    plt.imshow(feasible[::-1,:].astype(int), extent=(xx.min(), xx.max(), yy.min(), yy.max()), alpha=0.2, origin='lower', cmap='Greens')

    if vertices:
        vx = [v[0] for v in vertices]
        vy = [v[1] for v in vertices]
        plt.scatter(vx, vy, c='k')
        centroid = (np.mean(vx), np.mean(vy))
        angles = np.arctan2(np.array(vy)-centroid[1], np.array(vx)-centroid[0])
        order = np.argsort(angles)
        poly_x = np.array(vx)[order]
        poly_y = np.array(vy)[order]
        plt.fill(poly_x, poly_y, alpha=0.2)

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
            if opt_type == 'min' and val < best_val:
                best_val = val
                best_pt = (xv, yv)

    if best_pt is not None:
        plt.plot(best_pt[0], best_pt[1], 'ro', markersize=10, label='Punto óptimo')
    plt.xlim(0, x_max)
    plt.ylim(0, y_max)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método gráfico - región factible y punto óptimo')
    plt.legend()
    plt.grid(True)
    plt.show()
    return results, best_pt, best_val

def main():
    print("Ejemplo objetivo: 'maximizar z = 1x + 1y' o 'min z = x - 2y'")
    obj = input("Ingrese la función objetivo: ")
    opt_type, obj_coeffs = parse_objective(obj)
    print("Ingrese restricciones una por línea (ej: '1x + 3y <= 26'). Escriba 'fin' para terminar.")
    cons = []
    while True:
        s = input("Restricción (o 'fin'): ")
        if s.strip().lower() == 'fin':
            break
        a,b,op,rhs = parse_constraint(s)
        cons.append({'a':a,'b':b,'op':op,'rhs':rhs})
    vertices = compute_vertices(cons)
    if not vertices:
        print("No hay región factible (o no se encontraron vértices). Revisa las restricciones.")
        return
    results, best_pt, best_val = plot_problem(cons, vertices, obj_coeffs, opt_type, x_max=20, y_max=20)
    print("Vértices y valor de la función objetivo en cada uno:")
    for (pt, val) in results:
        print(f"({pt[0]:.4f}, {pt[1]:.4f}) -> z = {val:.4f}")
    if best_pt is not None:
        print(f"Punto óptimo: ({best_pt[0]:.4f}, {best_pt[1]:.4f}) con valor z = {best_val:.4f}")

if __name__ == '__main__':
    main()
