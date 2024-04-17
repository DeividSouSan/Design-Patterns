from sort_strategy import SortStrategy

class Sort():
    def __init__(self, strategy: SortStrategy, array: list = []):
        self.array = array
        self.strategy = strategy
        
    def sort(self):
        self.strategy.sort(self.array)