class Car:
    def __init__(self, factory):
        self.factory = factory

    def exibirInfo(self):
        print(f"Fabricante: {self.factory}")

class Palio(Car):
    def __init__(self):
        super().__init__("Fiat")

class Gol(Car):
    def __init__(self):
        super().__init__("Volkswagen")

class Celta(Car):
    def __init__(self):
        super().__init__("Chevrolet")

class Fiesta(Car):
    def __init__(self):
        super().__init__("Ford")