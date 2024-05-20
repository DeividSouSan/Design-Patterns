
from sort import Sort
from sort_strategy import FastSort, MediumSort, SlowSort


sort_method = input("Qual método de ordenação deseja utilizar? (fast, medium, slow): ")

# Essa parte poderia ter sido inserida dentro do método __init__ da classe Sort, mas para fins didáticos, foi mantida aqui.

match sort_method:
    case "fast":
        sort_algorithm = FastSort()
    case "medium":
        sort_algorithm = MediumSort()
    case "slow":
        sort_algorithm = SlowSort()
    case _:
        raise ValueError("Método de ordenação inválido")
    
sort = Sort(sort_algorithm, [1, 3, 2, 4, 5])
sort.sort()