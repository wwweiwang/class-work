prompt = "\nWhat topping do you want? "
prompt += "\n(Enter 'quit' when you are finish.)"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print ("I will add the " + topping + " for you.")
    else:
        print ("Your pizza will be ready soon.")
        break
