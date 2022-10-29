class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.___c = 30
    def public_method(self):
        print(self.___c)
        print(self.a)
        print('public')
        self.__private_method()
    def __private_method(self):
         print('private')

hell = Hello("vish")
#orint(hell.__c)
hell.public_method()
#hell.__private_method()