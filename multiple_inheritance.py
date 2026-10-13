class First:
    def display(self):
        print("hi")
class Second():
    def display(self):
        print("hello")
class Third(First,Second):
    def display_third(self):
        print("hey")

x = Third()
x.display_third()
x.display()
print(Third.mro())

