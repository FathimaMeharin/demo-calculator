class BaseClass:
    def __init__(self):
        print("Base init")

    def set_name(self,name):
        self.name = name
        print("baseclass setname")

class SubClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("subclass init")
    def set_name(self,name):
        super().set_name(name)
        print("subclass setname")
    def welcome(self):
        print("welcome")
    def display_name(self):
        print("name : "+self.name)


y = SubClass()
y.welcome()
y.set_name("muthu")
y.display_name()
