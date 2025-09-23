import math

# 1. Ask the user for a number
num = float(input("Enter a number: "))

# 2. Perform calculations using math module
sqrt_val = math.sqrt(num)
log_val = math.log(num)   # natural logarithm (base e)
sine_val = math.sin(num)  # sine in radians

# 3. Display the results
print("Square root of", num, "is:", sqrt_val)
print("Natural logarithm of", num, "is:", log_val)
print("Sine of", num, "is:", sine_val)
