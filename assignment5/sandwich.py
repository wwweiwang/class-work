sandwich_orders = ['turkey', 'tofu', 'cheese']
sandwiches_finished = []

while sandwich_orders:
    sandwich_finished = sandwich_orders.pop()
    print ("I made your " + sandwich_finished + ' sandwich.')
    sandwiches_finished.append(sandwich_finished)
print ("\nThe following sandwiches have been made:")
for sandwich_finished in sandwiches_finished:
    print (sandwich_finished)
