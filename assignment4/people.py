user_0 = {'first_name': 'Wei', 'last_name': 'Wang', 'city': 'Kirkland', 'age': 18}
user_1 = {'first_name': 'Kong', 'last_name': 'Wu', 'city': 'Bellevue', 'age': 19}
user_2 = {'first_name': 'Xiao', 'last_name': 'Wu', 'city': 'Seattle', 'age': 20}
people = [user_0, user_1, user_2]

print ("method 1")
for user in people:
    print (user['first_name'] + " " + user['last_name'] + " is " + str(user['age']) + " years old, living at " + user['city'] + ".")

print ("\nmethod 2")
for user in people:
    for key, value in user.items():
        print (str(key) + ": " + str(value))
