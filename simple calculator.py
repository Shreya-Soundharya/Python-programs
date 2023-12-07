x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))

print("\n1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")
print("5-Modulus")

while True:
    t=float(input("\nEnter arithmetic operation to be performed: "))
    if t==1:
        print(x,"+",y,"=",x+y)
        break
    elif t==2:
        print(x,"-",y,"=",x-y)
        break
    elif t==3:
        print(x,"x",y,"=",x*y)
        break
    elif t==4:
        print(x,"/",y,"=",x/y)
        break
    elif t==5:
        print(x,"||",y,"=",x%y)
        break
    else:
        print("Invalid code. Input valid code from displayed options.\n")
        continue
