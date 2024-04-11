""" Classe Abstrata "Midia" que sugere o comportamento das classes filhas. """


class Midia:
    def __init__(self, autor: str, titulo: str):
        self.autor = autor
        self.titulo = titulo

    def showInfo(self) -> str:
        pass
