import math
a = int(input("Enter Length one: "))
b = int(input("Enter Length two: "))
c = int(input("Enter Length three: "))
if a+b>c and a+c>b and b+c>a:
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("The area of the triangle is",area)
else:
    print("Triangle can't exist")




