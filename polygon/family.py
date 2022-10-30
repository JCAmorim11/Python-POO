class Parent:
    def __init__(self, name):
        print('PARENT', name)
class Parent2:
    def __init__(self, name):
        print('Parent2 oldy', name)
class Child(Parent2, Parent):
    def __init__(self):
        print('child')
        Parent.__init__(self,'max')
        Parent2.__init__(self,'stom')

child = Child()
print(Child.__mro__)