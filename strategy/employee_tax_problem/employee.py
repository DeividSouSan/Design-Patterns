"""
Essa classe é o "contexto" do padrão Strategy, isto é, ela é responsável por receber e executar o algoritmo selecionado em tempo de execução.
"""

from tax_strategy import TaxStrategy


class Employee:
    """
    Classe Contexto, ela é responsável por receber e executar o algoritmo selecionado em tempo de execução.
    """

    def __init__(self):
        self.__strategy: TaxStrategy = TaxStrategy()
        self.__salary: float = 0.0

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float) -> None:
        self.__salary = salary

    @property
    def strategy(self) -> TaxStrategy:
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy: TaxStrategy) -> None:
        self.__strategy = strategy

    def salary_with_tax(self) -> float:
        return self.strategy.calculate_tax(self.salary)
