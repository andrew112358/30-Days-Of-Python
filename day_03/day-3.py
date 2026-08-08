# # Operators

# age = 19
# h = 177.16
# comp = 1 + 3j

# base = int(input("Enter base: "))
# height = int(input("Enter height: "))
# area_triagle = int(0.5 * base * height)
# print(f"The area of the triangle is {area_triagle}")

# a = int(input("Enter side a: "))
# b = int(input("Enter side b: "))
# c = int(input("Enter side c: "))
# perimeter_triangle = a + b + c
# print(f"The perimeter of the triangle is {perimeter_triangle}")

# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# area_rectangle = length * width
# perimeter_rectangle = (length * 2) + (width * 2)
# print(
#     f"The area of the rectangle is {area_rectangle} and the perimeter is {perimeter_rectangle}")

# radius = int(input("Enter the radius of a circle: "))
# area_circle = 3.14 * radius * radius
# circumference_circle = 2 * 3.14 * radius
# print(
#     f"The area of the circle is {area_circle} and the circumference is {circumference_circle}")

# print(len('python') != len('dragon'))

# print('on in python', 'on' in 'python', 'on in dragon' 'on' in 'dragon')

# print('jargon in I hope this course is not full of jargon',
#       'jargon' in 'I hope this course is not full of jargon')

# length_of_python = len('python')
# float_python = float(length_of_python)
# str_python = str(length_of_python)

# num_1 = int(input("Enter a number to check if it is odd or even: "))
# if num_1 % 2 == 0:
#     print('even')
# else:
#     print('odd')

# print("check floor division of 7 by 3 is equal to int conversion of 2.7",
#       (7//3) == int(2.7))

# print('check if type of \'10\' is equal to type of 10', type('10') == type(10))

# # error since you can not enter '9.8' into the int function, need to convert to float first then int
# print('check if int(\'9.8\') is eaual to 10', int('9.8') == 10)

# hours = int(input("Enter hours: "))
# rate = int(input("Enter rte per hour: "))
# weekly_earning = hours * rate
# print(f"Your weekly earning is {weekly_earning}")

# years = int(input("Enter number of years you have lived: "))
# seconds_lived = years * 365 * 24 * 60 * 60
# print(f"You have lived for {seconds_lived} seconds")

for s in range(1, 6):
    print(s, end=' ')
    for i in range(4):
        print(s ** i, end=' ')
    print()
