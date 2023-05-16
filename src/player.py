import pygame
import math

from bullet import Bullet
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load('./assets/player/idle/idle0.png').convert_alpha()
        self.font = pygame.font.Font(None, 30)

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen):
        scaled_image = pygame.transform.scale(self.image, (100, 100))

        flipped_image = pygame.transform.flip(scaled_image, True, False)

        new_rect = flipped_image.get_rect(center=(self.x, self.y))
        screen.blit(flipped_image, new_rect)

        speed_text = self.font.render("Speed: {}".format(self.speed), True, (255, 255, 255))
        # position of the text on the screen
        screen.blit(speed_text, (10, 10))

    def shoot(self, bullets):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        offset = 25
        bullet = Bullet(self.x + offset, self.y + offset, math.atan2(mouse_y - (self.y + offset), mouse_x -
                                                                     (self.x + offset)), 10)
        bullets.append(bullet)
