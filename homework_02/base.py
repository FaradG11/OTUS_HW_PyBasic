from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=1000, fuel=0, fuel_consumption=0.1):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if distance > self.fuel * self.fuel_consumption:
            raise LowFuelError
        else:
            self.fuel -= distance * self.fuel_consumption

