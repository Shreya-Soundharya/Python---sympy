from sympy import symbols, Eq, solve

# Define the symbols
x, y, z = symbols('x y z')

# Define the equations
eq1 = Eq(3*x + 7*y, 12*z)
eq2 = Eq(4*x - 2*y, 5*z)

# Solve the equations
solution = solve((eq1, eq2), (x, y, z))

# Print the solution
print(solution)
