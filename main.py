class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.___C = 30


hell = Hello("vish")


print(hell.a)
print(hell._b)
print(hell.__c)
