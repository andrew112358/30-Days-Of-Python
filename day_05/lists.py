# Lists

#! ordered and changeable, allows for duplicate members

lst1 = list()
lst2 = []

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']

print('fruits:', fruits)
print('web techs:', web_techs)

# ? lists can contain different data types
lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]

# ? can use zero indexing to access elemnts in the list and also negative
print(fruits[0])
print(fruits[-4])
print(fruits[1])
print(fruits[-3])

# ? can also unpack a list into different variables
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

countries = ['Germany', 'France', 'Belgium', 'Sweden',
             'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# ? can also slice lists similar to strings
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:]
all_fruits = fruits[0:4]
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]

all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
reverse_fruits = fruits[::-1]

# ? lists also mutable
fruits[0] = 'avocado'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

# ? use the in operator to check if something is in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

# ? use appned to add an item to the end
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)

# ? use insert(indext, item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')
print(fruits)

# ? remove(item) removes the first occurrence of the item in the list
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)

# ? can also use the pop(index) method where if no index specified pops the end
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
fruits.pop(0)
print(fruits)

# ? can use the del function to delete the whole list or part of it
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits
# * printing would give an error since the list fruits was deleted

# ? clear() empties the list
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
fruits.clear()
print(fruits)

# ? assigning lists make references (shallow copy) use the .copy() to make deep copy
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
lst_copy = fruits.copy()
print(lst_copy)

# ? can use the + symbol to join lists or the .extend(list) function
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print(negative_numbers)

print(print(1), print(2))
