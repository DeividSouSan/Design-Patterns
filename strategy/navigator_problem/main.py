from navigator import Navigator
from route_strategy import  CarRouteStrategy, PublicTransportRouteStrategy

# Capturando a escolha do usuário em tempo de execução
route = input("Choose your route: car or public transport: ")

# Criando um dicionário com as estratégias de rota
route_strategy = {
    "car": CarRouteStrategy,
    "public transport": PublicTransportRouteStrategy
}

# Escolhendo a estratégia de rota
choosen_route = route_strategy[route]()

# Instanciando o navegador com a estratégia de rota escolhida
navigator = Navigator(choosen_route)

# Construindo a rota
navigator.build_route("A", "B")