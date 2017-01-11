'''
PART I
'''
zoo = ('Panda', 'Tiger', 'Monkey')

'''
PART II
'''
print(zoo.index('Tiger'))

'''
PART III
'''
for animal in zoo:
    if animal == 'Panda':
        print('There is a panda at my zoo!')
    else:
        print('There is no panda...')

'''
PART IV
'''
(panda, tiger, monkey) = zoo
print(panda)
print(tiger)
print(monkey)

'''
PART V
'''
zoo = list(zoo)
print(zoo)

'''
PART VI
'''
zoo.extend(['Mantis'])
zoo.extend(['Crane'])
zoo.extend(['Tortoise'])
print(zoo)

'''
PART VII
'''
zoo = tuple(zoo)
print(zoo)