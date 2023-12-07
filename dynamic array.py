n = int(input("Enter the number of elements in the array: "))
arr = [0] * n
for i in range(n):
    arr[i] = int(input(f"Enter element {i + 1}: "))
tot = sum(arr)
    
print("Array is: ",arr)
print("Sum of all elements in the array is: ",tot)

