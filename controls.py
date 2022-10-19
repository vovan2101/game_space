import pygame, sys
from bullet import Bullet
from ino import Ino
import time


def events(screen, gun, bullets):
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Вправо
            if event.key == pygame.K_d:
                gun.mright = True
            # Влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            # Стрельба
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Вправо после отжатия
            if event.key == pygame.K_d:
                gun.mright = False
            # Влево после отжатия
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, stats, sc, gun, inos, bullets):
    # Обновление Экрана
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(inos, bullets, screen, stats, sc):
    # Обновлять позицию пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():          
            stats.score += 1 * len(inos)
            sc.image_score()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def gun_kill(stats, screen, gun, inos, bullets):
    # Столкновение пушки и армии
    if stats.guns_left > 0:
        stats.guns_left -= 1
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_inos(gun, inos, stats, screen, bullets):
    # Обновляет позицию инопланетян
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, gun, inos, bullets)
    inos_check(stats, screen, gun, inos, bullets)


def inos_check(stats, screen, gun, inos, bullets):
    # Проверка, добралась ли армия до края экрана
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, inos, bullets)
            break


def create_army(screen, inos):
    # Создание армии пришельцев
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 1 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 200 - 1 * ino_height) / ino_height)

    for row_number in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)