'''
PART I
'''
showroom = set()
showroom.add('Nissan')
showroom.add('Mazda')
showroom.add('Hyundai')
showroom.add('Tesla')
print(len(showroom))
showroom.add('Mazda')
showroom.update(['Mitsubishi', 'McLaren'])
print(showroom)
showroom.discard('Hyundai')
print(showroom)

'''
PART II
'''
junkyard = set()
junkyard.add('Ford')
junkyard.add('Chevy')
junkyard.add('GM')
junkyard.add('Mitsubishi')
junkyard.add('Tesla')
dupes = set(showroom).intersection(junkyard)
print(dupes)
joined = set(showroom.union(junkyard))
print(joined)
joined.discard('GM')
joined.discard('Ford')
print(joined)