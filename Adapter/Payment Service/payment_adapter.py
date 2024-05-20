from payment_interface import PaymentInterface
from payment_service import PaymentService


class PaymentAdapter(PaymentInterface):
    def __init__(self):
        self.payment_processor = PaymentService()

    def execute(self, amount: float) -> None:
        self.payment_processor.process_payment(amount)

    def cancel(self, payment_id: int) -> None:
        self.payment_processor.cancel_payment(payment_id)
