def find_maximum_of_three_numbers(a, b, c):
    return max(a, b, c)

# Get input from the user for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the function to find the maximum
maximum = find_maximum_of_three_numbers(num1, num2, num3)

# Print the result
print(f"The maximum of {num1}, {num2}, and {num3} is: {maximum}")
