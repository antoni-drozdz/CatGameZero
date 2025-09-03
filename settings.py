import json


class SettingsOptions:
    enable: bool
    volume: int

    def __init__(self, enable: bool, volume: float):
        self.enable = enable


class Settings:
    __settings_storage = 'settings.json'
    music: SettingsOptions
    sfx: SettingsOptions

    def __init__(self):
        self.music = SettingsOptions(True, 1)
        self.sfx = SettingsOptions(True, 1)
        self.read_settings()

    def read_settings(self):
        data = None
        with open(self.__settings_storage, 'r') as file:
            data = json.load(file)
        if data is not None:
            self.music.enable = data["music"]["enable"]
            self.music.volume = data["music"]["volume"]
            self.sfx.enable = data["sfx"]["enable"]
            self.sfx.volume = data["sfx"]["volume"]

    def save_settings(self):
        to_save = {
            "music": {
                "enable": True,
                "volume": 1,
            },
            "sfx": {
                "enable": True,
                "volume": 1,
            }
        }
        to_save["sfx"]["enable"] = self.sfx.enable
        to_save["sfx"]["volume"] = self.sfx.volume
        to_save["music"]["enable"] = self.music.enable
        to_save["music"]["volume"] = self.music.volume
        with open(self.__settings_storage, 'w') as file:
            json.dump(to_save, file)

    def sfx_vol(self):
        return self.sfx.volume / 10

    def music_volume(self):
        return self.music.volume / 10

    def __getitem__(self, item):
        return self.__dict__[item]
