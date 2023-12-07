def print_diamond_pattern(n):
    # Print the top half of the diamond
    for i in range(1, n + 1, 2):
        spaces = (n - i) // 2
        numbers = ''.join(map(str, range(1, i + 1)))
        print(" " * spaces + numbers)

    # Print the bottom half of the diamond
    for i in range(n - 2, 0, -2):
        spaces = (n - i) // 2
        numbers = ''.join(map(str, range(1, i + 1)))
        print(" " * spaces + numbers)

try:
    n = int(input("Enter the number of rows for the diamond pattern: "))
    if n % 2 == 0:
        n += 1  # Make sure n is odd for a symmetric diamond

    print_diamond_pattern(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
