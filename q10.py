from sympy import Matrix, symbols

# Define the symbols
x, y, z = symbols('x y z')

# Define the coefficient matrix
A = Matrix([[3, 7, -12], [4, -2, -5]])

# Define the constant matrix
B = Matrix([0, 0])

# Augment A with B
augmented_matrix = A.row_join(B)

# Compute the RREF of the augmented matrix
reduced_row_echelon_form, pivot_columns = augmented_matrix.rref()

# Extract the solution
solution = [reduced_row_echelon_form[i, -1] for i in range(reduced_row_echelon_form.rows) if i in pivot_columns]

# Print the solution
if len(solution) == 3:
    print(f"x = {solution[0]}\ny = {solution[1]}\nz = {solution[2]}")
else:
    print("No unique solution exists.")
