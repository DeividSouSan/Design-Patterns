from abc import ABC, abstractmethod
from typing import override


class Carro(ABC):
    @abstractmethod
    def exibir_info(self) -> None:
        ...


class Palio(Carro):
    @override
    def exibir_info(self) -> None:
        print(f"Modelo: Palio - Ano: 2022")


class Fiesta(Carro):
    @override
    def exibir_info(self) -> None:
        print(f"Modelo: Fiesta - Ano: 2022")


class Gol(Carro):
    @override
    def exibir_info(self) -> None:
        print(f"Modelo: Gol - Ano: 2022")


class Celta(Carro):
    @override
    def exibir_info(self) -> None:
        print(f"Modelo: Celta - Ano: 2022")
