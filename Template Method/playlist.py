from muscia_mp3 import MusicaMP3
from ordenador_template import *
from modo_de_reproducao import ModoDeReproducao

class PlayList:
    def __init__(self, modo: ModoDeReproducao):
        self.musicas: list[MusicaMP3] = []
        self.ordernador: OrdenadorTemplate = self._define_ordenador(modo)
        
    def _define_ordenador(self, modo: ModoDeReproducao) -> OrdenadorTemplate:
        match modo:
            case ModoDeReproducao.porNome:
                self.ordenador = OrdenadorPorNome
                
            case ModoDeReproducao.porAutor:
                self.ordenador = OrdenadorPorAutor
                
            case ModoDeReproducao.porAno:
                self.ordenador = OrdenadorPorAno
                
            case ModoDeReproducao.porEstrela:
                self.ordenador = OrdenadorPorEstrela    
            
        return self.ordenador
    
    def set_modo_de_reproducao(self, modo: ModoDeReproducao) -> None:
        self.ordenador = self._define_ordenador(modo)
        
    def adicionar_musica(self, nome: str, autor: str, ano: int, estrela: int) -> None:
        musica: MusicaMP3 = MusicaMP3(nome, autor, ano, estrela)
        self.musicas.append(musica)
	
    def mostrar_lista_de_reproducao(self) -> None:
        nova_lista: list[MusicaMP3] = self.ordenador.ordenar_musica(self.musicas)
        
        for musica in nova_lista:
            print(f"{musica.nome}, {musica.autor}, {musica.ano}, {musica.estrelas}")