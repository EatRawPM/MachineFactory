from pygame.math import Vector2 as vec2
from pygame.draw import circle
from src.core.entity.core.entity import Entity
import pygame

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.width = self.display_surface.get_width()
        self.height = self.display_surface.get_height()

        self.half_width = self.width / 2
        self.half_height = self.height / 2

        self.pos = (self.half_width, self.half_height)

        self.half_width = self.width / 2
        self.half_height = self.height / 2

        self.direction = vec2(0, 0)
        self.speed = 2

        self.x = 0
        self.col = 0

        self.y = 0
        self.row = 0

        self.scale = 1.0

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def draw(self):
        circle(self.display_surface, 'black', self.pos, 10*self.scale)

    def update(self, scale):
        self.scale = scale

        self.speed = 2 * self.scale

        self.x += self.direction.x * self.speed
        self.y += self.direction.y * self.speed