from abc import ABC, abstractmethod
from typing import override


class CarroSedan(ABC):
    @abstractmethod
    def exibir_info_sedan(self) -> None:
        ...


class Siena(CarroSedan):
    @override
    def exibir_info_sedan(self) -> None:
        print("Modelo: Siena - Fábrica: Fiat - Categoria: Sedan")


class FiestaSedan(CarroSedan):
    @override
    def exibir_info_sedan(self) -> None:
        print("Modelo: Fiesta Sedan - Fábrica: Ford - Categoria: Sedan")
