from abc import ABC, abstractmethod
 
class shape(ABC):
    
    @abstractmethod
    def volume():
        pass
   
class sphere(shape):
    def __init__(self, radius):
        self.r = radius
    
    def volume(self):
        self.vol = (4/3)*3.14*self.r**2
        print(self.vol)

class cube(shape):
    def __init__(self, side):
        self.s = side
    
    def volume(self):
        self.vol = self.s**3
        print(self.vol)
    
