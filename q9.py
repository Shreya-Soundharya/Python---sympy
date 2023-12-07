from sympy import symbols, Function, dsolve

# Define the symbol
x = symbols('x')

# Define the function f(x)
f = Function('f')

# Define the differential equation
diff_eq = f(x).diff(x, 2) + 9*f(x) - 1

# Solve the differential equation
solution = dsolve(diff_eq, f(x))

# Print the solution
print(solution)
