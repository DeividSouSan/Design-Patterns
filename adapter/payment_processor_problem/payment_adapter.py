"""
Essa classe é o Adapter que adapta a interface do Adaptee (Serviço) para a interface que o cliente espera. Note que, geralmente, para cada serviço que precisamos adaptar, criamos um Adapter específico.
"""

from payment_gateway import PaymentGateway
from payment_service import PaymentService

class PaymentAdapter(PaymentGateway):
    def __init__(self):
        self.payment_processor = PaymentService()

    def execute(self, amount):
        self.payment_processor.process_payment(amount)
        
    def cancel(self, amount):
        self.payment_processor.cancel_payment(amount)