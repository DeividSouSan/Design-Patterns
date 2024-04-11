from models.midia import Midia


class Livro(Midia):
    def showInfo(self) -> str:
        return f"Livro: {self.titulo}, Autor: {self.autor}"
