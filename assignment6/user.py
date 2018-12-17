class user():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def user_name(self):
        print("Current user is " + self.first_name + " " + self.last_name)


    def greeting(self):
        print("hello " + self.first_name + " " + self.last_name + "!")
