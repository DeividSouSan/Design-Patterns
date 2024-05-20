class RouteStrategy:
    def build_route(self, start, end):
        pass


class CarRouteStrategy(RouteStrategy):
    def build_route(self, start, end):
        print(f"Building car route from {start} to {end}")


class PublicTransportRouteStrategy(RouteStrategy):
    def build_route(self, start, end):
        print(f"Building public transport route from {start} to {end}")
