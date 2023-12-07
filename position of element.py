#Positive elements in list

list1 = []
maximum = int(input("How many numbers do you want to enter in the list: "))
print("Enter a list of numbers one by one:")
for i in range(0, maximum):
    n = int(input())
    list1.append(n)

num = int(input("Enter the number to be searched: "))
position = -1

for i in range(0, len(list1)):
    if list1[i] == num:
        position = i + 1
        break

if position == -1:
    print(num, "is not present in the list")
else:
    print(num, "is present at position", position)
