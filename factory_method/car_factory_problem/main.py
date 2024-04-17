from car_factory import FiatFactory, FordFactory

factory = FiatFactory()
car = factory.create_car()
car.show_info()

factory = FordFactory()
car = factory.create_car()
car.show_info()
