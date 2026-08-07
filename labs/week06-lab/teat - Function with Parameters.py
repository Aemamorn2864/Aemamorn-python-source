# PART 2: FUNCTIONS WITH PARAMETERS
"""
# Example 1: Function with one parameter
def greet_person(name):
    #Greets a person by name
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()
"""
"""
# Example 2: Function with multiple parameters
def introduce_person(name, age, city):
    #Introduces a person with their details
    print(f"Hi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")
    print()

print("Calling introduce_person:")
introduce_person("Diana", 25, "New York")
introduce_person("Eve", 30, "Los Angeles")
"""

# Example 3: Mathematical function
def calculate_rectangle_area(length, width):
    #Calculates and displays rectangle area
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)