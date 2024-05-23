from playlist import PlayList
from modo_de_reproducao import ModoDeReproducao


class Main:
    def main() -> None:
        minha_playlist: PlayList = PlayList(ModoDeReproducao.porNome)

        minha_playlist.adicionar_musica("Everlong", "Foo Fighters", 1997, 5)
        minha_playlist.adicionar_musica("Song 2", "Blur", 1997, 4)
        minha_playlist.adicionar_musica(
            "American Jesus", "Bad Religion", 1993, 3)
        minha_playlist.adicionar_musica("No Cigar", "Milencollin", 2001, 2)
        minha_playlist.adicionar_musica("Ten", "Pearl Jam", 1991, 1)

        print("=== Lista por Nome de Musica ===")
        minha_playlist.mostrar_lista_de_reproducao()

        print("\n=== Lista por Autor ===")
        minha_playlist.set_modo_de_reproducao(ModoDeReproducao.porAutor)
        minha_playlist.mostrar_lista_de_reproducao()

        print("\n=== Lista por Ano ===")
        minha_playlist.set_modo_de_reproducao(ModoDeReproducao.porAno)
        minha_playlist.mostrar_lista_de_reproducao()

        print("\n=== Lista por Estrela ===")
        minha_playlist.set_modo_de_reproducao(ModoDeReproducao.porEstrela)
        minha_playlist.mostrar_lista_de_reproducao()


if __name__ == '__main__':
    Main.main()
