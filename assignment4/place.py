favorate_place = {
    'Wang': ['Kirkland'],
    'wu': ['Seattle', 'Bellevue'],
    'kong': ['samammish', 'Issaquah', 'Snoqualmie'],
    }
for name, places in favorate_place.items():
    print ("\n"+ name + "'s favorite place:")
    for place in places:
        print ("\t" + place.title() )
