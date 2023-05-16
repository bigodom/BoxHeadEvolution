import pygame

from settings import WORLD_MAP


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups setup
        self.visible_sprites = pygame.sprite.Group()
        self.invisible_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            print(row_index, row)

    def run(self):
        pass