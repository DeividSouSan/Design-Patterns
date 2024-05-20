from abc import ABC, abstractmethod
from carro_sedan import CarroSedan, Siena, FiestaSedan
from carro_popular import CarroPopular, Palio, Fiesta
from typing import override


class FabricaDeCarro(ABC):
    @abstractmethod
    def criar_carro_sedan(self) -> CarroSedan:
        ...

    @abstractmethod
    def criar_carro_sedan(self) -> CarroSedan:
        ...


class FabricaFiat(FabricaDeCarro):
    @override
    def criar_carro_sedan(self) -> CarroSedan:
        return Siena()

    @override
    def criar_carro_popular(self) -> CarroPopular:
        return Palio()


class FabricaFord(FabricaDeCarro):
    @override
    def criar_carro_sedan(self) -> CarroSedan:
        return FiestaSedan()

    @override
    def criar_carro_popular(self) -> CarroPopular:
        return Fiesta()
