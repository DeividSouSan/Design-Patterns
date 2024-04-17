from abc import ABC, abstractmethod
from typing_extensions import override


class SortStrategy(ABC):
    """
    Classe Strategy, ela irá definir o padrão para as classes concretas que irão implementar o algoritmo de ordenação.
    """
    @abstractmethod
    def sort(self, array: list):
        pass


class FastSort():
    @override
    def sort(self, array: list):
        print("Sorting array using fast sort algorithm")


class MediumSort():
    @override
    def sort(self, array: list):
        print("Sorting array using medium sort algorithm")


class SlowSort():
    @override
    def sort(self, array: list):
        print("Sorting array using slow sort algorithm")
