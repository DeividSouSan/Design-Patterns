""" Classe Abstrata "Midia" que sugere o comportamento das classes filhas. """

from abc import ABC, abstractmethod
from typing_extensions import override


class Media(ABC):
    def __init__(self, autor: str, titulo: str):
        self.autor = autor
        self.titulo = titulo

    @abstractmethod
    def show_info(self) -> str:
        pass


class Book(Media):
    @override
    def show_info(self) -> str:
        return f"Livro: {self.titulo}, Autor: {self.autor}"


class Movie(Media):
    @override
    def show_info(self) -> str:
        return f"Filme: {self.titulo}, Autor: {self.autor}"
