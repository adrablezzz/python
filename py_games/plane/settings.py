import pygame
class Settings:
    def __init__(self) -> None:
        self.screen_width = 480
        self.screen_height = 700
        self.background = pygame.image.load('img/background.png')
        self.ship_speed_factor = 10

        # 子弹设置
        self.bullet_speed_factor = 12