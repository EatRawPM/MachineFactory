import pygame

class SurfaceBase:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.width = self.display_surface.get_width()
        self.height = self.display_surface.get_height()

        self.half_width = self.width / 2
        self.half_height = self.height / 2

    def update_surface(self):
        self.display_surface = pygame.display.get_surface()
        self.width = self.display_surface.get_width()
        self.height = self.display_surface.get_height()

        self.half_width = self.width / 2
        self.half_height = self.height / 2