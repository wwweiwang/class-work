prompt = "\nWhat topping do you want? "
prompt += "\n(Enter 'quit' when you are finish.)"

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
        print ("Your pizza will be ready soon.")
    else:
        print ("I will add the " + topping + " for you.")
