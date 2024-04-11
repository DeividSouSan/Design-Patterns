from models.livro import Livro
from models.filme import Filme


class MediaFactory:
    """Classe Factory para a criação de midias. Aqui nós podemos criar uma classe sem que haja necessidade de explicitar no código o tipo, durante a criação (isso é dinâmico)."""
    def criarMidia(self, tipo: str, titulo: str, autor: str) -> object:
        midiasAceitadas = {
            "livro": Livro(autor, titulo),
            "filme": Filme(autor, titulo),
        }

        return midiasAceitadas[tipo]
