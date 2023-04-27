#Basic math and list comparing using packages.

from Mypackage.Shapes import *

s1 = sphere(4)
c1 = cube(4)
c1.volume()
s1.volume()

from Mypackage.Listpackage.listops import *

compare([1, 2, 3], [55, 66, 77])
merge([33, 44, 55], [55, 66, 77])
