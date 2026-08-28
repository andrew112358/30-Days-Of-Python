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

# ? use insert(index, item)
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

# ? use the .count(item) to count items in list
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# ? .index(item) returns the index of first occurence
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

# ? .reverse() to reverse a list
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# ? use the .sort() function to sort ascending order
# ? .sort(reverse=True) to sort descending order
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

# ! Exercises
empty_list = list()
list1 = [1, 2, 3, 4, 5]
print(len(list1))

print('first: ', list1[0], 'middle: ', list1[len(
    list1) // 2], 'last: ', list1[len(list1) - 1])

mixed_data_types = ['Andrew', 19, 70, 'taken', '123 inter state']
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', "Oracle", 'Amazon']
print(it_companies)
print(len(it_companies))
print('first: ', it_companies[0], 'middle: ', it_companies[len(
    it_companies) // 2], 'last: ', it_companies[len(it_companies) - 1])
it_companies[1] = 'Xiaomi'
print(it_companies)
it_companies.append('Samsung')
it_companies.insert(len(it_companies) // 2, 'logitech')
it_companies[0] = it_companies[0].upper()
print(it_companies)

companies = '#; '.join(it_companies)
print(companies)

print('is Microsoft in the list of it companies: ', 'Microsoft' in it_companies)
it_companies.sort()
it_companies.reverse()
print(it_companies)

slice_first_three = it_companies[3:]
print(slice_first_three)
slice_last_three = it_companies[0:len(it_companies) - 3]
print(slice_last_three)
slice_middle = it_companies[0:len(
    it_companies) // 2] + it_companies[(len(it_companies) // 2 + 1):]
print(slice_middle)
remove_first = it_companies.pop(0)
remove_middle = it_companies.pop(len(it_companies) // 2)
remove_last = it_companies.pop()
remove_all = it_companies.clear()
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_and_back_end = front_end + back_end
full_stack = front_and_back_end.copy()
index_of_redux = full_stack.index('Redux')
full_stack.insert(index_of_redux + 1, 'Python')
full_stack.insert(index_of_redux + 2, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = ages[0]
max = ages[len(ages) - 1]
ages.extend([min, max])

ages.sort()
median = (ages[len(ages) // 2] + ages[len(ages) // 2 + 1]) // 2

sum = 0
for i in ages:
    sum += i
average = sum / len(ages)

range = max - min

countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo, Democratic Republic of the',
    'Congo, Republic of the',
    'Costa Rica',
    "Côte d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor-Leste)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syria',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe'
]

country_list_length = len(countries)
middle_country = countries[country_list_length // 2]
print(middle_country)

first_half_of_countries = countries[0:country_list_length // 2]
last_half_of_countries = countries[country_list_length // 2 + 1:]

some_countries = ['China', 'Russia', 'USA',
                  'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic = some_countries
print(first)
print(second)
print(third)
print(scandic)
