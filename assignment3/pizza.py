pizzas = ['pepperoni', 'cheese', 'combo']
for pizza in pizzas:
    print ("I like to eat a slice of " + pizza + "." )
print ("I really like pizza. \n")

# range
for value in range(1,21):
    print (value)

numbers = list(range(1,1000001))
print (min(numbers))
print (max(numbers))
print (sum(numbers))

print ("\nodd_number")
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print (odd_number)

print ("\nThrees")
threes = list(range(3,31,3))
for three in threes:
    print (three)

print ("\nCube")
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
    print (cube)
