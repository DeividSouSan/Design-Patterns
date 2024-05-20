class PaymentService:
    def process_payment(self, amount: float) -> None:
        print(f"Processing R$ {amount} payment.")

    def cancel_payment(self, payment_id: int) -> None:
        print(f"Canceling payment with id {payment_id}.")
