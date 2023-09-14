import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False


def update_screen(game_settings, screen, ship, bullets):
    # 每次循环重绘
    screen.blit(game_settings.background, (0, 0))
    ship.blitme()
    for bullet in bullets:
        bullet.blitme()
    # 让最近绘制的可见
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)
