import pygame

from src.core.map.map import Map
from pygame.math import Vector2 as vec2

class Ground(Map):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.origin = vec2(1280/2, 720/2)

    def on_draw(self):
        pygame.draw.circle(self.surface, 'red', self.origin, 10)