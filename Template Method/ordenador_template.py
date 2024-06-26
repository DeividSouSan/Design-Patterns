from abc import ABC, abstractmethod
from muscia_mp3 import MusicaMP3
from typing import override
from copy import copy


class OrdenadorTemplate(ABC):
    @abstractmethod
    def eh_primeiro(self, musica_1: MusicaMP3, musica_2: MusicaMP3) -> bool:
        ...

    @classmethod
    def ordenar_musica(cls, lista: list[MusicaMP3]) -> list[MusicaMP3]:
        nova_lista: list[MusicaMP3] = copy(lista)  # ou lista[:]

        for i in range(len(nova_lista)):
            for j in range(i + 1, len(nova_lista)):
                if not cls.eh_primeiro(cls, nova_lista[i], nova_lista[j]):
                    nova_lista[j], nova_lista[i] = nova_lista[i], nova_lista[j]

        return nova_lista


class OrdenadorPorNome(OrdenadorTemplate):
    @override
    def eh_primeiro(self, musica_1: MusicaMP3, musica_2: MusicaMP3) -> bool:
        return musica_1.nome <= musica_2.nome


class OrdenadorPorAutor(OrdenadorTemplate):
    @override
    def eh_primeiro(self, musica_1: MusicaMP3, musica_2: MusicaMP3) -> bool:
        return musica_1.autor <= musica_2.autor


class OrdenadorPorAno(OrdenadorTemplate):
    @override
    def eh_primeiro(self, musica_1: MusicaMP3, musica_2: MusicaMP3) -> bool:
        return musica_1.ano - musica_2.ano <= 0


class OrdenadorPorEstrela(OrdenadorTemplate):
    @override
    def eh_primeiro(self, musica_1: MusicaMP3, musica_2: MusicaMP3) -> bool:
        return musica_1.estrelas <= musica_2.estrelas
