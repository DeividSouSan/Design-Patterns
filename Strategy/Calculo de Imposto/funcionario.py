from enum import Enum
from calcula_imposto import CalculaImposto, CalculaImpostoQuinzeOuDez, CalculaImpostoVinteOuQuinze


class Cargo(Enum):
    DESENVOLVEDOR: int = 1
    GERENTE: int = 2
    DBA: int = 3


class Funcionario:
    def __init__(self, cargo: Cargo, salario_base: float):
        self.__cargo: Cargo = cargo
        self.__salario_base: float = salario_base
        self.__estrategia_de_calculo: CalculaImposto = self._definir_estrategia_de_calculo()

    def _definir_estrategia_de_calculo(self) -> CalculaImposto:
        match self.__cargo:
            case Cargo.DESENVOLVEDOR:
                return CalculaImpostoQuinzeOuDez()

            case Cargo.GERENTE:
                return CalculaImpostoQuinzeOuDez()

            case Cargo.DBA:
                return CalculaImpostoVinteOuQuinze()

            case _:
                raise Exception('Cargo especificado não existe.')

    def calcular_salario_com_imposto(self) -> float:
        return self.__estrategia_de_calculo.calcula_salario_com_imposto(self)

    def get_salario_base(self) -> float:
        return self.__salario_base
