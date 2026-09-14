def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    elif a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

print(triangle_type(3, 3, 3))  # Equilateral
print(triangle_type(3, 4, 3))  # Isosceles
print(triangle_type(3, 4, 5))  # Scalene
