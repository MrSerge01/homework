a = int(input("Length of the first side: "))
b = int(input("Length of the second side: "))
c = int(input("Length of the third side: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("This is not a triangle.")
else:
    if a == b == c:
        print("This is the equilateral triangle.")
    elif a != b != c:
        print("This is the scalene triangle.")
    else:
        print("This is the isosceles triangle.")
