import math
from sys import exit

import pygame
import sys

from bullet import Bullet
from player import Player
from settings import *


class Game:
    def __init__(self):
        # initialize pygame
        pygame.init()

        # initialize the screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        # initialize the player
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT // 2
        self.player_speed = 5
        self.player = Player(self.player_x, self.player_y, self.player_speed)

        # initialize the bullet
        self.bullets = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self):
        # verify if keys get pressed
        keys = pygame.key.get_pressed()

        # move the player
        self.player.move(keys)

        # shoot a bullet
        if keys[pygame.K_SPACE]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet = Bullet(self.player.x + 25, self.player.y + 25, math.atan2(mouse_y - self.player.y, mouse_x -
                                                                               self.player.x), 10)
            self.bullets.append(bullet)

        for bullet in self.bullets:
            bullet.update()

        return True

    def draw(self):
        # Render the screen
        self.screen.fill('Blue')

        # Draw the player
        self.player.draw(self.screen)

        # update the bullet
        for bullet in self.bullets:
            bullet.draw(self.screen)

        pygame.display.flip()

    def run(self, player_speed=None):
        # initialize the game loop
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(FPS)

            running = self.handle_events()

            if not self.update():
                break

            self.draw()

        pygame.quit()
