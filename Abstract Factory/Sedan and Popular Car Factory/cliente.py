from fabrica_de_carro import *
from carro_sedan import CarroSedan
from carro_popular import CarroPopular


def main() -> None:
    fabrica: FabricaDeCarro = FabricaFiat()

    sedan: CarroSedan = fabrica.criar_carro_sedan()
    popular: CarroPopular = fabrica.criar_carro_popular()

    sedan.exibir_info_sedan()
    popular.exibir_info_popular()

    fabrica = FabricaFord()

    sedan = fabrica.criar_carro_sedan()
    popular = fabrica.criar_carro_popular()

    sedan.exibir_info_sedan()
    popular.exibir_info_popular()


if __name__ == "__main__":
    main()
