

from employee import Employee
from tax_strategy import *

# Capturando o cargo do usuário em tempo de execução
role = input("Choose your role: developer, dba or manager: ")

# Capturando o salário do usuário em tempo de execução
salary = float(input("Enter your salary:"))

# Criando um dicionário com as estratégias de imposto
tax_strategy = {
    "developer": DeveloperTaxStrategy,
    "dba": DBATaxStrategy,
    "manager": ManagerTaxStrategy
}

choosen_tax = tax_strategy[role]()

employee = Employee(choosen_tax)
salary_after_tax = employee.calculate_tax(salary)

print(f"Salary after tax: {salary_after_tax}")