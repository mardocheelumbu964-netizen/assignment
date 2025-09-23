# Define factorial function using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function with a sample number
num = 5
result = factorial(num)

# Print the output
print("Factorial of", num, "is:", result)
