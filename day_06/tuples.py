# tuples

# ! ordered and immutable

empty_tuple = ()
empty_tuple = tuple()

fruits = ('banana', 'orange', 'mango', 'lemon')

print('fruit tuple lenght', len(fruits))

first_fruit = fruits[0]
last_fruit = fruits[len(fruits) - 1]

first_fruit = fruits[-4]
last_fruit = fruits[-1]

all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_and_rest = fruits[1:]

all_fruits = fruits[-4:]
middle_two_fruits = fruits[-3:-1]  # does not include fruit at index -3
orange_and_rest = fruits[-3:]

# ? can change a tuple to a list with the list(tuple) method
fruits = list(fruits)
print(fruits)
fruits = tuple(fruits)
print(fruits)

# ? use in to check if something is in the tuple or not
print('orange' in fruits)
print('watermelon' in fruits)

# ? join tuples with the + operator
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# ? same like lists use del to delete tuples
del fruits
del vegetables

# * Exercises
empty_tuple = ()
empty_tuple = tuple()

brothers = ('M', 'E')
cousins = ('A', 'M', 'A', 'R', 'H')
brothers_and_cousins = brothers + cousins

print(len(brothers_and_cousins))
brothers_and_cousins = list(brothers_and_cousins)
brothers_and_cousins.append(['M', 'K', 'M', 'R', 'M', 'J'])
extended_fam = tuple(brothers_and_cousins)
print(extended_fam)

*brothers_and_cousins, parents = extended_fam

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('eggs', 'milk', 'cheese', 'meat')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)

middle_items = food_stuff_tp[1:len(food_stuff_tp) - 1]
middle_items = food_stuff_lt[1:len(food_stuff_lt) - 1]
print(middle_items)

first_three_items = food_stuff_lt[0:3]
print(first_three_items)
last_three_items = food_stuff_lt[-3:]
print(last_three_items)

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
