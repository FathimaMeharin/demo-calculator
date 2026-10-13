class Cars:
    def __init__(self,name,colour,price):
        self.name = name
        self.colour = colour
        self.price = price
    def start(self):
        print(self.name + " engine started")
car1 = Cars("innova","white",100000)
car2 = Cars("maruti","red",50000)
car1.price = 150000
car2.price = 65000
del car1.colour
print(car1.name,car1.price)
print(car2.name,car2.colour,car2.price)
car1.start()
car2.start()


