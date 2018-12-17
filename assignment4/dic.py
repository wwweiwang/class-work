user_0 = {'first_name': 'Wei', 'last_name': 'Wang', 'city': 'Kirkland', 'age': 18}
print (user_0)

favorite_numbers = {'Kong': '2', 'Wang': '1', 'Wei': '3', 'Xiao': '4', 'Wu': '5'}
for name, number in favorite_numbers.items():
    print (name + "'s favorite number is " + number + ".")

print ("\nGlossary")
glossary = {'str': 'string', 'int': 'integar', 'len': 'length', 'del': 'delete'}

glossary['elif'] = 'else if'


for code, meaning in glossary.items():
    print (code + ": " + meaning + ".\n")

major_rivers = {'Nile': 'egypt', 'huanghe': 'china', 'amazon': 'usa'}
for river, coutry in major_rivers.items():
    print ("The" + river.title() + "runs through " + coutry + " .")
for river, coutry in major_rivers.items():
    print (river)
for river, coutry in major_rivers.items():
    print (coutry)
