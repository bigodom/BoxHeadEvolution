import pygame


class Level:
    def __init__(self):
        # get the display surface
        self.display = pygame.display.get_surface()

        # sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        pass
