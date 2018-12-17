pizzas = ['pepperoni', 'cheese', 'combo', 'fruit', 'meat']
print (pizzas[0:3])
print (pizzas[1:4])
print (pizzas[-3:])

my_pizzas = pizzas[0:3]
friend_pizzas = my_pizzas[:]

my_pizzas.append('fruit')
friend_pizzas.append('meat')

print ("my favorate pizzas are:")
for my_pizza in my_pizzas:
    print (my_pizza)

print ("my friend's favorate pizzas are:")
for friend_pizza in friend_pizzas:
    print (friend_pizza)
