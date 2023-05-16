import pygame
import math
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = 0

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def update_angle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angle = math.atan2(mouse_y - self.y, mouse_x - self.x)

    def draw(self, screen):
        pygame.draw.rect(screen, 'Red', pygame.Rect(self.x, self.y, 20, 20))
