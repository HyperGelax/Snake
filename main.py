import pygame
import sqlite3
from random import randrange, uniform
import sys

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


if resolution == (1920, 1080):
    snake_size = 50
    apple_spawn_range_x = 1800
    apple_spawn_range_y = 1000
    menu_place = 960, 540
    start_player_coords = [(350, 700), (400, 700), (450, 700)]
    player_coords = [(350, 700), (400, 700), (450, 700)]
    start_b_place = 1012, 520
    exit_b_place = 1012, 720
    menu_b_place = 962, 620
    cont_b_place = 962, 470
    backscreen_place = 960, 540
    counter_place = 1800, 50
    start_b_draw_x = 860
    start_b_draw_y = 490
    exit_b_draw_x = 860
    exit_b_draw_y = 690
    menu_b_draw_x = 810
    menu_b_draw_y = 590
    cont_b_draw_x = 810
    cont_b_draw_y = 440
    button_size_1 = 300
    button_size_2 = 50
    apple_surf = pygame.image.load('resources/1080p/normalapple.png').convert_alpha()
    head_surf_xx = pygame.image.load('resources/1080p/skins/blue/snake_head_x+.png').convert_alpha()
    head_surf_x = pygame.image.load('resources/1080p/skins/blue/snake_head_x-.png').convert_alpha()
    head_surf_yy = pygame.image.load('resources/1080p/skins/blue/snake_head_y+.png').convert_alpha()
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
score = 19
multiplier = 1
direction = 'x+'
apple_coords = (randrange(snake_size, apple_spawn_range_x, snake_size), randrange(snake_size, apple_spawn_range_y,
                                                                                  snake_size))
running = True
stop = False
paused = False
game_status = False
menu_status = True

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
res_b = res_b_surf.get_rect(center=cont_b_place)
res_b_a = res_b_a_surf.get_rect(center=cont_b_place)


# кнопки

start_button = Button(button_size_1, button_size_2, start_b, start_b_a, start_surf, start_active_surf)
exit_button = Button(button_size_1, button_size_2, exit_b, exit_b_a, exit_surf, exit_active_surf)
menu_button = Button(button_size_1, button_size_2, menu_b, menu_b_a, menu_b_surf, menu_b_a_surf)
cont_button = Button(button_size_1, button_size_2, cont_b, cont_b_a, cont_b_surf, cont_b_a_surf)
res_button = Button(button_size_1, button_size_2, res_b, res_b_a, res_b_surf, res_b_a_surf)

# основные функции


def new_game():
    global direction, x, y, apple_coords, player_coords, score, stop, paused, apple_surf, apple, FPS, multiplier
    con = sqlite3.connect(bd)
    cur = con.cursor()
    result = cur.execute("""SELECT content FROM info WHERE title = 'record'""").fetchall()[0][0]
    if result < score:
        cur.execute("""UPDATE info SET content = ? WHERE title = ?""", (score, 'record'))
    cur.execute("""UPDATE info SET content = content + 1 WHERE title = ?""", ('played', ))
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


def menu():
    screen.blit(menu_surf, menu_back)

    exit_button.draw(exit_b_draw_x, exit_b_draw_y, sys.exit)
    start_button.draw(start_b_draw_x, start_b_draw_y, game_switch_1)

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
    game_status = False
    menu_status = True
    new_game()
    FPS = 75


def game_switch_3():
    global paused, FPS
    paused = False
    FPS = 5


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

pygame.quit()
