favorate_place = {
    'Wang': [1],
    'wu': [2, 3, 5],
    'kong': range(5),
    }
for name, places in favorate_place.items():
    print ("\n"+ name + "'s favorite number:")
    for place in places:
        print ("\t" + str(place))
