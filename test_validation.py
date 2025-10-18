from simplex_tableau import solve_simplex_tableau

result = solve_simplex_tableau('max z = 3x1 + 2x2', ['x1 + x2 >= 4'])
print(f"Success: {result['success']}")
print(f"Error: {result.get('error', 'N/A')}")
print(f"Status: {result.get('status', 'N/A')}")
