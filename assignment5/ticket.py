# 7-5

prompt = "\nHow old are you? "
prompt += "\n(Enter 'quit' when you are finish.)"

while True:
    age = input(prompt)
    if age == 'quit':
        print ("Enjoy your movie!")
        break
    if int(age) < 3:
        print ("Your ticket is free.")
    elif 3 <= int(age) < 12:
        print ("Your ticket price is $10.")
    else:
        print ("Your ticket price is $15.")
