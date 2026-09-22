# functions

# ! functions return None if there is no return statement

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
