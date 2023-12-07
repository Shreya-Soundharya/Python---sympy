from sympy import symbols, simplify, sin, cos

# Define the symbol
x = symbols('x')

# Define the expression
expression = sin(x) / cos(x)

# Simplify the expression
simplified_expression = simplify(expression)

# Print the simplified expression
print(simplified_expression)
