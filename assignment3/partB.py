cities = ['seattle', 'kirkland', 'bellevue']
print ("I have been to:")
for city in cities:
    print (city)
cities.append(input("Which city do you want to go?"))
print ("In the future, I will have been to:")
for city in cities:
    print (city)
