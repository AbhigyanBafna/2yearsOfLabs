class polygon:
    def __init__(self, nSides = 2):
        self.num_sides = nSides
        self.sides = [0] * nSides

    def set_sides(self):
        self.sides = [float(input("Enter Side : ")) for i in range(self.num_sides)]
        print(self.sides)

    def show_sides(self):
        print(self.sides)
        
    def area(self):
        area = 1
        for i in self.sides:
            area *= i
        print(area)



p1 = polygon()
p1.set_sides()
p1.show_sides()
p1.area()
