import pygame
class Bullet1:
    def __init__(self, game_settings, screen, ship) -> None:
        self.screen = screen
        self.ship = ship
        self.game_settings = game_settings

        self.image = pygame.image.load('img/bullet1.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.midbottom = self.ship.rect.midtop
        self.y = float(self.ship.rect.centery)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self, x):
        if self.y < 10:
            self.rect.centerx = x

        self.y -= self.game_settings.bullet_speed_factor
        self.rect.centery = self.y
        if self.y < 0:
            self.reset()

    def blitme(self):
        # 指定位置画飞船
        self.screen.blit(self.image, self.rect)
    
    def reset(self):
        self.y = float(self.ship.rect.centery)