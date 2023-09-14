import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet1


def run_game():
    # 初始化
    pygame.init()
    pygame.display.set_caption('Plane Battle')
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))

    # 创造飞船
    ship = Ship(game_settings, screen)
    bullet1 = []
    BULLET1_NUM = 1
    for i in range(BULLET1_NUM):
        new_bullet = Bullet1(game_settings, screen, ship)
        bullet1.append(new_bullet)

    # 延迟
    delay = 100
    # 开始游戏主循环
    while True:
        # 监听键盘鼠标事件
        gf.check_events(ship)
        # 刷新飞船
        x = ship.update()

        if delay % 10:
            for bullet in bullet1:
                bullet.update(x)

        delay -= 1
        if not delay:
            delay = 100
        # 刷新页面
        gf.update_screen(game_settings, screen, ship, bullet1)


run_game()
