"""
def calculate_triangle_area(height, base):
    #Calculates and displays triangle area
    area = 0.5 * height * base
    print(f"Triangle with height {height} and base {base}")
    print(f"Area = 0.5 * {height} * {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)


def calculate_circle_area(radius):
    #Calculates and displays circle area
    area = 3.14 * radius ** 2
    print(f"Circle with radius {radius}")
    print(f"Area = 3.14 * {radius} ** 2 = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5)
calculate_circle_area(10)
"""

def calculate_sphere(radius):
    volume = 4.0 / 3 * 3.14 * radius ** 3
    print(f"sphere with radius {radius}")
    print(f"Volume = 4.0/3 * {radius} ** 3 = {volume}")
    print()

print("Calculating sphere volume: ")
calculate_sphere(10)
calculate_sphere(20)