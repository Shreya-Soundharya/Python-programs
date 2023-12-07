#Program to find occurences of a number

def count_occurrences(arr, target):
    count = 0

    for element in arr:
        if element == target:
            count += 1

    return count

arr = [int(x) for x in input("Enter an array of numbers separated by spaces: ").split()]
target = int(input("Enter the element you want to count: "))
occurrences = count_occurrences(arr, target)
print(f"The element {target} occurs {occurrences} times in the array.")