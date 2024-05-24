from abc import ABC


class Coquetel(ABC):
    def __init__(self, nome: str, preco: float):
        self._nome: str = nome
        self._preco: float = preco

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def preco(self) -> float:
        return self._preco


class Cachaca(Coquetel):
    def __init__(self):
        super().__init__('Cachaça', 1.5)
