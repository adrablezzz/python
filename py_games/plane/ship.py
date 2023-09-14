import pygame
class Ship:
    def __init__(self, game_settings, screen) -> None:
        self.screen = screen
        self.game_settings = game_settings

        # 加载飞船图像,获取其外接矩形
        self.image1 = pygame.image.load('img/me1.png').convert_alpha()
        self.image2 = pygame.image.load('img/me2.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('img/me_destroy_1.png').convert_alpha(),
            pygame.image.load('img/me_destroy_2.png').convert_alpha(),
            pygame.image.load('img/me_destroy_3.png').convert_alpha(),
            pygame.image.load('img/me_destroy_4.png').convert_alpha()
        ])

        self.rect = self.image1.get_rect()
        self.screen_rect = screen.get_rect()

        # 飞船放到底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_left = False
        self.moving_right = False

        self.mask = pygame.mask.from_surface(self.image1)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        self.rect.centerx = self.center
        return self.center


    def blitme(self):
        # 指定位置画飞船
        self.screen.blit(self.image1, self.rect)