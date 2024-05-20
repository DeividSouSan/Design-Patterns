from car_factory.car_factory import FiatFactory, VolkswagenFactory, ChevroletFactory, FordFactory

print("Escolha um carro para criar: ")
car = input("1 - Palio\n2 - Gol\n3 - Celta\n4 - Fiesta\n >> ")


car_factory = {
    "Palio": FiatFactory.create_car(),
    "Gol": VolkswagenFactory.create_car(),
    "Celta": ChevroletFactory.create_car(),
    "Fiesta": FordFactory.create_car()
}

car = car_factory[car]
car.exibirInfo()
