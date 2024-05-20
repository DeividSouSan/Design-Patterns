from carro import *
from fabrica_de_carro import *


def main() -> None:
    fabrica: FabricaDeCarro = FabricaFiat()
    carro: Carro = fabrica.criar_carro()
    carro.exibir_info()

    fabrica = FabricaFord()
    carro = fabrica.criar_carro()
    carro.exibir_info()

    fabrica = FabricaWolks()
    carro = fabrica.criar_carro()
    carro.exibir_info()

    fabrica = FabricaChevrolet()
    carro = fabrica.criar_carro()
    carro.exibir_info()


if __name__ == "__main__":
    main()
