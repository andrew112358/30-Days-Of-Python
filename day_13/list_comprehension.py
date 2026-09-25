# list comprehension

# ! comparct way of creating a list from a sequence
# ! faster than processing a list using the for loop
# ? syntax
# * [expression for i in iterable if condition]

language = 'Python'
lst = list(language)  # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

lst = [i for i in language]
print(type(lst))
print(lst)

# ? can generate numbers too

numbers = [i for i in range(11)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [i * i for i in range(11)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers = [(i, i * i) for i in range(11)]
print(numbers)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# ? can use if condition too
# * even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# * odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# * filter numbers such as positive even numbers
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# * flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ! lambda function
# ? function without a name that can take any number of arguments
# * only one expression, need for anonymous functions inside another function


x = lambda param1, param2, param3: param1 + param2 + param3

print(x(1, 2, 3))

# named function
def add_two_nums(a, b):
    return a + b
print(add_two_nums(2, 3))

add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))

