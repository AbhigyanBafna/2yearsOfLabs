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
        print(f"Updated bonus = {developer.bonus}")
        
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
        cls.bonus += 5000
        print(f"Updated bonus = {manager.bonus}")
        
    @staticmethod
    def upEmp(self, subordinates):
        self.sub = subordinates
        print(f"Updated Subordinates = {self.sub}")
        
        
emp1 = developer("Abhigyan", "Bafna", "20", "Python")
emp2 = manager("Abhigyan", "Bafna", "20", ["Huzefa", "Aditya", "Chaitanya"])
emp1.show()
emp1.upbonus()
emp1.show()
emp2.show()
emp2.upbonus()
emp2.upEmp(["Huzefa", "Aaditya", "Chaitanya", "Dhamne"])
emp2.show()