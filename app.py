# archivo: app.py
"""
Aplicación web Flask para resolver problemas de programación lineal 
usando el método gráfico.

Autor: Para curso de Investigación de Operaciones
Fecha: 2025
"""

import os
from flask import Flask, render_template, request, flash, redirect, url_for
from lp_solver import solve_lp_problem

# Crear instancia de la aplicación Flask
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'utp-investigacion-operaciones-jose-herrera-2025')

@app.route('/')
def index():
    """
    Página principal con el formulario para ingresar el problema de LP.
    """
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    """
    Procesa el formulario y resuelve el problema de programación lineal.
    """
    # Obtener datos del formulario
    objective = request.form.get('objective', '').strip()
    constraints_text = request.form.get('constraints', '').strip()
    
    # Validar que se ingresaron datos
    if not objective:
        flash('Por favor ingresa una función objetivo.', 'error')
        return redirect(url_for('index'))
    
    if not constraints_text:
        flash('Por favor ingresa al menos una restricción.', 'error')
        return redirect(url_for('index'))
    
    # Procesar restricciones (una por línea)
    constraints_list = [line.strip() for line in constraints_text.split('\n') 
                       if line.strip()]
    
    if not constraints_list:
        flash('Por favor ingresa al menos una restricción válida.', 'error')
        return redirect(url_for('index'))
    
    # Resolver el problema
    try:
        result = solve_lp_problem(objective, constraints_list)
        
        if not result['success']:
            flash(result['error'], 'error')
            return redirect(url_for('index'))
        
        # Preparar datos para mostrar en la página de resultados
        context = {
            'objective': objective,
            'constraints': constraints_list,
            'opt_type': result['opt_type'],
            'obj_coeffs': result['obj_coeffs'],
            'vertices': result['vertices'],
            'results': result['results'],
            'best_point': result['best_point'],
            'best_value': result['best_value'],
            'graphic': result['graphic']
        }
        
        return render_template('results.html', **context)
        
    except Exception as e:
        flash(f'Error inesperado: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/about')
def about():
    """
    Página con información sobre el método gráfico.
    """
    return render_template('about.html')

@app.route('/examples')
def examples():
    """
    Página con ejemplos de problemas de programación lineal.
    """
    examples_data = [
        {
            'title': 'Problema de Maximización Básico',
            'objective': 'maximizar z = 3x + 2y',
            'constraints': 'x + 2y <= 8\n2x + y <= 10\nx >= 0\ny >= 0',
            'description': 'Un problema clásico de maximización con dos restricciones.'
        },
        {
            'title': 'Problema de Minimización',
            'objective': 'minimizar z = 2x + 3y',
            'constraints': 'x + y >= 4\n2x + y >= 6\nx >= 0\ny >= 0',
            'description': 'Problema de minimización con restricciones de tipo mayor o igual.'
        },
        {
            'title': 'Problema Mixto',
            'objective': 'maximizar z = x + 4y',
            'constraints': 'x + 2y <= 12\n2x + y <= 16\nx + y >= 5\nx >= 0\ny >= 0',
            'description': 'Problema con restricciones mixtas (menor y mayor que).'
        }
    ]
    
    return render_template('examples.html', examples=examples_data)

# Manejo de errores
@app.errorhandler(404)
def page_not_found(e):
    """Página de error 404."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Página de error 500."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Configuración para desarrollo y producción
    import os
    
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    print("🚀 Iniciando aplicación de Programación Lineal...")
    print("📊 Método Gráfico - Investigación de Operaciones")
    print("👨‍💻 Desarrollado por José Herrera para UTP")
    print("👩‍🏫 Profesora: Bibiana Patricia Arias Villada")
    
    if debug:
        print("🌐 Abre tu navegador en: http://localhost:5000")
    else:
        print(f"🌐 Servidor ejecutándose en puerto: {port}")
    
    print("-" * 50)
    
    app.run(debug=debug, host='0.0.0.0', port=port)