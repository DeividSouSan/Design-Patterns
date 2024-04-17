from abc import ABC, abstractmethod
from typing_extensions import override

class Car:
    @abstractmethod
    def show_info(self):
        pass
        
class Palio(Car):
    @override
    def show_info(self):
        print(f"Model: Palio, Year: 2022")

class Fiesta(Car):
    @override
    def show_info(self):
        print(f"Model: Fiesta, Year: 2022")