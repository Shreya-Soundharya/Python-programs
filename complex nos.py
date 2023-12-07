def complex_addition(a, b):
    return a + b

def complex_subtraction(a, b):
    return a - b

def complex_multiplication(a, b):
    return a * b

def complex_division(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

# Example complex numbers
complex_num1 = complex(2, 3)
complex_num2 = complex(1, 2)

# Perform arithmetic operations
addition_result = complex_addition(complex_num1, complex_num2)
subtraction_result = complex_subtraction(complex_num1, complex_num2)
multiplication_result = complex_multiplication(complex_num1, complex_num2)
division_result = complex_division(complex_num1, complex_num2)

# Display the results
print(f"Complex Number 1: {complex_num1}")
print(f"Complex Number 2: {complex_num2}")

print(f"Addition Result: {addition_result}")
print(f"Subtraction Result: {subtraction_result}")
print(f"Multiplication Result: {multiplication_result}")
print(f"Division Result: {division_result}")
