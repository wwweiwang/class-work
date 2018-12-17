alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print ("You earned 5 points!")
if 'red' in alien_color:
    print ("You earned 5 points!")
if 'yellow' in alien_color:
    print ("You earned 5 points!")

if alien_color == 'green':
    print ("You earned 5 points for shooting the alien！")
elif alien_color == 'yellow':
    print ("You earned 10 points!")
else:
    print ("You earned 15 points!")

alien_color = 'green'

if alien_color == 'green':
    print ("You earned 5 points for shooting the alien！")
elif alien_color:
    print ("You earned 10 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print ("You earned 5 points for shooting the alien！")
elif alien_color != 'green':
    print ("You earned 10 points!")

alien_color = 'green'
if alien_color == 'green':
    print ("You earned 5 points！")
elif alien_color == 'yellow':
    print ("You earned 10 points!")
else:
    print ("You earned 15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print ("You earned 5 points！")
elif alien_color == 'yellow':
    print ("You earned 10 points!")
else:
    print ("You earned 15 points!")

alien_color = 'red'
if alien_color == 'green':
    print ("You earned 5 points！")
elif alien_color == 'yellow':
    print ("You earned 10 points!")
else:
    print ("You earned 15 points!")
