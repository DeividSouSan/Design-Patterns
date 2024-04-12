"""
Essa classe é o "strategy" do padrão Strategy, isto é, ela é responsável por implementar cada algoritmo do cálculo de imposto em uma classe distinta que implementa uma interface ou estende uma classe abstrata.
"""

from abc import ABC, abstractmethod

class TaxStrategy(ABC):
    """
    Classe Strategy, ela irá definir o padrão para as classes concretas que irão implementar o algoritmo de cálculo de imposto para cada tipo de cargo.
    """
    @abstractmethod
    def calculate_tax(self, salary):
        pass


class DeveloperTaxStrategy(TaxStrategy):
    def calculate_tax(self, salary):
        print("Computing tax for developer")
        if salary > 2000:
            print("Salary is greater than 2000, applying 15% tax")
            return salary * 0.85
        else:
            print("Salary is smaller than 2000, applying 10% tax")
            return salary * 0.9


class DBATaxStrategy(TaxStrategy):
    def calculate_tax(self, salary):
        print("Computing tax for dba")
        if salary > 2000:
            print("Salary is greater than 2000, applying 15% tax")
            return salary * 0.85
        else:
            print("Salary is smaller than 2000, applying 10% tax")
            return salary * 0.9


class ManagerTaxStrategy(TaxStrategy):
    def calculate_tax(self, salary):
        print("Computing tax for manager")
        if salary > 3500:
            print("Salary is greater than 3500, applying 15% tax")
            return salary * 0.8
        else:
            print("Salary is smaller than 3500, applying 10% tax")
            return salary * 0.85
