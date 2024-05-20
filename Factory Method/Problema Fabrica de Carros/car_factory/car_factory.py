from car.car import *


class CarFactory():
    def create_car():
        pass


class FiatFactory(CarFactory):
    @staticmethod
    def create_car():
        return Palio()


class VolkswagenFactory(CarFactory):
    @staticmethod
    def create_car():
        return Gol()


class ChevroletFactory(CarFactory):
    @staticmethod
    def create_car():
        return Celta()


class FordFactory(CarFactory):
    @staticmethod
    def create_car():
        return Fiesta()
