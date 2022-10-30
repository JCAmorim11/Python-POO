from dir import myfunctions as mat
from Rectangle import *
from Triangle import *

rec = Rectangle()
tri = Triangle()

rec.set_values(50, 40)
tri.set_values(30, 20)

rec.set_color('red')
tri.set_color("blue")
iiii
print(rec.area())
print(tri.area())
print(mat.add(50, 10))
print(mat.mult(3,2))
print(tri.get_color())
print(rec.get_color())