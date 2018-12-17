responses = {}
poll_active = True
while poll_active:
    name = input("Please enter your name: ")
    response = input ("Where do you want to go vacation? ")
    responses[name] = response

    repeat = input("Would you like to let another people answer the question? yes/no ")
    if repeat == 'no':
        poll_active = False

for name, response in responses.items():
    print (name.title() + " would like to go " + response + " for vacation.")
