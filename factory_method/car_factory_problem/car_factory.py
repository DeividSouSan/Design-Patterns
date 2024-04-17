from abc import ABC, abstractmethod
from typing_extensions import override
from car import Car, Palio, Fiesta


class CarFactory(ABC):
    """
    Classe Factory, ela irá definir o padrão para as classes concretas que irão implementar a criação de carros.
    """
    @abstractmethod
    def create_car(self) -> Car:
        pass


class FiatFactory(CarFactory):
    @override
    def create_car(self) -> Car:
        return Palio()


class FordFactory(CarFactory):
    @override
    def create_car(self) -> Car:
        return Fiesta()
