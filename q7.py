from sympy import symbols, solve

# Define the symbols
x, y = symbols('x y')

# Define the equations
equation1 = x + y - 2
equation2 = 2*x + y

# Solve the system of equations
solution = solve((equation1, equation2), (x, y))

# Print the solution
print(f"x = {solution[x]}, y = {solution[y]}")
