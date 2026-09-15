# dictionaries

# ! unordered, mutable paird (key : value) data type

empty_dict = {}
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(len(dct))
print(len(person))

print(dct['key1'])
print(person['first_name'])

# ? error if the key does not exit use the .get() to avoid error

print(person.get('first_name'))

# ? adding to dictionary
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct['key5'] = 'value5'

person['job_title'] = 'Instructor'
print(person)

# ? modifying dictionary
dct['key1'] = 'value-one'
person['first_name'] = 'Eyob'
person['age'] = 252

# ? checking keys in a dictionary
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('key2' in dct)
print('key5' in dct)

# ? use .pop(key) to remove a specific key
# ? .popitem() removes the last item
# ? del removes an item with key name

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.pop('key1')
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.popitem()
del dct['key2']

# ? to change to list of tuples use .items()
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items())

# ? clear with .clear()
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.clear()
print(dct)

# ? use del to delete dictionary
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
del dct

# ? use .copy() to make a deep copy
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy()

# ? use .keys() to get a list of the keys
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
keys = dct.keys()
print(keys)

# ? use .values() to get values as a list
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
values = dct.values()
print(values)

# ! EXERCISES

dog = {}
dog['name'] = 'tokage'
dog['color'] = 'teal'
dog['breed'] = 'pug'
dog['legs'] = 4
dog['age'] = 5

student = {
    'first_name': 'Bob',
    'last_name': 'Yu',
    'gender': 'male',
    'age': 20,
    'marital_status': 'single',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country': 'United States of America',
    'city': 'Los Angeles',
    'address': '123 Bel Air'
}
print(len(student))
print(student.get('skills'))
print(type(student.get('skills')))

student['skills'].append('Java')
print(student.get('skills'))

print(student.keys())
print(student.values())

student_list = student.items()
print(student_list)

student.popitem()
student.pop('age')
del student['country']
print(student)
del student
