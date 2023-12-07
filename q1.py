import decimal

# Set the precision to 100 decimal places
decimal.getcontext().prec = 100

# Calculate the square root of 2
root_two = decimal.Decimal(2).sqrt()

# Print the result
print(root_two)
