class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    y_distance = 0
    _sound = 'i train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):

    def __init__(self):
        self.sound = super().sound
        self.sound = super()._sound

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
        return (self.x_distance, self.y_distance)


    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)
        return self.sound


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()