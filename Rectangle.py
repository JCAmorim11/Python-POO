class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width


react = Rectangle(20, 300)
react2 = Rectangle(50, 80)

react.height = 20
react2.height = 30

react.width = 100
react2.width = 450
