class Parent:
    def __init__(self):
        print('PARENT')

class Child(Parent):
    def __init__(self):
        print('child')

child = Child()