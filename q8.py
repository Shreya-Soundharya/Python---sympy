from sympy import symbols, integrate, sin, cos

# Define the symbols
x, y = symbols('x y')

# Define the functions
f1 = x**2
f2 = sin(x)
f3 = cos(x)

# Integrate the functions
integral_f1 = integrate(f1, x)
integral_f2 = integrate(f2, x)
integral_f3 = integrate(f3, x)
integral_f4 = integrate(f1, y)
integral_f5 = integrate(f2, y)
integral_f6 = integrate(f3, y)

# Print the results
print("Integral of x^2 with respect to x:", integral_f1)
print("Integral of sin(x) with respect to x:", integral_f2)
print("Integral of cos(x) with respect to x:", integral_f3)
print("Integral of x^2 with respect to y:", integral_f4)
print("Integral of sin(x) with respect to y:", integral_f5)
print("Integral of cos(x) with respect to y:", integral_f6)
