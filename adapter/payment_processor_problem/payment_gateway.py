"""
Essa classe é a Interface do Cliente, que é a interface que o cliente espera que o Adaptee implemente. O cliente espera que o PaymentService tenha os métodos execute e cancel (o que não é verdade)
"""

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def execute(self, amount):
        pass

    @abstractmethod
    def cancel(self, payment_id):
        pass