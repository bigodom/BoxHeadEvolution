import pygame

from settings import WORLD_MAP


class Level:
    def __init__(self):
        # get the display surface
        self.display = pygame.display.get_surface()

        # sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    # create the map
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            print(row_index)
            print(row)

    def run(self):
        pass
