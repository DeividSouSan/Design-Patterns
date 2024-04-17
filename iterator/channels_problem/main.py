from channels_agregator import SportsChannel
from channel import Channel

my_channels = SportsChannel()
channel_iterator = my_channels.create_iterator()

print("- Iterando do primeiro ao último canal")
print("First channel: ", channel_iterator.get_current_channel())
channel_iterator.next()
print("Next channel: ", channel_iterator.get_current_channel())
channel_iterator.next()
print("Next channel: ", channel_iterator.get_current_channel())
channel_iterator.next()
print("Next channel: ", channel_iterator.get_current_channel())
channel_iterator.next()
print("Next channel: ", channel_iterator.get_current_channel(), end="\n\n")

print("- Iterando após o último canal")
channel_iterator.next()
print("Next channel: ", channel_iterator.get_current_channel())
channel_iterator.next()
print("Next channel: ", channel_iterator.get_current_channel(), end="\n\n")

print("- Iterando antes do primeiro canal")
channel_iterator.first()
print("First channel: ", channel_iterator.get_current_channel())
channel_iterator.previous()
print("Previous channel: ", channel_iterator.get_current_channel())

    