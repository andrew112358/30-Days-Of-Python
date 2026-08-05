# Day 2: 30 Days of python programming
import math

first_name = "Andrew"
last_name = "Lim"
full_name = "Andrew Lim"
country = "United States of America"
city = "San Francisco"
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = True
first_name, last_name, country, age, is_married = "Tom", "Wu", "China", 100, True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
divide = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = math.floor(num_one / num_two)

radius = 30
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius
radius = int(input("Enter the radius of a circle: "))
area_of_circle = math.pi * (radius ** 2)
print(f"The area of a circle with radius {radius} is {area_of_circle}")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter a country: ")
age = int(input("Enter an age: "))
