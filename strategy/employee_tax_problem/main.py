"""
Esse arquivo existem com o intuito de centralizar a execução do código, isto é, ele é responsável por capturar as informações do usuário em tempo de execução e executar o algoritmo selecionado.
"""


from employee import Employee
from tax_strategy import *

# Capturando informações do usuário em tempo de execução
role = input("Choose your role: developer, dba or manager: ")
salary = float(input("Enter your salary:"))

# Criando o contexto no qual o algoritmo selecionado será executado
employee = Employee(role, salary)
print(employee.salary_with_tax())
