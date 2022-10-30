from Polygon import *
from shape import *

class Triangle(Polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height() / 2
