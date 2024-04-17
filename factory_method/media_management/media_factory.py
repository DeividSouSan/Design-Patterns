from media import Book, Movie

class MediaFactory:
    """Classe Factory para a criação de midias. Aqui nós podemos criar uma classe sem que haja necessidade de explicitar no código o tipo, durante a criação (isso é dinâmico)."""
    def create_media(self, kind: str, title: str, author: str) -> object:
        accepted_medias = {
            "livro": Book(author, title),
            "filme": Movie(author, title),
        }

        return accepted_medias[kind]
