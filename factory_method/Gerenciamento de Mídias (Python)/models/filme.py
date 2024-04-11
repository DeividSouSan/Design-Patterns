from models.midia import Midia


class Filme(Midia):
    def showInfo(self) -> str:
        return f"Filme: {self.titulo}, Autor: {self.autor}"
