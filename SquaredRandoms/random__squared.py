import random

'''PART I'''
random_numbers = random.sample(range(0, 49), 20)
print('Twenty random numbers: ', random_numbers)

'''PART II'''
squares = [num**2 for num in random_numbers]
print('Those twenty numbers squared: ', squares)