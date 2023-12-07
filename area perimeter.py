#Program to find area and perimiter

print("Choose the shape: ")
print("1-Triangle")
print("2-Rectangle")
print("3-Circle")

while True:
    t = int(input("Enter the shape: "))
    if t == 1:
        s1 = float(input("Enter length of the 1st side of the triangle: "))
        s2 = float(input("Enter length of the 2nd side of the triangle: "))
        s3 = float(input("Enter length of the 3rd side of the triangle: "))
        perimeter = s1 + s2 + s3
        print("Perimeter of the triangle is %.2f" % perimeter)
        s = (s1 + s2 + s3) / 2
        area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
        print("Area of the triangle is: %.2f" % area)
        break
    elif t == 2:
        r1 = float(input("Enter length of the rectangle: "))
        r2 = float(input("Enter width of the rectangle: "))
        perimeter = 2 * (r1 + r2)
        area = r1 * r2
        print("Perimeter of the rectangle is %.2f" % perimeter)
        print("Area of the rectangle is: %.2f" % area)
        break
    elif t == 3:
        c1 = float(input("Enter radius of the circle: "))
        perimeter = 2 * 3.14 * c1
        area = 3.14 * (c1 ** 2)
        print("Perimeter of the circle is %.2f" % perimeter)
        print("Area of the circle is: %.2f" % area)
        break
    else:
        print("Invalid code. Input valid code from displayed options.\n")
        continue
