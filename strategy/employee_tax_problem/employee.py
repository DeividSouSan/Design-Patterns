"""
Essa classe é o "contexto" do padrão Strategy, isto é, ela é responsável por receber e executar o algoritmo selecionado em tempo de execução.
"""

from tax_strategy import DeveloperTaxStrategy, TaxStrategy, DBATaxStrategy, ManagerTaxStrategy


class Employee:
    """
    Classe Contexto, ela é responsável por receber e executar o algoritmo selecionado em tempo de execução.
    """

    def __init__(self, role: str, salary: float):
        self.__salary = salary

        tax_strategy_mapper = {
            "developer": DeveloperTaxStrategy(),
            "dba": DBATaxStrategy(),
            "manager": ManagerTaxStrategy()
        }

        self.__strategy: TaxStrategy = tax_strategy_mapper[role]

    def salary_with_tax(self) -> float:
        return self.__strategy.calculate_tax(self.__salary)
