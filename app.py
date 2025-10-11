# archivo: app.py
"""
Aplicación web Flask para resolver problemas de programación lineal 
usando el método gráfico.

Autor: Para curso de Investigación de Operaciones
Fecha: 2025
"""

import os
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from lp_solver import solve_lp_problem
from simplex_solver import solve_simplex
from dual_simplex_solver import solve_dual_simplex

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

@app.route('/simplex')
def simplex():
    """
    Página para resolver problemas usando el método Simplex.
    """
    return render_template('simplex.html')

@app.route('/solve-simplex', methods=['POST'])
def solve_simplex():
    """
    Procesa el formulario y resuelve el problema usando método Simplex.
    """
    try:
        objective = request.form.get('objective', '').strip()
        constraints_text = request.form.get('constraints', '').strip()
        
        if not objective or not constraints_text:
            flash('Por favor completa todos los campos.', 'error')
            return redirect(url_for('simplex'))
        
        constraints_list = [line.strip() for line in constraints_text.split('\n') 
                           if line.strip()]
        
        result = solve_simplex(objective, constraints_list)
        
        if not result['success']:
            flash(result['error'], 'error')
            return redirect(url_for('simplex'))
        
        return render_template('simplex_results.html', 
                             objective=objective,
                             constraints=constraints_list,
                             result=result)
        
    except Exception as e:
        flash(f'Error inesperado: {str(e)}', 'error')
        return redirect(url_for('simplex'))

@app.route('/dual-simplex')
def dual_simplex():
    """
    Página para resolver problemas usando el método Dual Simplex.
    """
    return render_template('dual_simplex.html')

@app.route('/solve-dual-simplex', methods=['POST'])
def solve_dual_simplex_route():
    """
    Procesa el formulario y resuelve el problema usando método Dual Simplex.
    """
    try:
        objective = request.form.get('objective', '').strip()
        constraints_text = request.form.get('constraints', '').strip()
        
        if not objective or not constraints_text:
            flash('Por favor completa todos los campos.', 'error')
            return redirect(url_for('dual_simplex'))
        
        constraints_list = [line.strip() for line in constraints_text.split('\n') 
                           if line.strip()]
        
        result = solve_dual_simplex(objective, constraints_list)
        
        if not result['success']:
            flash(result['error'], 'error')
            return redirect(url_for('dual_simplex'))
        
        return render_template('dual_simplex_results.html', 
                             objective=objective,
                             constraints=constraints_list,
                             result=result)
        
    except Exception as e:
        flash(f'Error inesperado: {str(e)}', 'error')
        return redirect(url_for('dual_simplex'))

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
            'title': 'Primer Ejercicio del Taller',
            'objective': 'maximizar z = x + y',
            'constraints': 'x + 3y <= 26\n4x + 3y <= 44\n2x + 3y <= 28\nx >= 0\ny >= 0',
            'description': 'Problema de maximización con restricciones lineales.'
        },
        {
            'title': 'Segundo Ejercicio del Taller',
            'objective': 'minimizar z = 3x + 2y',
            'constraints': '3x + 4y <= 12\n3x + 2y >= 2\nx >= 0\ny >= 0',
            'description': 'Problema de minimización con restricciones mixtas.'
        },
        {
            'title': 'Problema de Producción Industrial',
            'objective': 'maximizar z = 5x + 4y',
            'constraints': '2x + 3y <= 18\n4x + 2y <= 20\nx + y >= 2',
            'description': 'Problema típico de optimización en producción industrial.'
        },
        {
            'title': 'Problema de Recursos Limitados',
            'objective': 'minimizar z = 2x + 5y',
            'constraints': 'x + 2y >= 8\n3x + y >= 9\n2x + 4y <= 24',
            'description': 'Optimización con restricciones de recursos limitados.'
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
    print("📊 Métodos: Gráfico, Simplex y Dual Simplex")
    print("🎓 Investigación de Operaciones - Segundo Parcial")
    print("👨‍💻 Desarrollado por José Miguel Herrera Gutiérrez para UTP")
    print("👩‍🏫 Profesora: Bibiana Patricia Arias Villada")
    
    if debug:
        print("🌐 Abre tu navegador en: http://localhost:5000")
    else:
        print(f"🌐 Servidor ejecutándose en puerto: {port}")
    
    print("-" * 50)
    
    app.run(debug=debug, host='0.0.0.0', port=port)