import random
import pgzrun
import pygame

from audio_library import AudioLibrary
from audio_type import AudioType
from common import *
from static import WIDTH, HEIGHT, PLAYER_IMAGE_HEIGHT, PLAYER_IMAGE_WIDTH
from user_settings import UserSettings

user_settings = UserSettings()
sfx_library = {
    "pistol": AudioLibrary(filename='music/pistol.mp3', audio_type=AudioType.SFX, loop=0, channel=0),
    "mortar": AudioLibrary(filename='music/mortar.mp3', audio_type=AudioType.SFX, loop=0, channel=0),
    "reload": AudioLibrary(filename='music/gun_reload.mp3', audio_type=AudioType.SFX, loop=0, channel=0),
    "explosion": AudioLibrary(filename='music/explosion_fx_3.mp3', audio_type=AudioType.SFX, loop=0, channel=0),
}

music_library = {
    "main_theme": AudioLibrary(filename='music/pi-pi-pi-pi-bubu-bum2.mp3', channel=1, loop=-1)
}


def enemies_draw(enemies):
    for i in range (len(enemies)):
        enemies[i].draw()

def my_map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            if my_map[i][j] == 1:
                cell.left = j*size_w
                cell.top = i*size_h
                cell.draw()
            elif my_map[i][j] == 2:
                cell2.left = j*size_w
                cell2.top = i*size_h
                cell2.draw()
            elif my_map[i][j] == 3:
                spawn.left = j*size_w
                spawn.top = i*size_h
                spawn.draw()
            elif my_map[i][j] == 4:
                cell4.left = j * size_w
                cell4.top = i * size_h
                cell4.draw()
            elif my_map[i][j] == 5:
                cell5.left = j * size_w
                cell5.top = i * size_h
                cell5.draw()
                cells5.append(cell5)

def generate_enemies(mice_count: int = 6):
    mice = []

    while True:
        direction = random.randint(1, 4)

        if direction == 1:
            mouse_direction = 'mouse-up'
        elif direction == 2:
            mouse_direction = 'mouse-down'
        elif direction == 3:
            mouse_direction = 'mouse-left'
        elif direction == 4:
            mouse_direction = 'mouse-right'
        else:
            mouse_direction = None

        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)

        if mouse_direction is not None and not is_in_collision(x, y):
            mouse = pgzrun.mod.Actor(mouse_direction, (x, y))
            mice.append(mouse)
        if len(mice) == mice_count:
            break
    return mice

def is_in_collision(x, y):
    [player_position_x, player_position_y] = int(WIDTH / 2), int(HEIGHT / 2)
    margin_top = player_position_y - PLAYER_IMAGE_HEIGHT
    margin_bottom = player_position_y + PLAYER_IMAGE_HEIGHT
    margin_left = player_position_x - PLAYER_IMAGE_WIDTH
    margin_right = player_position_x + PLAYER_IMAGE_WIDTH

    collision_square = [
        range(margin_top, margin_bottom),
        range(margin_left, margin_right)
    ]

    return x in collision_square[0] or y in collision_square[0] or x in collision_square[1] or y in collision_square[1] or y in collision_square[1]


