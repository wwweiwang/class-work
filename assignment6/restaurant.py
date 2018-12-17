# 9-6

class Restaurant():
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.restaurant_type + " restaurant.")

    def served(self):
        print("Today it served " + str(self.number_served) + " people.")


    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

    def number_served(self, number):
        self.served = number

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, restaurant_type, flavor):
        super().__init__(restaurant_name, restaurant_type)
        self.flavor = flavor

    def describe_flavor(self):
        print("The most popular flavor is " + self.flavor)

one_IceCreamStand = IceCreamStand('coldstone', 'icecream', 'cheesecake')
one_IceCreamStand.describe_restaurant()
one_IceCreamStand.open_restaurant()
one_IceCreamStand.describe_flavor()


        
