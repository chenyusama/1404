from random import randint
from prac_06.car import Car


class UnreliableCar(Car):

    def __int__(self, name, fuel, reliability):
        super().__int__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
