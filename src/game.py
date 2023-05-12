from sys import exit

import pygame
import sys

from level import Level
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.running = True
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT // 2
        self.player_speed = 5

    def run(self, player_speed=None):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.player_x -= self.player_speed
            if keys[pygame.K_RIGHT]:
                self.player_x += self.player_speed
            if keys[pygame.K_UP]:
                self.player_y -= self.player_speed
            if keys[pygame.K_DOWN]:
                self.player_y += self.player_speed

            # Render the screen
            self.screen.fill('Black')
            self.level.run()
            pygame.draw.rect(self.screen, (0, 0, 255),
                             pygame.Rect(self.player_x, self.player_y, 50, 50))  # Retângulo representando o personagem
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()
        exit()
