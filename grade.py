#Progeam to calculate grade from marks

n=int(input("Enter your mark: "))
print("\n")
if n in range(91,100):
    print("O grade")
elif n in range(81,90):
    print("A+ grade")
elif n in range(71,80):
    print("A grade")
elif n in range(61,70):
    print("B+ grade")
elif n in range(56,60):
    print("B grade")
elif n in range(50,55):
    print("C grade")
elif n in range(0,49):
    print("F grade")
else:
    print("N/A")
