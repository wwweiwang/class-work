pet_0 = {'animal': 'cat', 'owner': 'Wang', 'city': 'Kirkland', 'age': 18}
pet_1 = {'animal': 'dog', 'owner': 'Wu', 'city': 'Bellevue', 'age': 19}
pet_2 = {'animal': 'bunny', 'owner': 'Wu', 'city': 'Seattle', 'age': 20}
pets = [pet_0, pet_1, pet_2]

print ("method 1")
for pet in pets:
    print (pet['animal'] + " " + pet['owner'] + " is " + str(pet['age']) + " years old, living at " + pet['city'] + ".")

print ("\nmethod 2")
for pet in pets:
    for key, value in pet.items():
        print (str(key) + ": " + str(value))
