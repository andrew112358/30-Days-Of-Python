# Operators

age = 19
h = 177.16
comp = 1 + 3j

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_triagle = int(0.5 * base * height)
print(f"The area of the triangle is {area_triagle}")

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter_triangle = a + b + c
print(f"The perimeter of the triangle is {perimeter_triangle}")

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = (length * 2) + (width * 2)
print(
    f"The area of the rectangle is {area_rectangle} and the perimeter is {perimeter_rectangle}")

radius = int(input("Enter the radius of a circle: "))
area_circle = 3.14 * radius * radius
circumference_circle = 2 * 3.14 * radius
print(
    f"The area of the circle is {area_circle} and the circumference is {circumference_circle}")

print(len('python') != len('dragon'))

print('on in python', 'on' in 'python', 'on in dragon' 'on' in 'dragon')

print('jargon in I hope this course is not full of jargon',
      'jargon' in 'I hope this course is not full of jargon')
