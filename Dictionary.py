my_dict = {}

my_dict = {1: 'mango', 2: 'ball'}

my_dict = {'name': 'Anaira', 1: [2, 8, 13]}

my_dict = {'name': 'Anaira', 'age': 11}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 12
print(my_dict)

my_dict['address'] = 'Springs'
print(my_dict)

my_dict.pop('age')
print(my_dict)
