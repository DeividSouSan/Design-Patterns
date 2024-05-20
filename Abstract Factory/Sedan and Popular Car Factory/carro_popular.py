from abc import ABC, abstractmethod
from typing import override


class CarroPopular(ABC):
    @abstractmethod
    def exibir_info_popular(self) -> None:
        ...


class Palio(CarroPopular):
    @override
    def exibir_info_popular(self) -> None:
        print("Modelo: Palio - Fábrica: Fiat - Categoria: Popular")


class Fiesta(CarroPopular):
    @override
    def exibir_info_popular(self) -> None:
        print("Modelo: Fiesta - Fábrica: Ford - Categoria: Popular")
