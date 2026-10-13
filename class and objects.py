#class Student:
    #def __init__(self,name,age,course):
        #self.name = name
        #self.age = age
        #self.course = course
    #def display(self):
        #print("name :"+self.name)
        #print("age :"+str(self.age))
        #print("course :"+self.course)
#x = Student("shameem",25,"python")
#x.display()

#class Car:
    #def __init__(self,brand,model,price):
        #self.brand = brand
        #self.model = model
        #self.price = price
    #def display(self):
        #print("brand :"+self.brand)
        #print("model :"+self.model)
        #print("price :"+str(self.price))
#car1 = Car("Toyota","Camry",30000)
#car2 = Car("BMW","X5",60000)
#car1.display()
#car2.display()

#class Rectangle:
    #def __init__(self,length,width):
        #self.length = length
        #self.width = width
    #def area(self):
        #return self.length*self.width
    #def perimeter(self):
        #return 2*(self.length+self.width)
    #def display(self):
        #print("area :"+str(self.area()))
        #print("perimeter :"+str(self.perimeter()))
#x = Rectangle(10,5)
#x.display()

#class BankAccount:
    #def __init__(self,account_holder,balance):
        #self.account_holder = account_holder
        #self.balance = balance
    #def display(self):
        #print("account holder :"+self.account_holder)
        #print("balance :"+str(self.balance))
   # def deposite(self,amount):
        #self.balance += amount
        #print("deposited :"+str(amount))
    #def withdraw(self,amount):
        #self.balance -= amount
        #print("withdraw :"+str(amount))
    #def display_balance(self):
         #print("balance :"+str(self.balance))

#x = BankAccount("shameem",1000)
#x.display()
#x.deposite(500)
#x.withdraw(800)
#x.display_balance()


class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
class Car(Vehicle):
    def __init__(self,brand,speed,number_of_doors):
        super().__init__(brand,speed)
        self.number_of_doors = number_of_doors
    def display(self):
        print("brand :"+self.brand)
        print("speed :"+str(self.speed))
        print("number of doors :"+str(self.number_of_doors))
x = Car("BMW",500,2)
x.display()
