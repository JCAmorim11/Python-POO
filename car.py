class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed
    def get_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = Car(200,'scarlet')
honda = Car(320, 'emerald')
audi = Car(400, 'silver')

# ford.speed = 200
# honda.speed = 200
# audi.speed = 200
#
ford.set_speed(300)
# honda.color = 'lavender'
# audi.color = 'green'
#
print(ford.get_speed())
print(ford.color)
