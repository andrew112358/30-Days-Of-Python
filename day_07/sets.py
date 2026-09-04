# sets

# ! unordered and un-indexed distinct elements just like math
# * can find union, intersection, difference, symmetric difference, subset, super set, and disjoin set

st = set()
st = {'item1', 'item2', 'item3', 'item4'}

fruits = {'banana', 'orange', 'mango', 'lemon'}

# ? same for strings lists and tuples use the len() function
print(len(fruits))

# ? use loops to access items in a set

# ? use in to check existence
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)

# ? use .add(item) to add items to set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('apple')
print(fruits)

# ? use the update(list, tuple, or set) function to add multiple items to a set
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)

# ? use the .remove(item) to remove specific item, error if not found
# * use .discard() for no error
# ? use the .pop() to remove a random item, returns removed item

st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()

# ? .clear() to clear the set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)

# ? use del to delete set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# ? use the set(list) function to convert list to set
# * good for when you want to remove duplicates from the list
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)

# ? can join a set using the .union(set), .update(), or | symbol
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits | vegetables)

# ? can use the & operand or .intersection() to find intersection items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2))
print(st1 & st2)

# ? use .issubset() or .issuperset() for subset or superset
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1)  # True
st1.issuperset(st2)  # True

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)  # False, because it is a super set
whole_numbers.issuperset(even_numbers)  # True

# ? use the .difference() or - symbol for difference
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1))
print(st1 - st2)

# ? use the .symmetric_difference() or the ^ symbol
# * all items in both sets that are not present in both
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.symmetric_difference(st1))
print(st2 ^ st1)

# ? use the .disjoint() function to check if no common items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1))

# Exercises
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f'Length of the it companies set {len(it_companies)}')

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Instagram', 'Meta', 'Dell'])
print(it_companies)

it_companies.pop()
print(it_companies)

# diff between remove and discard is that if you try to remove something thats not in the set there will be an error

C = A | B
print(C)

print(A & B)

print(A.issubset(B))

print(A.isdisjoint(B))

A = A.union(B)
B = B.union(A)

print(A ^ B)

del it_companies
del A
del B
del age
