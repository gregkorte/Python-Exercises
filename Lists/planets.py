planet_list = ["Mercury", "Mars"]

'''
PART I
'''
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Neptune", "Uranus"])
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
planet_list.append("Pluto")
rocky_planets = planet_list[0:3:1]
rocky_planets.extend(planet_list[8:9:1])

print(planet_list)
print(rocky_planets)

del planet_list[8]
del rocky_planets[3]

print(planet_list)
print(rocky_planets)

'''
PART II
'''
spacecraft = [('Cassini', 'Jupiter'), ('Odyssey', 'Mars'), ('Juno', 'Jupiter'), ('Voyager 1', 'Uranus')]
for planet in planet_list:
  for craft in spacecraft:
    if craft[1] == planet:
      print(planet)