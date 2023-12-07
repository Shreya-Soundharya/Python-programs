#Reverse an array

n=int(input("Enter number of elements in array: "))
l=[]
for i in range(n):
    e=float(input("Enter the element: "))
    l.append(e)
print("The array is: ",l)
print("\nReversed array is: ",l[::-1])