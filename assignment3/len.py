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
print (len (guest))
