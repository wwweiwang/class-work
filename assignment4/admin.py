usernames = ['admin', 'Wang', 'Wei', 'Xiao', 'Wu']
for username in usernames:
    if username == 'admin':
        print ("Hello Admin, would you like to see a status report?")
    else:
        print ("Hello " + username + ", thank you for logging in again.")

del usernames[0]
del usernames[0]
del usernames[0]
del usernames[0]
del usernames[0]

if username in usernames:
    for username in usernames:
        print ("Welcome!")
else:
    print ("We need to find some users.")

current_users = ['Kong', 'Wang', 'Wei', 'Xiao', 'Wu']
new_users =['Kong', 'Wang', 'Deng', 'Xiu', 'Hong']
for new_user in new_users:
    if new_user in current_users:
        print (new_user + ", please use an other name.")
    else:
        print (new_user + ", the name is available.")

numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print (str(number) + "st")
    elif number == 2:
        print (str(number) + "nd")
    else:
        print (str(number) + "st")
