# functions

# ! functions return None if there is no return statement

import math


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers())


def add_ten(num):
    return num + 10


num_one = 5
print(num_one)
num_one = add_ten(num_one)
print(num_one)


def sum_two_numbers(a, b):
    return a + b


print(f'The sum of two numbers {sum_two_numbers(1, 9)}')

# ? when passing arguments with key and value, order does not matter


def add_two_numbers(num1, num2):
    return num1 + num2


print(add_two_numbers(num2=3, num1=2))

# ? can have default parameters with functions


def weight_of_object(mass, gravity=9.81):
    weight = str(mass * gravity) + ' N'
    return weight


print(f'Weight of an object in Newtons: {weight_of_object(100)}')

# ? can have arbitrary parameters when you dont know how many you want


def sum_all_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


print(sum_all_nums(2, 3, 5))
print(sum_all_nums(2, 3, 4, 5, 6, 7))

# ? use ** when you have a function with parameters with the same name as a dictionary key and value pair


def greet(name, location):
    print(f'Hi there, {name}, how is the weather in {location}')


my_dict = {'name': 'Naruto', 'location': 'Konoha'}
greet(**my_dict)

# * can also have arbitrary number of named arguments for a dictionary


def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)

# ? can also pass in a function as a parameter for another function


def square_number(x):
    return x * x


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))

# ! EXERCISES


def add_two_numbers(a, b):
    return a + b


def calculate_area_of_circle(radius):
    return 3.14 * radius * radius


def add_all_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


def convert_celsius_to_fahrenheit(degrees):
    return (degrees * (9/5)) + 32


def check_season(month):
    autumn = ('September', 'October', 'November')
    winter = ('December', 'January', 'February')
    spring = ('March', 'April', 'May')
    summer = ('June', 'July', 'August')
    if month in autumn:
        return autumn
    elif month in winter:
        return winter
    elif month in spring:
        return spring
    else:
        return summer


def calculate_slope(x1, x2, y1, y2):
    return ((y2 - y1) / (x2 - x1))


def solve_quadratic_eqn(a, b, c):
    print(
        f'The solution to that quadratic formula is {(-b) + math.sqrt((b * b) - (4 * (a) * (c)))} and {(-b) - math.sqrt((b * b) - (4 * (a) * (c)))}')


def reverse_list(lst):
    copy = lst.copy()
    for s in range(len(lst) // 2):
        copy[s], copy[-1 - s] = copy[-1 - s], copy[s]
    return copy


def capitalize_list_items(lst):
    return [item.upper() for item in lst]


def add_item(lst, *items):
    for item in items:
        lst.append(item)
    return lst


def remove_item(lst, item):
    if lst.get(item):
        lst.remove(item)
    return lst


def sum_of_numbers(num):
    sum = 0
    for s in range(num + 1):
        sum += s
    return sum


def sum_of_odds(num):
    sum_odds = 0
    for s in range(1, num + 1, 2):
        sum_odds += s
    return sum_odds


def sum_of_even(num):
    sum_evens = 0
    for s in range(0, num + 1, 2):
        sum_evens += s
    return sum_evens


def evens_and_odds(num):
    num_odds, num_evens = 0, 0
    for s in range(num + 1):
        if s % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    return (f'The number of odds are {num_odds}.\nThe number of evens are {num_evens}.')


def factorial(num):
    total = 1
    for s in range(1, num + 1):
        total *= s
    return total


def is_empty(arg):
    return not bool(arg)


def calculate_mean(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)


def calculate_median(lst):
    return sorted(lst)[len(lst) // 2]


def calculae_mode(lst):
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1
    max_count = max(count.values())
    modes = [key for key, count in count.items() if count == max_count]
    return modes


def calculate_range(lst):
    return max(lst) - min(lst)


def greet(name='Guest'):
    print(f'Hello, {name}!')


def show_args(**args):
    for key, value in args.items():
        print(f'{key}: {value}', end=', ')


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for s in range(3, int(num**0.5) + 1, 2):
        if num & s == 0:
            return False
    return True


def check_unique_items(lst):
    temp = []
    for item in lst:
        if item in temp:
            return False
        temp.append(item)
    return True


def check_same_data_types(lst):
    if not lst:
        return True
    type_first = type(lst[0])
    for item in lst:
        if type_first != type(item):
            return False
    return True


def check_variable_name(name):
    return name.isidentifier() and not name.iskeyword()
