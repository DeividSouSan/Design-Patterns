from abc import ABC


class Coquetel(ABC):
    def __init__(self, nome: str, preco: float):
        self.nome: str = nome
        self.preco: float = preco

    def get_nome(self) -> str:
        return self.nome

    def get_preco(self) -> float:
        return self.preco


class Cachaca(Coquetel):
    def __init__(self):
        super().__init__('Cachaça', 1.5)
