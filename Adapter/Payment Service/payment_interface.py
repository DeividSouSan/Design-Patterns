from abc import ABC, abstractmethod


class PaymentInterface(ABC):
    @abstractmethod
    def execute(self, amount: float) -> None:
        ...

    @abstractmethod
    def cancel(self, payment_id: int) -> None:
        pass
