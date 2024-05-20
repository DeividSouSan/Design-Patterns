from abc import ABC, abstractmethod
from typing import override
from carro import *


class FabricaDeCarro(ABC):
    @abstractmethod
    def criar_carro(self) -> Carro:
        ...


class FabricaFiat(FabricaDeCarro):
    @override
    def criar_carro(self) -> Carro:
        return Palio()


class FabricaFord(FabricaDeCarro):
    @override
    def criar_carro(self) -> Carro:
        return Fiesta()


class FabricaWolks(FabricaDeCarro):
    @override
    def criar_carro(self) -> Carro:
        return Gol()


class FabricaChevrolet(FabricaDeCarro):
    @override
    def criar_carro(self) -> Carro:
        return Celta()
