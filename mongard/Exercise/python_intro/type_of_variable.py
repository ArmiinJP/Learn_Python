
class Car():
    wheel = 4
    car_counter = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price

        Car.car_counter += 1
    
    def show(self):
        print(f'car: {self.name}, price is: {self.price}, wheel is: {self.wheel}')
    


c1 = Car("benz", 2000)
c2 = Car("pride", 100)
print("-------------------------------------------")
print(f'number of car is : {Car.car_counter}')
print("-------------------------------------------")


c1.show()
print(c1.__dict__)
c2.show()
print(c2.__dict__)
print(Car.__dict__["wheel"])

print("-------------------------------------------")
#-----------
c2.wheel = 3
#-----------
c1.show()
print(c1.__dict__)
c2.show()
print(c2.__dict__)
print(Car.__dict__["wheel"])

print("-------------------------------------------")
#-----------
Car.wheel = 5
#-----------
c1.show()
print(c1.__dict__) 
c2.show()
print(c2.__dict__)
print(Car.__dict__["wheel"])

