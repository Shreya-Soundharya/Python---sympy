from sympy import symbols, limit, sin

# Define the symbol
x = symbols('x')

# Define the expression
expression = (sin(x) - x) / x**3

# Calculate the limit
result = limit(expression, x, 0)

# Print the result
print(result)
