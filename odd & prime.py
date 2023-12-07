def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    num = int(input("Enter a number: "))
    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    
    if is_prime(num):
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
