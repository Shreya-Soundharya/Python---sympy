from sympy import expand, symbols

# Define the symbols
x, y = symbols('x y')

# Calculate the expanded form of (x+y)^6
expression = (x + y) ** 6
expanded_form = expand(expression)

# Print the expanded form
print(expanded_form)
