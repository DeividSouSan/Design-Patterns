from coquetel import Coquetel, Cachaca
from coquetel_decorator import CoquetelDecorator, Refrigerante, Limao

class Main:
    def main() -> None:
        meu_coquetel: Coquetel = Cachaca()
        print(f"{meu_coquetel.get_nome()} = {meu_coquetel.get_preco()}")
        
        meu_coquetel_decorado: CoquetelDecorator = Refrigerante(meu_coquetel)
        print(f"{meu_coquetel_decorado.get_nome()} = {meu_coquetel_decorado.get_preco()}")
        
        meu_coquetel_decorado = Limao(meu_coquetel_decorado)
        print(f"{meu_coquetel_decorado.get_nome()} = {meu_coquetel_decorado.get_preco()}")
        
        
if __name__ == "__main__":
    Main.main()