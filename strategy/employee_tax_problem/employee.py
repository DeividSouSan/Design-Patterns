class Employee:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_tax(self, salary):
        return self.strategy.calculate_tax(salary)