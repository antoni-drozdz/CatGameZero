import pygame
from audio_type import AudioType
from settings import Settings


class AudioLibrary:
    def __init__(self, settings: Settings, filename, audio_type=AudioType.MUSIC, loop=0, channel=0):
        self.filename = filename
        self.audio_type = audio_type
        self.loop = loop
        self.channel = channel
        self.settings = settings
        self.is_playing = False

    def play(self):
        if self.audio_type == AudioType.MUSIC and self.settings.music.enable:
            pygame.mixer.Channel(self.channel).play(Sound=pygame.mixer.Sound(self.filename), loops=self.loop)
            pygame.mixer.Channel(self.channel).set_volume(self.__volume(AudioType.MUSIC))
            self.is_playing = True

        if self.audio_type == AudioType.SFX and self.settings.sfx.enable:
            pygame.mixer.Channel(self.channel).play(Sound=pygame.mixer.Sound(self.filename), loops=self.loop)
            pygame.mixer.Channel(self.channel).set_volume(self.__volume(AudioType.SFX))

    def mute(self):
        pygame.mixer.Channel(self.channel).stop()

    def __volume(self, scope: AudioType):
        if scope == AudioType.MUSIC:
            return self.settings.music.volume / 10
        if scope == AudioType.SFX:
            return self.settings.sfx.volume / 10
        return 1

    def reload_settings(self):
        self.settings.read_settings()