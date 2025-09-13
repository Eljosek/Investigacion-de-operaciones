# Linear Programming Solver - Web Application

A comprehensive web-based linear programming solver built for university coursework in Operations Research. This application provides both analytical solutions and visual representations of optimization problems.

## Features

- **Graphical Method**: Solve 2-variable linear programming problems with visual representation
- **Interactive Web Interface**: Modern, responsive design with dark mode support
- **Mathematical Symbol Support**: Accepts standard inequality symbols (≤, ≥) and variable constraints
- **Real-time Validation**: Input validation with immediate feedback
- **Dynamic Plotting**: Automatic generation of constraint graphs and feasible regions
- **Complete Solution Analysis**: Shows optimal point, objective function value, and constraint analysis

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Eljosek/Investigacion-de-operaciones.git
   cd Investigacion-de-operaciones
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to `http://localhost:5000`

## Technology Stack

- **Backend**: Python 3.x with Flask framework
- **Mathematical Computing**: NumPy for linear algebra operations
- **Visualization**: Matplotlib for graph generation
- **Frontend**: HTML5, CSS3, JavaScript with Bootstrap 5
- **Styling**: Font Awesome icons, custom CSS with dark mode

## Application Structure

```
├── app.py                 # Flask application and routes
├── lp_solver.py          # Core linear programming algorithms
├── metodo_grafico.py     # Graphical method implementation
├── static/
│   ├── css/styles.css    # Custom styling and dark mode
│   └── js/app.js         # Frontend validation and interactions
├── templates/            # HTML templates
└── requirements.txt      # Python dependencies
```

## Usage Example

### Problem Setup:
- **Objective Function**: Maximize Z = 3x + 2y
- **Constraints**:
  - x + y ≤ 4
  - 2x + y ≤ 6
  - x ≥ 0, y ≥ 0

### Input Format:
1. Enter objective function: `3x + 2y`
2. Select "Maximize"
3. Enter constraints (one per line):
   ```
   x + y <= 4
   2x + y <= 6
   ```

The application automatically handles non-negativity constraints.

## Supported Constraint Formats

- Standard inequalities: `x + y <= 4`, `2x - y >= 1`
- Mathematical symbols: `x + y ≤ 4`, `2x - y ≥ 1`
- Variable bounds: `x >= 2`, `y <= 5`
- Variable relationships: `x <= y`, `y >= x`
- Equality constraints: `x + y = 3`

## Algorithm Implementation

The solver uses the **Graphical Method** for 2-variable linear programming:

1. **Constraint Processing**: Parse and validate all constraints
2. **Intersection Calculation**: Find all constraint intersections
3. **Feasible Region**: Determine viable solution space
4. **Corner Point Evaluation**: Test objective function at all vertices
5. **Optimization**: Identify optimal solution based on maximization/minimization

## Development Notes

- Built for educational purposes in Operations Research
- Focuses on 2-variable problems for graphical visualization
- Includes comprehensive input validation and error handling
- Designed for easy extension to additional LP methods

## Academic Context

This application was developed as part of a university parcial in Operations Research, demonstrating practical implementation of linear programming concepts with modern web technologies.

## License

This project is developed for educational purposes. Feel free to use and modify for academic work.