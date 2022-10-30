from Polygon import *
from shape import *

class Rectangle(Polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height()
