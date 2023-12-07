def sum_even_and_odd_numbers(arr):
    sum_even = 0
    sum_odd = 0

    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_even, sum_odd

try:
    arr = [int(x) for x in input("Enter an array of numbers separated by spaces: ").split()]
    even_sum, odd_sum = sum_even_and_odd_numbers(arr)
    
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
except ValueError:
    print("Invalid input. Please enter a list of numbers.")
