guest = ['wang', 'wu', 'kong']
message = guest[0].title() + ", would you like to come for dinner?"
print (message)
message1 = guest[1].title() + ", would you like to come for dinner?"
print (message1)
message2 = guest[2].title() + ", would you like to come for dinner?"
print (message2)

message3 = guest[2].title() + " cannot come."
print (message3)
guest[2] = 'deng'
print (message)
print (message1)
message4 = guest[2].title() + ", would you like to come for dinner?"
print (message4)

guest.insert(0, 'wei')
guest.insert(2, 'xiao')
guest.insert(5, 'xiu')
message5 = "I got a new table, " + guest[0].title() + ", would you like to come for dinner?"
message6 = "I got a new table, " + guest[1].title() + ", would you like to come for dinner?"
message7 = "I got a new table, " + guest[2].title() + ", would you like to come for dinner?"
message8 = "I got a new table, " + guest[3].title() + ", would you like to come for dinner?"
message9 = "I got a new table, " + guest[4].title() + ", would you like to come for dinner?"
message0 = "I got a new table, " + guest[5].title() + ", would you like to come for dinner?"
print (message5)
print (message6)
print (message7)
print (message8)
print (message9)
print (message0)

print ("Sorry, the new table doesn't work.")
popped_guest = guest.pop()
print ("Sorry, " + popped_guest.title() + ", cannot invite you this time.")
popped_guest = guest.pop()
print ("Sorry, " + popped_guest.title() + ", cannot invite you this time.")
popped_guest = guest.pop()
print ("Sorry, " + popped_guest.title() + ", cannot invite you this time.")
popped_guest = guest.pop()
print ("Sorry, " + popped_guest.title() + ", cannot invite you this time.")
mes0 = guest[0].title() + ", would you like to come for dinner?"
mes1 = guest[1].title() + ", would you like to come for dinner?"
print (mes0)
print (mes1)
del guest[0]
del guest[0]
print (guest)
