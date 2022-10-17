from turtle import Screen
import pygame, sys
from bullet import Bullet

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

def update(bg_color, screen, gun, bullets):
    # Обновление Экрана
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()

def update_bullets(bullets):
    # Обновлять позицию пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)