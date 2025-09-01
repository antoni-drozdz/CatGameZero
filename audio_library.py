import pygame

from audio_type import AudioType


class AudioLibrary:
    def __init__(self, filename, audio_type=AudioType.MUSIC, loop=0, channel=0):
        self.filename = filename
        self.audio_type = audio_type
        self.loop = loop
        self.channel = channel

    def play(self):
        pygame.mixer.Channel(self.channel).play(Sound=pygame.mixer.Sound(self.filename), loops=self.loop)

    def mute(self):
        pygame.mixer.Channel(self.channel).stop()