class user():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def user_name(self):
        print("Current user is " + self.first_name + " " + self.last_name)


    def greeting(self):
        print("hello " + self.first_name + " " + self.last_name + "!")

class admin(user):
    def __init__(self, first_name, last_name, privileges=["can add post", "can delete post", "can ban user"]):
        super().__init__(first_name, last_name)
        self.admin_privilege = Privileges(privileges)

    def show_privileges(self):
        print(self.first_name + " privileges:")
        print(self.admin_privilege.get_privilieges())


class Privileges():
    privilieges = ["can add post", "can delete post", "can ban user"]

    def __init__(self, privileges):
        self.privilieges = privileges.copy()


    def get_privilieges(self):
        return self.privilieges


user1 = admin('Wei', 'Wang', ["can add post", "can delete post"])
user1.show_privileges()

user2 = admin('Xiao', 'Wu')
user2.show_privileges()
