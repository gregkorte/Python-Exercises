my_family = {'sister': {'name': 'Krista', 'age': 42}, 'mother': {'name': 'Cathie', 'age': 70}}

my_family_str = {v['name'] + ' is my ' + k + ' and is ' + str(v['age']) + ' years old' for (k,v) in my_family.items()}

for string in my_family_str:
    print(string)