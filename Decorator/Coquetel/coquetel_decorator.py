from abc import ABC
from coquetel import Coquetel
from typing import override


class CoquetelDecorator(Coquetel, ABC):
    def __init__(self, coquetel: Coquetel):
        self.coquetel: Coquetel = coquetel

    @override
    @property
    def nome(self) -> str:
        return f"{self.coquetel.nome} {self._nome}"

    @override
    @property
    def preco(self) -> float:
        return self.coquetel.preco + self._preco


class Refrigerante(CoquetelDecorator):
    def __init__(self, coquetel: Coquetel):
        super().__init__(coquetel)

        self._nome = 'Refrigerante'
        self._preco = 1.0


class Limao(CoquetelDecorator):
    def __init__(self, coquetel: Coquetel):
        super().__init__(coquetel)

        self._nome = 'Limão'
        self._preco = 0.25
