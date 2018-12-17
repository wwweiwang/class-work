# import user
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
