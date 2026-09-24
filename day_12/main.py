from random import random, randint
import string
import math
from statistics import *  # importing all the statistics modules
import sys
import os
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
from mymodule import generate_full_name, sum_two_nums, person, gravity
import mymodule

print(mymodule.generate_full_name('Bob', 'He'))

# ? can also improt functions differently
print(generate_full_name('Asabneh', 'Yetayeh'))
print(sum_two_nums(1, 9))
mass = 100
weight = mass * gravity
print(weight)
# print(person['firstname'])

# ? can also import functions with different names

# ? common built-in modules include
# * math, datetime, os, sys, random, statistics, collections, json, re

# ! os module
# * provides functions for creating, changing current working directory, removing, fetching contents, changing and identifying the current directory
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

# ! sys module
# * used to manipulate parts of the Python runtime environment
# print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version

# ! statistics module
# * functions for mathematical statistics of numeric data
# * mean, median, mode, stdev, etc.
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

# ! math module
# * mathematical operations and constants
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(pow(2, 3))    # 8.0, exponential function
print(floor(9.81))  # 9, rounding to the lowest
print(ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

# ! string module
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# ! random module
# it doesn't take any arguments; it returns a value between 0 and 0.9999
print(random())
# it returns a random integer number between [5, 20] inclusive
print(randint(5, 20))

# ! Exercises


def random_user_id():
    letters_and_digits = string.ascii_letters + string.digits
    id = ''
    for s in range(6):
        id += letters_and_digits[randint(0, len(letters_and_digits) - 1)]
    return id


def user_id_gen_by_user():
    num_characters = int(input('Enter the number of characters for your id: '))
    num_ids = int(input('Enter the number of ids you want generate: '))
    letters_and_digits = string.ascii_letters + string.digits
    for s in range(num_ids):
        id = ''
        for i in range(num_characters):
            id += letters_and_digits[randint(0, len(letters_and_digits) - 1)]
        print(id)


def rgb_color_gen():
    return f'rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})'


def list_of_hexa_colors():
    symbols = string.digits + 'abcdef'
    hexadecimal = ''
    for s in range(6):
        hexadecimal += symbols[randint(0, len(symbols))]
    return hexadecimal


def list_of_rgb_colors():
    pass
