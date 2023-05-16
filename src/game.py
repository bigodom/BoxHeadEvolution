import math
from sys import exit

import pygame
import sys

from bullet import Bullet
from level import Level
from player import Player
from settings import *


class Game:
    def __init__(self):
        # initialize pygame
        self.clock = pygame.time.Clock()
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
        self.is_shooting = False

        # initialize the level
        self.level = Level()

        # some settings
        self.font = pygame.font.Font(None, 30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                self.is_shooting = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
                self.is_shooting = False
        return True

    def update(self):
        # verify if keys get pressed
        keys = pygame.key.get_pressed()

        # move the player
        self.player.move(keys)

        # shoot a bullet

        for bullet in self.bullets:
            bullet.update()

        if self.is_shooting:
            self.player.shoot(self.bullets)

        return True

    def draw(self):
        # Render the screen
        self.screen.fill('Blue')

        # Draw the player
        self.player.draw(self.screen)

        # update the bullet
        for bullet in self.bullets:
            bullet.draw(self.screen)

        # draw the fps
        fps_text = self.font.render("FPS: {}".format(int(self.clock.get_fps())), True, (255, 255, 255))
        self.screen.blit(fps_text, (100, 10))

    def run(self, player_speed=None):
        # initialize the game loop
        clock = pygame.time.Clock()
        running = True

        while running:
            self.clock.tick(FPS)

            running = self.handle_events()

            if not self.update():
                break

            self.draw()

            pygame.display.flip()

        pygame.quit()
