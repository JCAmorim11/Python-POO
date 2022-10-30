from dir import myfunctions as mat


class Polygon:
    ___width = None
    ___height = None

    def set_values(self, width, height):
        self.___width = width
        self.___height = height

    def get_width(self):
        return self.___width

    def get_height(self):
        return self.___height


class Rectangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height()


class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() / 2


rec = Rectangle()
tri = Triangle()

rec.set_values(50, 40)
tri.set_values(30, 20)

print(rec.area())
print(tri.area())
print(mat.add(50, 10))
print(mat.mult(3,2))