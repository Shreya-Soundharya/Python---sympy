from sympy import symbols, diff, log, sin, cos

# Define the symbol
x = symbols('x')

# Define the functions
f1 = log(x)
f2 = 1 / x
f3 = sin(x)
f4 = cos(x)

# Calculate the derivatives
derivative_f1 = diff(f1, x)
derivative_f2 = diff(f2, x)
derivative_f3 = diff(f3, x)
derivative_f4 = diff(f4, x)

# Print the results
print("Derivative of log(x):", derivative_f1)
print("Derivative of 1/x:", derivative_f2)
print("Derivative of sin(x):", derivative_f3)
print("Derivative of cos(x):", derivative_f4)
