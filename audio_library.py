import pygame
import json
from audio_type import AudioType


class AudioLibrary:
    def __init__(self, filename, audio_type=AudioType.MUSIC, loop=0, channel=0):
        self.filename = filename
        self.audio_type = audio_type
        self.loop = loop
        self.channel = channel

        with open('settings.json', 'r') as f:
            self.settings = json.load(f)

    def play(self):
        if self.audio_type == AudioType.MUSIC and self.settings["music"]["enable"]:
            pygame.mixer.Channel(self.channel).play(Sound=pygame.mixer.Sound(self.filename), loops=self.loop)
            pygame.mixer.Channel(self.channel).set_volume(self.__volume("music"))

        if self.audio_type == AudioType.SFX and self.settings["sfx"]["enable"]:
            pygame.mixer.Channel(self.channel).play(Sound=pygame.mixer.Sound(self.filename), loops=self.loop)
            pygame.mixer.Channel(self.channel).set_volume(self.__volume("sfx"))

    def mute(self):
        pygame.mixer.Channel(self.channel).stop()

    def __volume(self, scope):
        return self.settings[scope]["volume"] / 10