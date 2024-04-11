class TaxStrategy:

    def calculate_tax(self, salary):
        pass


class DeveloperTaxStrategy(TaxStrategy):
    def calculate_tax(self, salary):
        print("Computing tax for developer")
        if salary > 2000:
            print("Salary is greater than 2000, applying 15% tax")
            return salary * 0.85
        else:
            print("Salary is greater than 2000, applying 10% tax")
            return salary * 0.9


class DBATaxStrategy(TaxStrategy):
    def calculate_tax(self, salary):
        print("Computing tax for dba")
        if salary > 2000:
            print("Salary is greater than 2000, applying 15% tax")
            return salary * 0.85
        else:
            print("Salary is greater than 2000, applying 10% tax")
            return salary * 0.9


class ManagerTaxStrategy(TaxStrategy):
    def calculate_tax(self, salary):
        print("Computing tax for manager")
        if salary > 3500:
            print("Salary is greater than 3500, applying 15% tax")
            return salary * 0.8
        else:
            print("Salary is greater than 3500, applying 10% tax")
            return salary * 0.85
