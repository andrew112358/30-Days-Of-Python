# conditionals

a = 3
if a > 0:
    print('A is a positive number')

if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

a = 0

if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# ? short hand method in one line
a = 3
print('A is positive') if a > 0 else print('A is negative')

# ? nested conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# ? can avoid nested with logical operators
# * using the and operator
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# * using the or operator
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')

# ! EXERCISES

age = int(input('Enter your age: '))
print('You are old enough to drive.') if age > 18 else print(
    f'You need {18 - age} more years to learn to drive.')

your_age = int(input('Enter your age: '))
my_age = 21
if your_age > my_age:
    if your_age - my_age == 1:
        print('You are 1 year older than me')
    else:
        print(f'You are {your_age - my_age} years older than me')
elif your_age == my_age:
    print('We are the same age')
else:
    if my_age - your_age == 1:
        print('You are 1 year younger than me')
    else:
        print(f'You are {my_age - your_age} years younger than me')

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a == b:
    print(f'{a} is equal to {b}')
else:
    print(f'{a} is less than {b}')

score = int(input('Enter your score: '))
grade = 'A'
if score < 90 and score >= 80:
    grade = 'B'
elif score < 80 and score >= 70:
    grade = 'C'
elif score < 70 and score >= 60:
    grade = 'D'
elif score < 60:
    grade = 'F'
print(f'Your final grade is: {grade}')

autumn = ('September', 'October', 'November')
winter = ('December', 'January', 'February')
spring = ('March', 'April', 'May')
summer = ('June', 'July', 'August')
month = input('Enter a month: ')
if month in autumn:
    print(f'{month} is during the Autumn season')
elif month in winter:
    print(f'{month} is during the Winter season')
elif month in spring:
    print(f'{month} is during the Spring season')
else:
    print(f'{month} is during the Summer season')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit to add to the list: ')
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(f'{fruit} was successfully added to the list')

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    temp = person.get('skills')
    print(temp[len(temp) // 2])
if 'skills' in person:
    print('Python' in person.get('skills'))

if 'skills' in person:
    temp = person.get('skills')
    if 'JavaScript' in temp and 'React' in temp:
        print('He is a front end developer')
    elif 'Node' in temp and 'Python' in temp and 'MongoDB' in temp:
        print('He is a backend developer')
    elif 'React' in temp and 'Node' in temp and 'MongoDB' in temp:
        print('He is a fullstack developer')
    else:
        print('unknown title')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f'{person.get('first_name')} {person.get('last_name')} live in Finland. He is married')
