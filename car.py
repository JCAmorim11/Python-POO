class Car:
    def __init__(self, speed, color):
        print(speed)
        print(color)
        self.speed = speed;
        self.color = color;
        print('the init is called')

ford = Car(200,'scarlet')
honda = Car(320, 'emerald')
audi = Car(400, 'silver')

# ford.speed = 200
# honda.speed = 200
# audi.speed = 200
#
ford.color = 'blue'
# honda.color = 'lavender'
# audi.color = 'green'
#
# print(ford.speed)
# print(ford.color)
