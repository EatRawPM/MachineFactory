import pygame
from src.core.map.core.map import Map
from src.core.entity.player import Player
from pygame.math import Vector2 as vec2
from src.core.tool.draw import draw_text

class Ground(Map):
    def __init__(self):
        super().__init__()
        #窗口
        self.display_surface = pygame.display.get_surface()
        self.width = self.display_surface.get_width()
        self.height = self.display_surface.get_height()

        self.lines_surface = pygame.Surface((self.width, self.height))
        self.lines_surface.set_colorkey('green')
        self.lines_surface.set_alpha(60)

        self.half_width = self.width / 2
        self.half_height = self.height / 2

        #模式
        self.is_create = False
        self.is_delete = False

        self.scale = 1.0

        self.size = 64

        self.origin = vec2(self.half_width, self.half_height)

        self.offset = vec2(0, 0)

        self.mouse_world_pos = vec2(0, 0)

        self.player = Player()

    def on_enter(self): ...

    def on_draw(self):
        if self.is_create:
            # pygame.draw.circle(self.lines_surface, 'green', self.origin, 10*self.scale)
            self.draw_lines('black')
        if self.is_delete:
            # pygame.draw.circle(self.lines_surface, 'red', self.origin, 10*self.scale)
            self.draw_lines('red')
        self.player.draw()
        draw_text(f'x: {self.player.x} y: {self.player.y}', color='black', size=20)
        draw_text(f'size: {self.scale}', color='black', size=20, y=30)
        draw_text(f'mouse: {self.mouse_world_pos}', color='black', size=20, y=50)

    def draw_lines(self, color):
        cols = self.width // self.size
        rows = self.height // self.size

        offset_offset = vec2(x = self.origin.x - int(self.origin.x / self.size) * self.size,
                             y = self.origin.y - int(self.origin.y / self.size) * self.size)

        self.lines_surface.fill('green')

        for col in range(cols):
            x = (offset_offset.x + self.size / 2) + col * self.size
            pygame.draw.line(self.lines_surface, color, (x, 0), (x, self.height))

        for row in range(rows):
            y = (offset_offset.y + self.size / 2) + row * self.size
            pygame.draw.line(self.lines_surface, color, (0, y), (self.width, y))

        self.display_surface.blit(self.lines_surface, (0, 0))

    def get_world_pos(self, x, y) -> vec2:
        scale = 64 / (self.scale * 64)

        distance = (vec2(x, y) - self.origin) * scale

        col = int((distance.x + 32) / 64)
        row = int((distance.y + 32) / 64)

        col -= 1 if distance.x < -self.size / 2 else 0
        row -= 1 if distance.y < -self.size / 2 else 0

        return vec2(col, row)

    def on_update(self):
        self.size = int(64 * self.scale)
        self.offset = vec2(-self.player.x, -self.player.y)

        scale_offset = vec2(self.offset.x * self.scale, self.offset.y * self.scale)

        self.origin = vec2(self.half_width, self.half_height) + scale_offset

        self.mouse_world_pos = self.get_world_pos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        self.player.update(self.scale)

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