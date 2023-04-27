#Vector Magnitude calculation using operator overloading.

'''
Q1) Overload comparision operators for comparing vectors.
'''

import math
ans = True

class vectors:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.v = [0 , 0]
        self.mod = 0

    def set_v(self):
        self.x = int(input("Enter X Coordinate: "))
        self.y = int(input("Enter Y Coordinate: "))
        self.v = [self.x, self. y]

    def get_v(self):
        print(f" {self.x}i + {self.y}j")
        
    def magnitude(self):
        self.mod = math.sqrt(sum(i**2 for i in self.v))
        print( math.sqrt(sum(i**2 for i in self.v)) )
        
    def __lt__(self, v2):
        if(self.mod < v2.mod):
            print(ans)
        else:
            print(not ans)
            
    def __gt__(self, v2):
        if(self.mod > v2.mod):
            print(ans)
        else:
            print(not ans)
    
    def __le__(self, v2):
        if(self.mod <= v2.mod):
            print(ans)
        else:
            print(not ans)
            
    def __ge__(self, v2):
        if(self.mod >= v2.mod):
            print(ans)
        else:
            print(not ans)
            
    def __eq__(self, v2):
        if(self.mod == v2.mod):
            print(ans)
        else:
            print(not ans)

v1 = vectors()
v1.set_v()
v1.get_v()
v1.magnitude()
v2 = vectors()
v2.set_v()
v2.get_v()
v2.magnitude()
v1 < v2
v1 > v2
v1 <= v2
v1 >= v2
v1 == v2