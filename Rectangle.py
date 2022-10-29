class Rectangle:
    def __init__(self, height, width):
        self.__heigth = height
        self.__width = width

    def set_height(self, height):
        self.__heigth = height
    def get_height(self):
        return self.__heigth
    def get_width(self):
        return self.__width
    def set_width(self, width):
        self.__width = width
    def area(self):
        return self.__width * self.__heigth


react = Rectangle(20, 300)
react2 = Rectangle(50, 80)

print(react.area())
print(react2.area())
