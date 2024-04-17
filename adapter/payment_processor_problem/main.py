from payment_adapter import PaymentAdapter

payment = PaymentAdapter()
payment.execute(100)
payment.cancel(2)