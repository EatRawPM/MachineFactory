import pygame
from src.core.map.map import Map
from src.core.entity.player import Player
from pygame.math import Vector2 as vec2

class Ground(Map):
    def __init__(self):
        super().__init__()
        #窗口
        self.display_surface = pygame.display.get_surface()
        self.width = self.display_surface.get_width()
        self.height = self.display_surface.get_height()

        self.half_width = self.width / 2
        self.half_height = self.height / 2

        #模式
        self.is_create = True
        self.is_delete = False

        self.scale = 1.0

        self.size = 64

        self.origin = vec2(self.half_width, self.half_height)

        self.offset = vec2(0, 0)

        self.player = Player()

    def on_enter(self): ...

    def on_draw(self):
        if self.is_create:
            pygame.draw.circle(self.display_surface, 'green', self.origin, 10*self.scale)
            self.draw_lines('black')
        if self.is_delete:
            pygame.draw.circle(self.display_surface, 'red', self.origin, 10*self.scale)
            self.draw_lines('red')
        self.player.draw()

    def draw_lines(self, color):
        cols = self.width // self.size
        rows = self.height // self.size

        offset_offset = vec2(x = self.origin.x - int(self.origin.x / self.size) * self.size,
                             y = self.origin.y - int(self.origin.y / self.size) * self.size)

        for col in range(cols):
            x = (offset_offset.x + self.size / 2) + col * self.size
            pygame.draw.line(self.display_surface, color, (x, 0), (x, self.height))

        for row in range(rows):
            y = (offset_offset.y + self.size / 2) + row * self.size
            pygame.draw.line(self.display_surface, color, (0, y), (self.width, y))

    def on_update(self):
        self.size = int(64 * self.scale)
        self.offset = (-self.player.x, -self.player.y)

        self.origin = vec2(self.half_width, self.half_height) + self.offset

        self.player.update(self.scale, self.size)

    def on_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if self.is_create:
                    self.is_create = False
                else:
                    self.is_create = True
                    self.is_delete = False
            if event.key == pygame.K_q:
                if self.is_delete:
                    self.is_delete = False
                else:
                    self.is_delete = True
                    self.is_create = False
        self.player.input()
        self.scale_event(event)

    def scale_event(self,event):
        if event.type == pygame.MOUSEWHEEL:
            self.scale += event.y * 0.25
        self.scale = max(0.5, min(self.scale, 2.0))

    def on_exit(self): ...