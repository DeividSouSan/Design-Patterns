from __future__ import annotations

from abc import ABC, abstractmethod
from typing import override, TYPE_CHECKING

if TYPE_CHECKING:
    from funcionario import Funcionario


class CalculaImposto(ABC):
    @abstractmethod
    def calcula_salario_com_imposto(self, funcionario: Funcionario) -> float:
        ...


class CalculaImpostoQuinzeOuDez(CalculaImposto):
    @override
    def calcula_salario_com_imposto(self, funcionario) -> float:
        salario_base = funcionario.get_salario_base()

        if salario_base > 2000:
            return funcionario.get_salario_base() * 0.85

        return funcionario.get_salario_base() * 0.9


class CalculaImpostoVinteOuQuinze(CalculaImposto):
    @override
    def calcula_salario_com_imposto(self, funcionario) -> float:
        salario_base = funcionario.get_salario_base()

        if salario_base > 3500:
            return funcionario.get_salario_base() * 0.8

        return funcionario.get_salario_base() * 0.85
