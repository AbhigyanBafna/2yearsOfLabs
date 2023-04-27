#Basics of classes in python.

'''
Q1) Create an employee class and derive developer and manager classes from it. For developers define a new
attribute as developing language and for managers a list of their subordinates. Also define appropriate methods
for the same.
'''

class employee:
    bonus = 5000
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.email = fname + lname + "@gmail.com"
    
    def show(self):
        print(f"Name : {self.firstname} {self.lastname}")
        print(f"Age : {self.age}")
        print(f"MailID : {self.email}")
        print(f"Bonus : {employee.bonus}")

class developer(employee):
    def __init__(self, fname, lname, age, lang):
        super().__init__(fname, lname, age)
        self.lang = lang
    
    def show(self):
        print(f"Name : {self.firstname} {self.lastname}")
        print(f"Age : {self.age}")
        print(f"MailID : {self.email}")
        print(f"Bonus : {developer.bonus}")
        print(f"Language : {self.lang}")
        
    @classmethod
    def upbonus(cls):
        cls.bonus += 5000
        
class manager(employee):
    def __init__(self, fname, lname, age, subordinates):
        super().__init__(fname, lname, age)
        self.sub = subordinates
    
    def show(self):
        print(f"Name : {self.firstname} {self.lastname}")
        print(f"Age : {self.age}")
        print(f"MailID : {self.email}")
        print(f"Bonus : {manager.bonus}")
        print(f"Subordinates : {self.sub}")
        
    @classmethod
    def upbonus(cls):
        cls.bonus += 4000
        
    def upEmp(self, subordinates):
        self.sub = subordinates
        
        
emp1 = developer("Abhigyan", "Bafna", "20", "Python")
emp2 = manager("Abhigyan", "Bafna", "20", ["Huzefa", "Aditya", "Chaitanya"])
emp1.upbonus()
emp1.show()
emp2.upbonus()
emp2.upEmp(["Huzefa", "Aaditya", "Chaitanya", "Dhamne"])
emp2.show()

'''
Q2) Create class Vehicle with instance variables milage, max_speed and name. Derive classes bus and car from
it. Child classes override seating_capacity and fare method from the base class vehicle. Default seating capacity
for bus = 40, car = 3. Fare for vehicle is 20 times its capacity + 10% maintainence charges. Method vehicle_info
displays mileage, max_speed, seating_capacity and fare of the vehicle.
'''

class Vehicle:
    def __init__(self, mileage, max_speed, name):
        self.mileage = mileage
        self.max_speed = max_speed
        self.name = name

    def seating_capacity(self):
        pass

    def fare(self):
        return (self.seating_capacity() * 20)+ (self.seating_capacity() * 20 *0.1)

    def vehicle_info(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Mileage: {self.mileage}")
        print(f"Max Speed: {self.max_speed}")
        print(f"Seating Capacity: {self.seating_capacity()}")
        print(f"Fare: {self.fare()}")


class Bus(Vehicle):
    def __init__(self, mileage, max_speed, name):
        super().__init__(mileage, max_speed, name)

    def seating_capacity(self):
        return 40


class Car(Vehicle):
    def __init__(self, mileage, max_speed, name):
        super().__init__(mileage, max_speed, name)

    def seating_capacity(self):
        return 3


bus = Bus(10, 100, "Volvo")
car = Car(20, 120, "Toyota")

bus.vehicle_info()
car.vehicle_info()
