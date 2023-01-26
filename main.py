import pygame
import sqlite3
from random import randrange, uniform
import sys
import time

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Start")
clock = pygame.time.Clock()
bd = 'data.db'

resolution = 0
full_hd_surf = pygame.image.load("resources/resolution/full_hd.png")
full_hd_a_surf = pygame.image.load("resources/resolution/full_hd_a.png")
hd_surf = pygame.image.load("resources/resolution/hd.png")
hd_a_surf = pygame.image.load("resources/resolution/hd_a.png")
window_surf = pygame.image.load("resources/resolution/window.png")
window = window_surf.get_rect(center=(250, 250))
full_hd = full_hd_surf.get_rect(center=(250, 200))
hd = hd_surf.get_rect(center=(250, 300))
full_hd_a = full_hd_a_surf.get_rect(center=(250, 200))
hd_a = hd_a_surf.get_rect(center=(250, 300))


def resolution_changer_1():
    global resolution
    resolution = 1920, 1080


def resolution_changer_2():
    global resolution
    resolution = 1280, 720


class Button:
    def __init__(self, width, height, inactive, active, surf, active_surf):
        self.width = width
        self.height = height
        self.inactive = inactive
        self.active = active
        self.surf = surf
        self.active_surf = active_surf

    def draw(self, x, y, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                screen.blit(self.active_surf, self.active)
                if click[0] == 1:
                    if action is not None:
                        action()
            else:
                screen.blit(self.surf, self.inactive)
        else:
            screen.blit(self.surf, self.inactive)


hd_b = Button(300, 50, hd, hd_a, hd_surf, hd_a_surf)
full_hd_b = Button(300, 50, full_hd, full_hd_a, full_hd_surf, full_hd_a_surf)

while not resolution:
    clock.tick(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resolution = True

    screen.blit(window_surf, window)

    full_hd_b.draw(100, 175, resolution_changer_1)
    hd_b.draw(100, 275, resolution_changer_2)

    pygame.display.flip()

pygame.quit()

WIDTH, HEIGHT = resolution
FPS = 75

# colors
GRAY = (133, 133, 133)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (100, 100, 100)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

con = sqlite3.connect(bd)
cur = con.cursor()
old_skin = cur.execute("""SELECT title FROM info WHERE content = 'Set'""").fetchall()[0][0]
old_wall = cur.execute("""SELECT title FROM info WHERE content = 'Set1'""").fetchall()[0][0]
con.close()


if resolution == (1920, 1080):
    snake_size = 50
    apple_spawn_range_x = 1800
    apple_spawn_range_y = 1000
    menu_place = 960, 540
    start_player_coords = [(350, 700), (400, 700), (450, 700)]
    player_coords = [(350, 700), (400, 700), (450, 700)]
    start_b_place = 1012, 520
    shop_b_place = 1012, 620
    exit_b_place = 1012, 720
    menu_b_place = 962, 620
    cont_b_place = 962, 470
    menu_shop_b_place = 150, 1055
    backscreen_place = 960, 540
    counter_place = 1800, 50
    start_b_draw_x = 860
    start_b_draw_y = 490
    shop_b_draw_x = 860
    shop_b_draw_y = 590
    exit_b_draw_x = 860
    exit_b_draw_y = 690
    menu_b_draw_x = 810
    menu_b_draw_y = 590
    cont_b_draw_x = 810
    cont_b_draw_y = 440
    button_size_1 = 300
    button_size_2 = 50
    red_skin_place = 231, 488
    red_skin_x = 206
    red_skin_y = 464
    menu_shop_x = 0
    menu_shop_y = 1030
    ruby_place = 1750, 930
    blue_skin_place = 663, 488
    blue_skin_x = 638
    blue_skin_y = 464
    first_lock = 663, 870
    second_lock = 231, 870
    cube1_place = 1255, 488
    cube_x = 1230
    cube_y = 464
    cube2_place = 1687, 488
    cube2_x = 1662
    cube2_y = 464
    cube3_place = 1255, 875
    cube3_x = 1230
    cube3_y = 851
    cube4_place = 1687, 875
    cube4_x = 1662
    cube4_y = 851
    apple_surf = pygame.image.load('resources/1080p/normalapple.png').convert_alpha()
    head_surf_xx = pygame.image.load('resources/1080p/skins/blue/snake_head_x+.png').convert_alpha()
    head_surf_x = pygame.image.load('resources/1080p/skins/blue/snake_head_x-.png').convert_alpha()
    head_surf_yy = pygame.image.load(f'resources/1080p/skins/{old_skin}/snake_head_y+.png').convert_alpha()
    head_surf_y = pygame.image.load('resources/1080p/skins/blue/snake_head_y-.png').convert_alpha()
    body_surf_x = pygame.image.load('resources/1080p/skins/blue/snake_body_x.png').convert_alpha()
    body_surf_y = pygame.image.load('resources/1080p/skins/blue/snake_body_y.png').convert_alpha()
    snake_r_xy = pygame.image.load('resources/1080p/skins/blue/snake_rotation_x+y+.png').convert_alpha()
    snake_r_x_y = pygame.image.load('resources/1080p/skins/blue/snake_rotation_x-y+.png').convert_alpha()
    snake_r_xy_ = pygame.image.load('resources/1080p/skins/blue/snake_rotation_x+y-.png').convert_alpha()
    snake_r_x_y_ = pygame.image.load('resources/1080p/skins/blue/snake_rotation_x-y-.png').convert_alpha()
    snake_back_x = pygame.image.load('resources/1080p/skins/blue/snake_back_x+.png').convert_alpha()
    snake_back_xx = pygame.image.load('resources/1080p/skins/blue/snake_back_x-.png').convert_alpha()
    snake_back_y = pygame.image.load('resources/1080p/skins/blue/snake_back_y+.png').convert_alpha()
    snake_back_yy = pygame.image.load('resources/1080p/skins/blue/snake_back_y-.png').convert_alpha()
    backscreen_surf = pygame.image.load('resources/1080p/backscreen.png').convert()
    menu_surf = pygame.image.load('resources/1080p/menu back.png').convert()
    start_surf = pygame.image.load('resources/1080p/start button.png').convert_alpha()
    start_active_surf = pygame.image.load('resources/1080p/start button active.png').convert_alpha()
    exit_surf = pygame.image.load('resources/1080p/exit button.png').convert_alpha()
    exit_active_surf = pygame.image.load('resources/1080p/exit button active.png').convert_alpha()
    cont_b_surf = pygame.image.load('resources/1080p/cont.png').convert_alpha()
    cont_b_a_surf = pygame.image.load('resources/1080p/cont_a.png').convert_alpha()
    menu_b_surf = pygame.image.load('resources/1080p/menu_b.png').convert_alpha()
    menu_b_a_surf = pygame.image.load('resources/1080p/menu_b_a.png').convert_alpha()
    pause_surf = pygame.image.load('resources/1080p/pause.png')
    res_b_surf = pygame.image.load('resources/1080p/res_b.png').convert_alpha()
    res_b_a_surf = pygame.image.load('resources/1080p/res_b_a.png').convert_alpha()
    shop_backscreen = pygame.image.load('resources/1080p/shop.png').convert_alpha()
    shop_b_surf = pygame.image.load('resources/1080p/shop_b.png').convert_alpha()
    shop_b_a_surf = pygame.image.load('resources/1080p/shop_b_a.png').convert_alpha()
    red_head_surf = pygame.image.load('resources/1080p/skins/red/snake_head_y+.png')
    ruby_surf = pygame.image.load('resources/1080p/ruby.png').convert_alpha()
    selected_surf = pygame.image.load('resources/1080p/selected.png').convert_alpha()
    blue_head_surf = pygame.image.load(f'resources/1080p/skins/blue/snake_head_y+.png').convert_alpha()
    lock_surf = pygame.image.load(f'resources/1080p/lock.png').convert_alpha()
    wall2_surf = pygame.image.load(f'resources/1080p/wall2.png').convert_alpha()
    wall3_surf = pygame.image.load(f'resources/1080p/wall3.png').convert_alpha()
    wall4_surf = pygame.image.load(f'resources/1080p/wall4.png').convert_alpha()
    cube1_surf = pygame.image.load(f'resources/1080p/cube1.png').convert_alpha()
    cube2_surf = pygame.image.load(f'resources/1080p/cube2.png').convert_alpha()
    cube3_surf = pygame.image.load(f'resources/1080p/cube3.png').convert_alpha()
    cube4_surf = pygame.image.load(f'resources/1080p/cube4.png').convert_alpha()

elif resolution == (1280, 720):
    snake_size = 34
    apple_spawn_range_x = 1190
    apple_spawn_range_y = 680
    menu_place = 640, 360
    start_player_coords = [(239, 476), (273, 476), (306, 476)]
    player_coords = [(239, 476), (273, 476), (306, 476)]
    start_b_place = 675, 347
    exit_b_place = 675, 480
    menu_b_place = 641, 413
    cont_b_place = 641, 313
    backscreen_place = 640, 360
    counter_place = 1200, 34
    start_b_draw_x = 574
    start_b_draw_y = 327
    exit_b_draw_x = 573
    exit_b_draw_y = 460
    menu_b_draw_x = 540
    menu_b_draw_y = 393
    cont_b_draw_x = 540
    cont_b_draw_y = 293
    button_size_1 = 200
    button_size_2 = 33
    apple_surf = pygame.image.load('resources/720p/normalapple.png').convert_alpha()
    head_surf_xx = pygame.image.load('resources/720p/snake_head_x+.png').convert_alpha()
    head_surf_x = pygame.image.load('resources/720p/snake_head_x-.png').convert_alpha()
    head_surf_yy = pygame.image.load('resources/720p/snake_head_y+.png').convert_alpha()
    head_surf_y = pygame.image.load('resources/720p/snake_head_y-.png').convert_alpha()
    body_surf_x = pygame.image.load('resources/720p/snake_body_x.png').convert_alpha()
    body_surf_y = pygame.image.load('resources/720p/snake_body_y.png').convert_alpha()
    snake_r_xy = pygame.image.load('resources/720p/snake_rotation_x+y+.png').convert_alpha()
    snake_r_x_y = pygame.image.load('resources/720p/snake_rotation_x-y+.png').convert_alpha()
    snake_r_xy_ = pygame.image.load('resources/720p/snake_rotation_x+y-.png').convert_alpha()
    snake_r_x_y_ = pygame.image.load('resources/720p/snake_rotation_x-y-.png').convert_alpha()
    snake_back_x = pygame.image.load('resources/720p/snake_back_x+.png').convert_alpha()
    snake_back_xx = pygame.image.load('resources/720p/snake_back_x-.png').convert_alpha()
    snake_back_y = pygame.image.load('resources/720p/snake_back_y+.png').convert_alpha()
    snake_back_yy = pygame.image.load('resources/720p/snake_back_y-.png').convert_alpha()
    backscreen_surf = pygame.image.load('resources/720p/backscreen.png').convert()
    menu_surf = pygame.image.load('resources/720p/menu back.png').convert()
    start_surf = pygame.image.load('resources/720p/start button.png').convert_alpha()
    start_active_surf = pygame.image.load('resources/720p/start button active.png').convert_alpha()
    exit_surf = pygame.image.load('resources/720p/exit button.png').convert_alpha()
    exit_active_surf = pygame.image.load('resources/720p/exit button active.png').convert_alpha()
    cont_b_surf = pygame.image.load('resources/720p/cont.png').convert_alpha()
    cont_b_a_surf = pygame.image.load('resources/720p/cont_a.png').convert_alpha()
    menu_b_surf = pygame.image.load('resources/720p/menu_b.png').convert_alpha()
    menu_b_a_surf = pygame.image.load('resources/720p/menu_b_a.png').convert_alpha()
    pause_surf = pygame.image.load('resources/720p/pause.png')
    res_b_surf = pygame.image.load('resources/720p/res_b.png').convert_alpha()
    res_b_a_surf = pygame.image.load('resources/720p/res_b_a.png').convert_alpha()

# базовые переменные
score = 0
multiplier = 1
direction = 'x+'
apple_coords = (randrange(snake_size, apple_spawn_range_x, snake_size), randrange(snake_size, apple_spawn_range_y,
                                                                                  snake_size))
running = True
stop = False
paused = False
game_status = False
menu_status = True
shop_status = False

# текстуры
apple = apple_surf.get_rect(center=apple_coords)
menu_back = menu_surf.get_rect(center=menu_place)
start_b = start_surf.get_rect(center=start_b_place)
start_b_a = start_active_surf.get_rect(center=start_b_place)
exit_b = exit_surf.get_rect(center=exit_b_place)
exit_b_a = exit_active_surf.get_rect(center=exit_b_place)
backscreen = backscreen_surf.get_rect(center=backscreen_place)
head = head_surf_xx.get_rect(center=player_coords[-1])
cont_b = cont_b_surf.get_rect(center=cont_b_place)
cont_b_a = cont_b_a_surf.get_rect(center=cont_b_place)
pause_m = pause_surf.get_rect(center=menu_place)
menu_b = menu_b_surf.get_rect(center=menu_b_place)
menu_b_a = menu_b_a_surf.get_rect(center=menu_b_place)
menu_s_b = menu_b_surf.get_rect(center=menu_shop_b_place)
menu_s_b_a = menu_b_a_surf.get_rect(center=menu_shop_b_place)
res_b = res_b_surf.get_rect(center=cont_b_place)
res_b_a = res_b_a_surf.get_rect(center=cont_b_place)
shop_b = shop_b_surf.get_rect(center=shop_b_place)
shop_b_a = shop_b_a_surf.get_rect(center=shop_b_place)
red_skin_b = red_head_surf.get_rect(center=red_skin_place)
red_skin_b_a = red_head_surf.get_rect(center=red_skin_place)
ruby = ruby_surf.get_rect(center=ruby_place)
blue_skin = blue_head_surf.get_rect(center=blue_skin_place)
blue_skin_a = blue_head_surf.get_rect(center=blue_skin_place)
wall1 = backscreen_surf.get_rect(center=cube1_place)
wall2 = backscreen_surf.get_rect(center=cube2_place)
wall3 = backscreen_surf.get_rect(center=cube3_place)
wall4 = backscreen_surf.get_rect(center=cube4_place)

# кнопки

start_button = Button(button_size_1, button_size_2, start_b, start_b_a, start_surf, start_active_surf)
exit_button = Button(button_size_1, button_size_2, exit_b, exit_b_a, exit_surf, exit_active_surf)
menu_button = Button(button_size_1, button_size_2, menu_b, menu_b_a, menu_b_surf, menu_b_a_surf)
cont_button = Button(button_size_1, button_size_2, cont_b, cont_b_a, cont_b_surf, cont_b_a_surf)
res_button = Button(button_size_1, button_size_2, res_b, res_b_a, res_b_surf, res_b_a_surf)
shop_button = Button(button_size_1, button_size_2, shop_b, shop_b_a, shop_b_surf, shop_b_a_surf)
red_skin_button = Button(button_size_2, button_size_2, red_skin_b, red_skin_b_a, red_head_surf, red_head_surf)
menu_shop_button = Button(button_size_1, button_size_2, menu_s_b, menu_s_b_a, menu_b_surf, menu_b_a_surf)
blue_skin_button = Button(button_size_2, button_size_2, blue_skin, blue_skin_a, blue_head_surf, blue_head_surf)
wall1_button = Button(button_size_2, button_size_2, wall1, wall1, cube1_surf, cube1_surf)
wall2_button = Button(button_size_2, button_size_2, wall2, wall2, cube2_surf, cube2_surf)
wall3_button = Button(button_size_2, button_size_2, wall2, wall2, cube3_surf, cube3_surf)
wall4_button = Button(button_size_2, button_size_2, wall2, wall2, cube4_surf, cube4_surf)


# основные функции

def check_selected_skin():
    global old_skin
    con = sqlite3.connect(bd)
    cur = con.cursor()
    for i in ['blue', 'yellow', 'red', 'green']:
        result = cur.execute("""SELECT content FROM info WHERE title = ?""", (i, )).fetchall()[0][0]
        if result == 'Set':
            old_skin = i
            return


def check_selected_wall():
    global old_wall
    con = sqlite3.connect(bd)
    cur = con.cursor()
    for i in ['wall1', 'wall2', 'wall3', 'wall4']:
        result = cur.execute("""SELECT content FROM info WHERE title = ?""", (i, )).fetchall()[0][0]
        if result == 'Set1':
            old_wall = i
            return


def new_game():
    global direction, x, y, apple_coords, player_coords, score, stop, paused, apple_surf, apple, FPS, multiplier
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'record'""").fetchall()[0][0]
    if result < score:
        cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (score, 'record'))
    cur.execute("""UPDATE info SET content = content + 1 WHERE title = ?""", ('played',))
    multiplier = uniform(score / 20, score / 10)
    rubies = cur.execute("""SELECT content FROM info WHERE title = 'rubies'""").fetchall()[0][0]
    if multiplier > 1:
        new_rubies = round((score * multiplier) + rubies)
        cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (new_rubies, 'rubies'))
    else:
        new_rubies = score + rubies
        cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (new_rubies, 'rubies'))
    con.commit()
    con.close()
    FPS = 5
    direction = 'x+'
    player_coords = start_player_coords[:]
    x, y = player_coords[-1]
    multiplier = 1
    score = 0
    stop = False
    paused = False
    apple_coords = new_apple_coords()
    apple = apple_surf.get_rect(center=apple_coords)
    pygame.display.update(apple)
    screen.blit(apple_surf, apple)


def extension():
    global player_coords
    timex, timey = player_coords[0]
    if player_coords[0][0] - player_coords[1][0] < 0:
        player_coords.insert(0, (timex - snake_size, timey))
    if player_coords[0][0] - player_coords[1][0] > 0:
        player_coords.insert(0, (timex + snake_size, timey))
    if player_coords[0][1] - player_coords[1][1] < 0:
        player_coords.insert(0, (timex, timey - snake_size))
    if player_coords[0][1] - player_coords[1][1] > 0:
        player_coords.insert(0, (timex, timey + snake_size))


def snake():
    global head_surf_xx, head_surf_y, head_surf_x, head_surf_yy, body_surf_x, body_surf_y, player_coords, direction, \
        screen, snake_r_xy, snake_r_xy_, snake_r_x_y_, snake_r_x_y, snake_back_x, snake_back_xx, snake_back_y, \
        snake_back_yy
    # голова
    head = head_surf_xx.get_rect(center=player_coords[-1])
    if direction == 'x+':
        screen.blit(head_surf_xx, head)
    if direction == 'x-':
        screen.blit(head_surf_x, head)
    if direction == 'y+':
        screen.blit(head_surf_yy, head)
    if direction == 'y-':
        screen.blit(head_surf_y, head)

    # тело
    for i in range(1, len(player_coords) - 1):
        if player_coords[i][1] == player_coords[i - 1][1] and player_coords[i][1] == player_coords[i + 1][1]:
            body = body_surf_x.get_rect(center=player_coords[i])
            screen.blit(body_surf_x, body)
        elif player_coords[i][0] == player_coords[i - 1][0] and player_coords[i][0] == player_coords[i + 1][0]:
            body = body_surf_y.get_rect(center=player_coords[i])
            screen.blit(body_surf_y, body)
        else:
            # поворот х - у -
            if player_coords[i][0] == player_coords[i - 1][0] and player_coords[i][0] != player_coords[i + 1][0]:
                if player_coords[i][0] > player_coords[i + 1][0] and player_coords[i][1] < player_coords[i - 1][1]:
                    snake_r = snake_r_x_y_.get_rect(center=player_coords[i])
                    screen.blit(snake_r_x_y_, snake_r)
            if player_coords[i][0] == player_coords[i + 1][0] and player_coords[i][0] != player_coords[i - 1][0]:
                if player_coords[i][0] > player_coords[i - 1][0] and player_coords[i][1] < player_coords[i + 1][1]:
                    snake_r = snake_r_x_y_.get_rect(center=player_coords[i])
                    screen.blit(snake_r_x_y_, snake_r)
            # поворот х + у -
            if player_coords[i][0] == player_coords[i - 1][0] and player_coords[i][0] != player_coords[i + 1][0]:
                if player_coords[i][0] < player_coords[i + 1][0] and player_coords[i][1] < player_coords[i - 1][1]:
                    snake_r = snake_r_xy_.get_rect(center=player_coords[i])
                    screen.blit(snake_r_xy_, snake_r)
            if player_coords[i][0] == player_coords[i + 1][0] and player_coords[i][0] != player_coords[i - 1][0]:
                if player_coords[i][0] < player_coords[i - 1][0] and player_coords[i][1] < player_coords[i + 1][1]:
                    snake_r = snake_r_xy_.get_rect(center=player_coords[i])
                    screen.blit(snake_r_xy_, snake_r)

            # поворот x + y +
            if player_coords[i][0] == player_coords[i - 1][0] and player_coords[i][0] != player_coords[i + 1][0]:
                if player_coords[i][0] < player_coords[i + 1][0] and player_coords[i][1] > player_coords[i - 1][1]:
                    snake_r = snake_r_xy.get_rect(center=player_coords[i])
                    screen.blit(snake_r_xy, snake_r)
            if player_coords[i][0] == player_coords[i + 1][0] and player_coords[i][0] != player_coords[i - 1][0]:
                if player_coords[i][0] < player_coords[i - 1][0] and player_coords[i][1] > player_coords[i + 1][1]:
                    snake_r = snake_r_xy.get_rect(center=player_coords[i])
                    screen.blit(snake_r_xy, snake_r)

            # поворот x - y +
            if player_coords[i][0] == player_coords[i - 1][0] and player_coords[i][0] != player_coords[i + 1][0]:
                if player_coords[i][0] > player_coords[i + 1][0] and player_coords[i][1] > player_coords[i - 1][1]:
                    snake_r = snake_r_x_y.get_rect(center=player_coords[i])
                    screen.blit(snake_r_x_y, snake_r)
            if player_coords[i][0] == player_coords[i + 1][0] and player_coords[i][0] != player_coords[i - 1][0]:
                if player_coords[i][0] > player_coords[i - 1][0] and player_coords[i][1] > player_coords[i + 1][1]:
                    snake_r = snake_r_x_y.get_rect(center=player_coords[i])
                    screen.blit(snake_r_x_y, snake_r)

    # хвост
    if player_coords[0][0] - player_coords[1][0] < 0:
        back = snake_back_x.get_rect(center=player_coords[0])
        screen.blit(snake_back_x, back)
    if player_coords[0][0] - player_coords[1][0] > 0:
        back = snake_back_xx.get_rect(center=player_coords[0])
        screen.blit(snake_back_xx, back)
    if player_coords[0][1] - player_coords[1][1] < 0:
        back = snake_back_yy.get_rect(center=player_coords[0])
        screen.blit(snake_back_yy, back)
    if player_coords[0][1] - player_coords[1][1] > 0:
        back = snake_back_y.get_rect(center=player_coords[0])
        screen.blit(snake_back_y, back)


def pause():
    snake()
    screen.blit(pause_surf, pause_m)
    menu_button.draw(menu_b_draw_x, menu_b_draw_y, game_switch_2)
    cont_button.draw(cont_b_draw_x, cont_b_draw_y, game_switch_3)


def new_apple_coords():
    apple_coords = (randrange(snake_size, apple_spawn_range_x, snake_size), randrange(snake_size, apple_spawn_range_y,
                                                                                      snake_size))
    return apple_coords


def counter():
    f = pygame.font.Font('C:\WINDOWS\Fonts\impact.ttf', 36)
    text = f.render(f'Счет:{score}', True, DARK_GRAY)
    place = text.get_rect(center=counter_place)
    screen.blit(text, place)


def end_screen():
    global FPS, score
    snake()
    FPS = 75
    screen.blit(pause_surf, pause_m)
    menu_button.draw(menu_b_draw_x, menu_b_draw_y, game_switch_2)
    res_button.draw(cont_b_draw_x, cont_b_draw_y, new_game)


def game():
    global apple_coords, apple, stop, paused, score, direction, running, direction, paused, running, game_status, \
        menu_status

    screen.blit(backscreen_surf, backscreen)

    # Спавн яблока
    screen.blit(apple_surf, apple)
    if paused and not stop:
        pause()

    if not stop:
        if not paused:
            x, y = player_coords[-1]
            if direction == 'x+':
                player_coords.append((x + snake_size, y))
            if direction == 'x-':
                player_coords.append((x - snake_size, y))
            if direction == 'y-':
                player_coords.append((x, y + snake_size))
            if direction == 'y+':
                player_coords.append((x, y - snake_size))

            del player_coords[0]

            if apple_coords == player_coords[-1]:
                score += 1
                extension()
                while apple_coords in player_coords:
                    apple_coords = new_apple_coords()
                    apple = apple_surf.get_rect(center=apple_coords)
                    pygame.display.update(apple)
                    screen.blit(apple_surf, apple)

            snake()

            counter()

            # Проверка на столкновение
            for j in range(len(player_coords) - 1):
                if player_coords[-1] == player_coords[j]:
                    stop = True

            if y > HEIGHT or y < snake_size or x > WIDTH or x < snake_size:
                stop = True
    if stop:
        end_screen()

    pygame.display.update(apple)
    pygame.display.flip()


def red_skin_check():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'red'""").fetchall()[0][0]
    if result == 'Closed':
        lock = lock_surf.get_rect(center=red_skin_place)
        screen.blit(lock_surf, lock)


def wall2_check():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'wall2'""").fetchall()[0][0]
    if result == 'Closed1':
        lock = lock_surf.get_rect(center=cube2_place)
        screen.blit(lock_surf, lock)


def wall3_check():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'wall3'""").fetchall()[0][0]
    if result == 'Closed1':
        lock = lock_surf.get_rect(center=cube3_place)
        screen.blit(lock_surf, lock)


def wall4_check():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'wall4'""").fetchall()[0][0]
    if result == 'Closed1':
        lock = lock_surf.get_rect(center=cube4_place)
        screen.blit(lock_surf, lock)


def red_skin_operation():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'red'""").fetchall()[0][0]
    if result == 'Closed':
        money = cur.execute("""SELECT content FROM info WHERE title = 'rubies'""").fetchall()[0][0]
        if money >= 500:
            cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (money - 500, 'rubies'))
            cur.execute("""UPDATE info SET content = 'Bought' WHERE title = 'red'""")

    if result == 'Bought':
        skin_change1()
        cur.execute("""UPDATE info SET content = 'Set' WHERE title = 'red'""")
        cur.execute("""UPDATE info SET content = 'Bought' WHERE title = ?""", (old_skin,))
    if result == 'Set':
        pass
    con.commit()
    con.close()


def blue_skin_operation():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'blue'""").fetchall()[0][0]
    if result == 'Closed':
        money = cur.execute("""SELECT content FROM info WHERE title = 'rubies'""").fetchall()[0][0]
        if money >= 500:
            cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (money - 500, 'rubies'))
            cur.execute("""UPDATE info SET content = 'Bought' WHERE title = 'blue'""")

    if result == 'Bought':
        skin_change2()
        cur.execute("""UPDATE info SET content = 'Set' WHERE title = 'blue'""")
        cur.execute("""UPDATE info SET content = 'Bought' WHERE title = ?""", (old_skin,))
    if result == 'Set':
        pass
    con.commit()
    con.close()


def wall1_operation():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'wall1'""").fetchall()[0][0]
    if result == 'Closed1':
        money = cur.execute("""SELECT content FROM info WHERE title = 'rubies'""").fetchall()[0][0]
        if money >= 500:
            cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (money - 300, 'rubies'))
            cur.execute("""UPDATE info SET content = 'Bought1' WHERE title = 'wall1'""")

    if result == 'Bought1':
        wall1_change()
        cur.execute("""UPDATE info SET content = 'Set1' WHERE title = 'wall1'""")
        cur.execute("""UPDATE info SET content = 'Bought1' WHERE title = ?""", (old_wall,))
    if result == 'Set1':
        pass
    con.commit()
    con.close()


def wall2_operation():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'wall2'""").fetchall()[0][0]
    if result == 'Closed1':
        money = cur.execute("""SELECT content FROM info WHERE title = 'rubies'""").fetchall()[0][0]
        if money >= 500:
            cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (money - 300, 'rubies'))
            cur.execute("""UPDATE info SET content = 'Bought1' WHERE title = 'wall2'""")

    if result == 'Bought1':
        wall2_change()
        cur.execute("""UPDATE info SET content = 'Set1' WHERE title = 'wall2'""")
        cur.execute("""UPDATE info SET content = 'Bought1' WHERE title = ?""", (old_wall,))
    if result == 'Set1':
        pass
    con.commit()
    con.close()


def wall3_operation():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'wall3'""").fetchall()[0][0]
    if result == 'Closed1':
        money = cur.execute("""SELECT content FROM info WHERE title = 'rubies'""").fetchall()[0][0]
        if money >= 500:
            cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (money - 300, 'rubies'))
            cur.execute("""UPDATE info SET content = 'Bought1' WHERE title = 'wall3'""")

    if result == 'Bought1':
        wall3_change()
        cur.execute("""UPDATE info SET content = 'Set1' WHERE title = 'wall3'""")
        cur.execute("""UPDATE info SET content = 'Bought1' WHERE title = ?""", (old_wall,))
    if result == 'Set1':
        pass
    con.commit()
    con.close()


def wall4_operation():
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'wall4'""").fetchall()[0][0]
    if result == 'Closed1':
        money = cur.execute("""SELECT content FROM info WHERE title = 'rubies'""").fetchall()[0][0]
        if money >= 500:
            cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (money - 300, 'rubies'))
            cur.execute("""UPDATE info SET content = 'Bought1' WHERE title = 'wall4'""")

    if result == 'Bought1':
        wall4_change()
        cur.execute("""UPDATE info SET content = 'Set1' WHERE title = 'wall4'""")
        cur.execute("""UPDATE info SET content = 'Bought1' WHERE title = ?""", (old_wall,))
    if result == 'Set1':
        pass
    con.commit()
    con.close()


def shop():
    screen.blit(shop_backscreen, menu_back)
    menu_shop_button.draw(menu_shop_x, menu_shop_y, game_switch_5)
    red_skin_button.draw(red_skin_x, red_skin_y, red_skin_operation)
    blue_skin_button.draw(blue_skin_x, blue_skin_y, blue_skin_operation)
    wall1_button.draw(cube_x, cube_y, wall1_operation)
    wall2_button.draw(cube2_x, cube2_y, wall2_operation)
    wall3_button.draw(cube3_x, cube3_y, wall3_operation)
    wall4_button.draw(cube4_x, cube4_y, wall4_operation)
    lock = lock_surf.get_rect(center=first_lock)
    screen.blit(lock_surf, lock)
    lock = lock_surf.get_rect(center=second_lock)
    screen.blit(lock_surf, lock)
    screen.blit(cube1_surf, cube1_surf.get_rect(center=cube1_place))
    screen.blit(cube2_surf, cube2_surf.get_rect(center=cube2_place))
    screen.blit(cube3_surf, cube3_surf.get_rect(center=cube3_place))
    screen.blit(cube4_surf, cube4_surf.get_rect(center=cube4_place))
    con = sqlite3.connect(bd)
    cur = con.cursor()
    if resolution == (1920, 1080):
        f = pygame.font.Font('C:\WINDOWS\Fonts\impact.ttf', 36)
        rubies = cur.execute("""SELECT content FROM info WHERE title = 'rubies'""").fetchall()[0][0]
        text = f.render(f'{rubies}', True, DARK_GRAY)
        place = text.get_rect(center=(1800, 25))
        screen.blit(text, place)
    check_selected_skin()
    red_skin_check()
    check_selected_wall()
    wall2_check()
    wall3_check()
    wall4_check()
    if old_skin == 'red':
        if resolution == (1920, 1080):
            selected = selected_surf.get_rect(center=red_skin_place)
            screen.blit(selected_surf, selected)
    if old_skin == 'blue':
        if resolution == (1920, 1080):
            selected = selected_surf.get_rect(center=blue_skin_place)
            screen.blit(selected_surf, selected)
    if old_wall == 'wall1':
        if resolution == (1920, 1080):
            selected = selected_surf.get_rect(center=cube1_place)
            screen.blit(selected_surf, selected)
    if old_wall == 'wall2':
        if resolution == (1920, 1080):
            selected = selected_surf.get_rect(center=cube2_place)
            screen.blit(selected_surf, selected)
    if old_wall == 'wall3':
        if resolution == (1920, 1080):
            selected = selected_surf.get_rect(center=cube3_place)
            screen.blit(selected_surf, selected)
    if old_wall == 'wall4':
        if resolution == (1920, 1080):
            selected = selected_surf.get_rect(center=cube4_place)
            screen.blit(selected_surf, selected)
    pygame.display.flip()


def menu():
    screen.blit(menu_surf, menu_back)

    exit_button.draw(exit_b_draw_x, exit_b_draw_y, sys.exit)
    start_button.draw(start_b_draw_x, start_b_draw_y, game_switch_1)
    shop_button.draw(shop_b_draw_x, shop_b_draw_y, game_switch_4)
    screen.blit(ruby_surf, ruby)

    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'record'""").fetchall()[0][0]
    result2 = cur.execute("""SELECT content FROM info WHERE title = 'played'""").fetchall()[0][0]
    rubies = cur.execute("""SELECT content FROM info WHERE title = 'rubies'""").fetchall()[0][0]

    f = pygame.font.Font('C:\WINDOWS\Fonts\impact.ttf', 36)
    text = f.render(f'Рекорд: {result}', True, DARK_GRAY)
    text2 = f.render(f'Игр сыграно: {result2}', True, DARK_GRAY)
    text3 = f.render(f'{rubies}', True, DARK_GRAY)
    if resolution == (1920, 1080):
        place = text.get_rect(center=(1700, 980))
        screen.blit(text, place)

        place = text.get_rect(center=(1700, 1030))
        screen.blit(text2, place)

        place = text.get_rect(center=(1700, 930))
        screen.blit(text3, place)
    else:
        place = text.get_rect(center=(1133, 653))
        screen.blit(text, place)

        place = text.get_rect(center=(1133, 687))
        screen.blit(text2, place)

    con.close()

    pygame.display.flip()


def game_switch_1():
    global game_status, menu_status, FPS
    FPS = 5
    game_status = True
    menu_status = False


def game_switch_2():
    global game_status, menu_status, FPS
    time.sleep(0.1)
    game_status = False
    menu_status = True
    new_game()
    FPS = 75


def game_switch_3():
    global paused, FPS
    paused = False
    FPS = 5


def game_switch_4():
    global menu_status, shop_status
    menu_status = False
    shop_status = True


def game_switch_5():
    global menu_status, shop_status
    menu_status = True
    shop_status = False


def skin_change1():
    global head_surf_xx, head_surf_y, head_surf_x, head_surf_yy, body_surf_x, body_surf_y, player_coords, direction, \
        screen, snake_r_xy, snake_r_xy_, snake_r_x_y_, snake_r_x_y, snake_back_x, snake_back_xx, snake_back_y, \
        snake_back_yy
    head_surf_xx = pygame.image.load('resources/1080p/skins/red/snake_head_x+.png').convert_alpha()
    head_surf_x = pygame.image.load('resources/1080p/skins/red/snake_head_x-.png').convert_alpha()
    head_surf_yy = pygame.image.load(f'resources/1080p/skins/red/snake_head_y+.png').convert_alpha()
    head_surf_y = pygame.image.load('resources/1080p/skins/red/snake_head_y-.png').convert_alpha()
    body_surf_x = pygame.image.load('resources/1080p/skins/red/snake_body_x.png').convert_alpha()
    body_surf_y = pygame.image.load('resources/1080p/skins/red/snake_body_y.png').convert_alpha()
    snake_r_xy = pygame.image.load('resources/1080p/skins/red/snake_rotation_x+y+.png').convert_alpha()
    snake_r_x_y = pygame.image.load('resources/1080p/skins/red/snake_rotation_x-y+.png').convert_alpha()
    snake_r_xy_ = pygame.image.load('resources/1080p/skins/red/snake_rotation_x+y-.png').convert_alpha()
    snake_r_x_y_ = pygame.image.load('resources/1080p/skins/red/snake_rotation_x-y-.png').convert_alpha()
    snake_back_x = pygame.image.load('resources/1080p/skins/red/snake_back_x+.png').convert_alpha()
    snake_back_xx = pygame.image.load('resources/1080p/skins/red/snake_back_x-.png').convert_alpha()
    snake_back_y = pygame.image.load('resources/1080p/skins/red/snake_back_y+.png').convert_alpha()
    snake_back_yy = pygame.image.load('resources/1080p/skins/red/snake_back_y-.png').convert_alpha()


def skin_change2():
    global head_surf_xx, head_surf_y, head_surf_x, head_surf_yy, body_surf_x, body_surf_y, player_coords, direction, \
        screen, snake_r_xy, snake_r_xy_, snake_r_x_y_, snake_r_x_y, snake_back_x, snake_back_xx, snake_back_y, \
        snake_back_yy
    head_surf_xx = pygame.image.load('resources/1080p/skins/blue/snake_head_x+.png').convert_alpha()
    head_surf_x = pygame.image.load('resources/1080p/skins/blue/snake_head_x-.png').convert_alpha()
    head_surf_yy = pygame.image.load(f'resources/1080p/skins/blue/snake_head_y+.png').convert_alpha()
    head_surf_y = pygame.image.load('resources/1080p/skins/blue/snake_head_y-.png').convert_alpha()
    body_surf_x = pygame.image.load('resources/1080p/skins/blue/snake_body_x.png').convert_alpha()
    body_surf_y = pygame.image.load('resources/1080p/skins/blue/snake_body_y.png').convert_alpha()
    snake_r_xy = pygame.image.load('resources/1080p/skins/blue/snake_rotation_x+y+.png').convert_alpha()
    snake_r_x_y = pygame.image.load('resources/1080p/skins/blue/snake_rotation_x-y+.png').convert_alpha()
    snake_r_xy_ = pygame.image.load('resources/1080p/skins/blue/snake_rotation_x+y-.png').convert_alpha()
    snake_r_x_y_ = pygame.image.load('resources/1080p/skins/blue/snake_rotation_x-y-.png').convert_alpha()
    snake_back_x = pygame.image.load('resources/1080p/skins/blue/snake_back_x+.png').convert_alpha()
    snake_back_xx = pygame.image.load('resources/1080p/skins/blue/snake_back_x-.png').convert_alpha()
    snake_back_y = pygame.image.load('resources/1080p/skins/blue/snake_back_y+.png').convert_alpha()
    snake_back_yy = pygame.image.load('resources/1080p/skins/blue/snake_back_y-.png').convert_alpha()


def wall1_change():
    global backscreen_surf
    if resolution == (1920, 1080):
        backscreen_surf = pygame.image.load('resources/1080p/backscreen.png').convert()


def wall2_change():
    global backscreen_surf
    if resolution == (1920, 1080):
        backscreen_surf = pygame.image.load('resources/1080p/wall2.png').convert()


def wall3_change():
    global backscreen_surf
    if resolution == (1920, 1080):
        backscreen_surf = pygame.image.load('resources/1080p/wall3.png').convert()


def wall4_change():
    global backscreen_surf
    if resolution == (1920, 1080):
        backscreen_surf = pygame.image.load('resources/1080p/wall4.png').convert()


while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_status:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and (paused or stop):
                    game_switch_2()
                    new_game()
                if event.key == pygame.K_LEFT and direction != 'x+' and not paused:
                    direction = 'x-'
                if event.key == pygame.K_RIGHT and direction != 'x-' and not paused:
                    direction = 'x+'
                if event.key == pygame.K_UP and direction != 'y-' and not paused:
                    direction = 'y+'
                if event.key == pygame.K_DOWN and direction != 'y+' and not paused:
                    direction = 'y-'
                if event.key == pygame.K_ESCAPE and not paused:
                    paused = True
                    FPS = 75
                elif event.key == pygame.K_ESCAPE and paused:
                    paused = False
                    FPS = 5
                if event.key == pygame.K_r and stop:
                    new_game()

    if menu_status:
        menu()
    if game_status:
        game()
    if shop_status:
        shop()

pygame.quit()
