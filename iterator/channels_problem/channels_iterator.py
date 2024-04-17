from channel import Channel


class ChannelIterator():
    def __init__(self, channels: list[Channel]) -> None:
        self.channels = channels
        self.index = 0

    def first(self) -> None:
        self.index = 0

    def next(self) -> None:
        self.index += 1

    def previous(self) -> None:
        self.index -= 1

    def is_done(self) -> bool:
        return self.index == len(self.channels)

    def _current_item(self) -> Channel:
        if self.is_done():
            self.index = len(self.channels) - 1
        elif self.index < 0:
            self.index = 0

        return self.channels[self.index]

    def get_current_channel(self) -> str:
        return self._current_item().name
