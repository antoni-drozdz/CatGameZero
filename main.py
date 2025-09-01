import random
import pgzrun

import helpers
from static import *

play = pgzrun.mod.Actor('gra', (WIDTH / 2, HEIGHT / 2))

#Sterowanie od mode = "instr..."
instruction = pgzrun.mod.Actor('gra', (512, 580))
instruction_1 = pgzrun.mod.Actor('wsad', (300, 200))
instruction_2 = pgzrun.mod.Actor('spacet1', (300, 300))
instruction_3 = pgzrun.mod.Actor('shift1', (300, 400))
instruction_4 = pgzrun.mod.Actor('esc1', (300, 100))

settings = pgzrun.mod.Actor('gra', (512, 650))
cross = pgzrun.mod.Actor('cross', (1000, 30))

settings_m = pgzrun.mod.Actor('gra', (WIDTH / 2, HEIGHT / 2))

player = pgzrun.mod.Actor('cat', (WIDTH / 2, HEIGHT / 2))

bomb = pgzrun.mod.Actor('bomb', (random.randint(0,1024),random.randint(0, 1024)))
add_ammo = pgzrun.mod.Actor('amunicion', (1009,-60))
enemies = helpers.generate_enemies(ENEMIES_COUNT)
helpers.music_library["main_theme"].play()

pelets = []

def boom():
    global bomb
    if bomb.image == 'explosion':
        bomb.image = 'after-explosion'

def draw():
    if mode == 'menu':
        helpers.my_map_draw()
        if LEVEL < 5:
            helpers.my_map_draw()
            play.draw()
            instruction.draw()
            settings.draw()
            screen.draw.text('Level: ' + str(LEVEL), pos=(15, 15), color='white', fontsize=40)
            screen.draw.text('Kampania', center=(WIDTH / 2, HEIGHT / 2), color='white', fontsize=50)
            screen.draw.text('Sterowanie', center=(512, 580), color='white', fontsize=50)
            screen.draw.text('Ustawienia\n(Uwaga wersja testowa)', center=(512, 650), color='white', fontsize=50)
        elif LEVEL > 5:
            helpers.my_map_draw()
            screen.draw.text('Dzienkuję za zagranię w wersje\n testową gry "CatGameZero"', center=(WIDTH / 2, HEIGHT / 2), color='white', fontsize=55)
    elif mode == 'instr...':
        helpers.my_map_draw()
        cross.draw()
        instruction_4.draw()
        screen.draw.text('- wyjście z gry',center=(420,100), color='red', fontsize=35)
        instruction_1.draw()
        screen.draw.text('- chodzenie', center=(440, 200), color='white', fontsize=40)
        instruction_2.draw()
        screen.draw.text('- strzelanie',center=(420,300), color='white', fontsize=40)
        instruction_3.draw()
        screen.draw.text('- strzelanie (lepsze kule)', center=(500, 400), color='white', fontsize=40)
    elif mode == 'settings':
        helpers.my_map_draw()
        settings_m.draw()
        cross.draw()
        screen.draw.text('Dźwięk', center=(WIDTH / 2, HEIGHT / 2), color='White', fontsize=55)
    elif mode == 'miusic_settings':
        helpers.my_map_draw()
        cross.draw()

    elif mode == 'game':
        helpers.my_map_draw()
        helpers.enemies_draw(enemies)
        bomb.draw()
        for i in range(len(pelets)):
            pelets[i].draw()
        player.draw()
        screen.draw.text(str(ammo_in_gun) + '/' + str(AMMO), center=(950, 1000), color='white', fontsize=30)
        screen.draw.text('Amunicja przeciw pancerna: ' + str(super_ammo), center=(150, 1000), color='white',fontsize=30)
        add_ammo.draw()

    elif mode == 'win':
        helpers.my_map_draw()
        screen.draw.text('Wygrana!', center=(WIDTH / 2, HEIGHT / 2), color='white', fontsize=75)
        screen.draw.text('Kliknij enter', center=(512,580), color='white', fontsize=55)

    elif mode == 'end' or AMMO == 0 and ammo_in_gun == 0 and super_ammo == 0:
        screen.draw.text('Przegrana', center=(WIDTH / 2, HEIGHT / 2), color='red', fontsize=75)
        screen.draw.text('Kliknij enter', center=(512, 580), color='white', fontsize=55)

def on_key_down(key):
    global pelets, AMMO, super_ammo, ammo_in_gun, enemies, ENEMIES_COUNT, mode, win, LEVEL, test, additional_ammunition, shot
    if key == keys.ESCAPE:
        exit()

    if mode == 'game':
        if key == keys.R:
            AMMO += ammo_in_gun
            ammo_in_gun = 0
            for i in range(6):
                if AMMO > 0 and ammo_in_gun < 6:
                    AMMO -= 1
                    ammo_in_gun += 1
                    helpers.sfx_library["reload"].play()
                else:
                    break
        if key == keys.SPACE and ammo_in_gun > 0 or key == keys.LSHIFT and super_ammo > 0:
            if key == keys.SPACE:
                ammo_in_gun -= 1
                pelet = pgzrun.mod.Actor('meal')
                helpers.sfx_library["pistol"].play()
                pelet.force = 0
            elif key == keys.LSHIFT:
                super_ammo -= 1
                helpers.sfx_library["mortar"].play()
                pelet = pgzrun.mod.Actor('s_missel')
                pelet.force = 1
            # Y
            if player.image == 'up':
                pelet.pos = player.pos
                pelet.direction = 1
                pelets.append(pelet)
            elif player.image == 'cat':
                pelet.pos = player.pos
                pelet.direction = 2
                pelets.append(pelet)

            # X
            elif player.image == 'left':
                pelet.pos = player.pos
                pelet.direction = 3
                pelets.append(pelet)
            elif player.image == 'right':
                pelet.pos = player.pos
                pelet.direction = 4
                pelets.append(pelet)

    elif mode == 'win' and key == keys.RETURN and LEVEL < 5:
        add_ammo.y = -60
        additional_ammunition = 1

        LEVEL += 1

        ENEMIES_COUNT += 2
        enemies.clear()
        enemies = helpers.generate_enemies(ENEMIES_COUNT)

        player.pos = WIDTH / 2, HEIGHT / 2

        bomb.pos = random.randint(0, 1024), random.randint(0, 1024)

        AMMO = 18
        ammo_in_gun = 6
        super_ammo = 2

        win = ENEMIES_COUNT
        test = 1
        mode = 'menu'

    if mode == 'end' and key == keys.RETURN:

        add_ammo.y = -60
        additional_ammunition = 1
        enemies.clear()
        enemies = helpers.generate_enemies(ENEMIES_COUNT)
        player.pos = WIDTH / 2, HEIGHT / 2
        AMMO = 18
        ammo_in_gun = 6
        super_ammo = 2
        win = ENEMIES_COUNT
        test = 1
        mode = 'menu'

def on_mouse_down(pos, button):
    global mode, bomb
    if mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = 'game'
            bomb.image = 'bomb'
        if instruction.collidepoint(pos):
            mode = 'instr...'
        elif settings.collidepoint(pos):
            mode = 'settings'
    elif mode == 'instr...' and button == mouse.LEFT or mode == 'settings' and button == mouse.LEFT:
        if mode == 'settings':
            if settings_m.collidepoint(pos):
                mode = 'miusic_settings'
        if cross.collidepoint(pos):
            mode = 'menu'
    elif mode == 'miusic_settings' and button == mouse.LEFT:
        if cross.collidepoint(pos):
            mode = 'settings'

def collision():
    global pelets, enemies, win, mode, AMMO, add_ammo, additional_ammunition, bomb
    for j in range(len(pelets)):
        enemi_index = pelets[j].collidelist(enemies)
        if enemi_index != -1:
            win -= 1
            enemies.pop(enemi_index)
            if pelets[j].force == 0:
                pelets.pop(j)
            break
        if bomb.colliderect(pelets[j]) and bomb.image == 'bomb':
            pelets[j].direction = random.randint(1, 4)
            bomb.image = 'explosion'
            helpers.sfx_library["explosion"].play()
    enemi_index = bomb.collidelist(enemies)
    if enemi_index != -1 and bomb.image == 'explosion':
        win -= 1
        enemies.pop(enemi_index)

    enemi_index = player.collidelist(enemies)
    if enemi_index != -1 or player.colliderect(bomb) and bomb.image == 'explosion':
        mode = 'end'


    if player.colliderect(add_ammo) and additional_ammunition == 1:
        additional_ammunition = 0
        AMMO += random.randint(2,7)
        add = random.randint(0,100)
        if add == 50:
            super_ammo += random.randin(0,1)
        add_ammo.y = -60

def update():
    global player, pelets, mode, enemies, ENEMIES_COUNT, AMMO, ammo_in_gun, super_ammo, win, additional_ammunition, test
    if mode == 'game':


        collision()
        if bomb.image == 'explosion':
            clock.schedule(boom, 5.0)

        if keyboard.s and player.y < WIDTH or keyboard.down and player.y < HEIGHT:
            player.image = 'cat'
            player.y += 4
        elif keyboard.w and player.y != 0 or keyboard.up and player.y != 0:
            player.image = 'up'
            player.y -= 4

        elif keyboard.a and player.x != 0 or keyboard.left and player.x != 0:
            player.image = 'left'
            player.x -= 4
        elif keyboard.d and player.x < WIDTH or keyboard.right and player.x < WIDTH:
            player.image = 'right'
            player.x += 4
        for i in range(len(pelets)):
            if pelets[i].direction == 1 or pelets[i].direction == 2:
                if pelets[i].y != 0 and pelets[i].y != 1024:
                    if pelets[i].direction == 1:
                        pelets[i].y -= 8
                    elif pelets[i].direction == 2:
                        pelets[i].y += 8
                else:
                    pelets.pop(i)
                    break
            elif pelets[i].direction == 3 or pelets[i].direction == 4:
                if pelets[i].x != 0 and pelets[i].x != 1024:
                    if pelets[i].direction == 3:
                        pelets[i].x -= 6
                    elif pelets[i].direction == 4:
                        pelets[i].x += 6
                else:
                    pelets.pop(i)
                    break
        if additional_ammunition == 1:
            add_ammo.y == -60
        if AMMO == 0 and additional_ammunition == 1:
            add_ammo.y = 14


        if win == 0:
            mode = 'win'


pgzrun.go()
