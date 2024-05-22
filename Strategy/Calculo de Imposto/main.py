from funcionario import Funcionario, Cargo

class Main:
    def main() -> None:
        umFuncionario: Funcionario = Funcionario(Cargo.DESENVOLVEDOR, 2100.00)
        print(umFuncionario.calcular_salario_com_imposto())

        outroFuncionario: Funcionario = Funcionario(Cargo.DESENVOLVEDOR, 1700.00)
        print(outroFuncionario.calcular_salario_com_imposto())
    
if __name__ == '__main__':
    Main.main()