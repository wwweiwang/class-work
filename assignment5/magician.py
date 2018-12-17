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
