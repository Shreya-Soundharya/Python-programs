#Program to find avegage of n syudents
#create an empty list 
list1 = [] 
print("How many students marks you want to enter: ")
n = int(input())
for i in range(0,n):
 print("Enter marks of student",(i+1),":")
 marks = int(input())
 #append marks in the list
 list1.append(marks) 
 #initialize total 
 total = 0 
 for marks in list1:
 #add marks to total 
total = total + marks 
average = total / n
print("Average marks of",n,"students is:",average)
