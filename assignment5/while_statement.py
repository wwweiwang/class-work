#!/usr/bin/env python
# coding: utf-8

# In[9]:


# part B
message = input('Please enter your score (between 0-100): ')

score = int(message)
while 0 <= score <=100:
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 79:
        grade = "C"
    elif 60 <= score < 69:
        grade = "D"
    else:
        grade = "NC"
    print (grade)
    break


# In[10]:


# 7-1
message = input('Let me see if I can find you a: ')
print (message)


# In[11]:


# 7-2
message = input('How many are in your dinner group? ')
if int(message) > 8:
    print ("Please wait for a table.")
else:
    print ("Your table is ready.")


# In[12]:


# 7-3

message = input('Please type a number: ')
if int(message) % 10 == 0:
    print (message + " is a multiple of 10.")
else:
    print (message + " is not a multiple of 10.")


# In[13]:


# 7-4

prompt = "\nWhat topping do you want? "
prompt += "\n(Enter 'quit' when you are finish.)"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print ("I will add the " + topping + " for you.")
    else:
        print ("Your pizza will be ready soon.")
        break


# In[2]:


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


# In[14]:


# 7-6

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


# In[ ]:


# 7-7
prompt = "\nWhat topping do you want? "

while True:
    topping = input(prompt)
    print ("I will add the " + topping + " for you.")


# In[3]:


# 7-8
sandwich_orders = ['turkey', 'tofu', 'cheese']
sandwiches_finished = []

while sandwich_orders:
    sandwich_finished = sandwich_orders.pop()
    print ("I made your " + sandwich_finished + ' sandwich.')
    sandwiches_finished.append(sandwich_finished)
print ("\nThe following sandwiches have been made:")
for sandwich_finished in sandwiches_finished:
    print (sandwich_finished)


# In[4]:


# 7-9
sandwich_orders = ['turkey', 'pastrami', 'pastrami', 'tofu', 'pastrami', 'cheese']
print (sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print (sandwich_orders)


# In[5]:


# 7-10
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


# In[6]:


# 8-1 & 8-2
def display_message(chapter):
    print ("In " + chapter + ", I learnt Function.")

display_message('Chapter 8')

print ("\n")
def favorite_book(book):
    print ("One of my favorite book is " + book + " .")

favorite_book('Three bodies')


# In[7]:


# 8-3
def make_shirt(size, message):
    print ("\n Print " + message + " on size: " + size + ".")

make_shirt('Large', 'Dad')

make_shirt(size = 'Large', message = 'Dad')


# In[9]:


# 8-4
def make_shirt(size, message = 'I love Python'):
    print ("\n Print " + message + " on size: " + size + ".")

make_shirt('Large')
make_shirt('Medium')
make_shirt('small', 'I love R')


# In[11]:


# 8-5
def describe_city(city, country = 'USA'):
    print ("\n" + city + " is in " + country + ".")

describe_city('Seattle')
describe_city('Kirkland')
describe_city('Beijing', 'China')


# In[19]:


# 8-6

    
def location(city, country):
    return "\n" + city.title() + ", " + country.title()

print(location('seattle', 'USA'))
print(location('kirkland', 'USA'))
print(location('beijing', 'china'))


# In[4]:


# 8-7
def make_album(artist_name, album_title):
    albums = {'artist': artist_name, 'title': album_title}
    return albums

print(make_album('Cardi B', 'Invasion of Privacy'))
print(make_album('Kacey Musgraves', 'Golden Hour'))
print(make_album('Camila Cabello', 'Camila'))




    


# In[7]:


# 8-7
def make_album(artist_name, album_title, track_number=''):
    albums = {'artist': artist_name, 'title': album_title, 'track': track_number}
    if track_number:
        albums['track_number'] = track_number
    return albums

a = make_album('Cardi B', 'Invasion of Privacy')
print(a)
b = make_album('Kacey Musgraves', 'Golden Hour', '10')
print(b)


# In[4]:


# 8-8
def make_album(artist_name, album_title):
    albums = {'artist': artist_name, 'title': album_title}
    return albums

prompt1 = "\nPlease enter an artist name: "
prompt1 += "\nenter 'quit' when you are done."

prompt2 = "Please enter her/his album title: "
prompt2 += "\nenter 'quit' when you are done."

while True:
    user_name = input(prompt1)
    if user_name == 'quit':
        break
    user_title = input(prompt2)
    if user_title == 'quit':
        break
    else:
        user_albums = make_album(user_name, user_title)
        print(user_albums)


# In[6]:


# 8-9
def show_magicians(names):
    for name in names:
        print(name)
        

        
magicians = ['David Blaine', 'Lance Burton', 'Shin Lim', 'David Devant']
show_magicians(magicians)


# In[12]:


# 8-10

def show_magicians(names):
    for name in names:
        print(name)
        
def make_great(names, new_names):
    while names:
        current_name = names.pop()
        new_names.append("the Great " + current_name)
        
magicians = ['David Blaine', 'Lance Burton', 'Shin Lim', 'David Devant']
great_magicians = []

make_great(magicians, great_magicians)

show_magicians(magicians)
show_magicians(great_magicians)

print(magicians)
        


# In[19]:


# 8-11

def show_magicians(names):
    for name in names:
        print(name)
        
def make_great(names, new_names):
    while names:
        current_name = names.pop()
        new_names.append("the Great " + current_name)
        
magicians = ['David Blaine', 'Lance Burton', 'Shin Lim', 'David Devant']
great_magicians = []

make_great(magicians[:], great_magicians)

show_magicians(magicians)
print("\n")
show_magicians(great_magicians)
print("\n")
print(magicians)
        


# In[22]:


# 8-11
def sandwich(*topping):
    print(topping)

sandwich('turkey')
sandwich('turkey', 'tomato')
sandwich('turkey', 'tomato', 'cheese')


# In[25]:


# 8-12
def build_profile(first, last, **user_info):

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Wei', 'Wang',
                                location='Kirkland',
                                field='MSIM')
print(user_profile)


# In[26]:


# 8-13
def build_profile(manufacturer, model, **car_info):

    profile = {}
    profile['manufacturer_name'] = manufacturer
    profile['model_name'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car_profile = build_profile('VW', 'GTI',
                                color='black',
                                year='2015')
print(car_profile)


# In[27]:


import cars

car_profile = build_profile('VW', 'GTI',
                                color='black',
                                year='2015')
print(car_profile)


# In[ ]:


import magician.show_magicians()
import magician.make_great() as great()
import cars as cars_profile 

