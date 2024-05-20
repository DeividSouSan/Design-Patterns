from payment_adapter import PaymentAdapter
from payment_interface import PaymentInterface
from payment_service import PaymentService


def main() -> None:
    # payment: PaymentInterface = PaymentService()
    # faria com que o execute() e cancel() gerasse, erro.
    payment: PaymentInterface = PaymentAdapter()

    payment.execute(100.00)
    payment.cancel(2)


if __name__ == "__main__":
    main()
