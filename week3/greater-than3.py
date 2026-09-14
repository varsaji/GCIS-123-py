a = int (input("enter the first number: "))
b = int (input("enter the second number: "))
c = int (input("enter the third number: "))
if a > b and a > c:
    print("the first number is greater than the second and third number")
elif b > a and b > c:
    print("the second number is greater than the first and third number")
elif c > a and c > b:
    print("the third number is greater than the first and second number")
else:
    print("all numbers are equal")