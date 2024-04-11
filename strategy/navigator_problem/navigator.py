class Navigator:
    def __init__(self, route_strategy):
        self.route_strategy = route_strategy
        
    def build_route(self, start, end):
        self.route_strategy.build_route(start, end)