from abc import ABC, abstractmethod
from channels_iterator import ChannelIterator
from channel import Channel


class ChannelAggregator(ABC):
    def __init__(self):
        self._canais = []

    def count(self):
        return len(self._canais)

    def create_iterator(self):
        return ChannelIterator(self._canais)


class SportsChannel(ChannelAggregator):
    def __init__(self):
        super().__init__()

        self._canais = [Channel("Esporte ao Vivo"),
                        Channel('Fox Sports'),
                        Channel('Sportv'),
                        Channel('Campeonato Espanhol'),
                        Channel('Campeonato Brasileiro')]
