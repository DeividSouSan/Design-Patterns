"""
Essa classe contém o Adaptee ou Serviço que possui uma interface incompátivel com o cliente.
"""

class PaymentService:
    def process_payment(self, amount):
        print(f"Processing R$ {amount} payment.")

    def cancel_payment(self, payment_id):
        print(f"Canceling payment with id {payment_id}.")

