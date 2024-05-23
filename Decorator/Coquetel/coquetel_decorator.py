from abc import ABC
from coquetel import Coquetel
from typing import override

class CoquetelDecorator(Coquetel, ABC):
    def __init__(self, coquetel: Coquetel):
        self.coquetel: Coquetel = coquetel
            
    @override
    def get_nome(self) -> str:
        return f"{self.coquetel.get_nome()} {self.nome}"
    
    
    def get_preco(self) -> float:
        return self.coquetel.get_preco() + self.preco
    
class Refrigerante(CoquetelDecorator):
    def __init__(self, coquetel: Coquetel):
        super().__init__(coquetel)
        
        self.nome = 'Refrigerante'
        self.preco = 1.0
        
class Limao(CoquetelDecorator):
    def __init__(self, coquetel: Coquetel):
        super().__init__(coquetel)
        
        self.nome = 'Limão'
        self.preco = 0.25