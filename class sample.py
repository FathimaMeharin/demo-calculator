#class MySampleClass:
    #def hello(self,n):
        #self.name=n
    #def print_name(self):
       # print(self.name)
#x=MySampleClass()
#y=MySampleClass()
#name="chinju"
#x.hello(name)
#y.hello("muhtu")
#x.print_name()
#y.print_name()
#from function import name


class MySampleClass:
    year=2026
    def __init__(self,name,age,place):
      self.name = name
      self.age = age
      self.place = place

    def display(self):
      print("name : "+self.name)
      print("age : "+str(self.age))
      print("place : "+self.place)
      print("year :"+str(MySampleClass.year))

    @classmethod
    def add_year(cls):
         cls.year=cls.year+1

    def add_age(self):
        self.age = self.age+1
    def relocate(self,place):
        self.place = place


x=MySampleClass("meharin",23,"morayur")
y=MySampleClass("shameem",24,"ozhukur")

x.display()
y.display()
print("____________________")

MySampleClass.year=MySampleClass.year+1
x.add_age()
y.add_age()
x.relocate("Uae")
y.relocate("Uae")
x.display()
y.display()
print("____________________")

MySampleClass.add_year()
x.add_age()
y.add_age()
x.display()
y.display()




