# Strings

a = 3
b = 4
print(f'{a} / {b} = {a / b:.2f}')

language = 'python'
first_three = language[0:3]
print(first_three)
last_three = language[-3:]
print(last_three)

reverse_language = language[::-1]
print(reverse_language)

pto = language[0:6:2]
print(pto)

challenge = 'thirty days of python'
challenge.count('y')  # counts number of occurences
challenge.endswith('on')  # checks if strings endw with ending
# relpalces tab character with spaces, default size 8
challenge.expandtabs(10)
challenge.find('y')  # finds first occurence, -1 if not found
challenge.rfind('y')  # finds last occurence, -1 if not found
challenge.index('da')  # returns lowest index of substring, error if not found
# additional args indicate starting and ending index
challenge.rindex('da')  # finds the highest index
challenge.isalnum()  # checks if alphanumeric
challenge.isalpha()  # checks if all alphabet
challenge.isdecimal()  # checks if all 0-9
challenge.isdigit()  # checks if all 0-9
# checks for valid identifier, if sting name could be variable name
challenge.isidentifier()

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# returns concatenated string 'HTML CSS JavaScript React'
result = ' '.join(web_tech)

challenge.strip('noth')  # strips all characters from the string
challenge.split()  # splits the string using given string or space as separator
challenge.title()  # returns title cased string
challenge.swapcase()  # changes case
challenge.startswith('thirty')  # checks if string starts with specified string

# Excercises
challenge = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
str_1 = 'Coding ' + 'For ' + 'All'
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
slice_first_word = company[company.index(' ') + 1:]
print(slice_first_word)

if "Coding For All".index('Coding') != -1:
    print(True)

company = 'Coding For All'
company = company.replace('Coding', 'Python')
print(company)

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(
    ', ')
print(companies)

print('Coding For All'[0])
print('Coding For All'[10])

acronym_1 = ''.join(word[0].upper() for word in "Python For Everyone".split())
acronym_2 = ''.join(word[0].upper() for word in "Coding For All".split())

index_C = 'Coding For All'.index('C')
index_F = 'Coding For All'.index('F')
last_index_l = 'Coding For All People'.rfind('l')

conjunction = 'You cannot end a sentence with because because because is a conjunction'
print("First index of because: ", conjunction.find('because'))
print("Last index of because: ", conjunction.rfind('because'))

conjunction = conjunction.replace('because because because ', '')
print("Remove \'because because because\'", conjunction)

company = '   Coding For All      '
company = company[company.index('C'):company.rfind('l') + 1]
print(company)

check_valid_identifier = '30DaysOfPython'
print(check_valid_identifier.isidentifier())
check_valid_identifier = 'thirty_days_of_python'
print(check_valid_identifier.isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
python_libraries_string = '# '.join(python_libraries)
print(python_libraries_string)

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = int(3.14 * radius ** 2)
print(f'The area of a circle with radius {radius} is {area} meters square.')
