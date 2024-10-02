import pygame
from PyInstaller.utils.hooks.setuptools import pre_safe_import_module

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
        self.is_create = True
        self.is_delete = False

        self.scale = 1.0

        self.size = 64

        self.origin = vec2(self.half_width, self.half_height)

        self.offset = vec2(0, 0)

        self.mouse_pos = vec2(0, 0)

        self.col = 0
        self.row = 0

        self.player = Player()

        self.block_list = {}

    def on_enter(self): ...

    def on_draw(self):

        self.draw_block()
        if self.is_create:
            self.draw_lines('black')
            self.up_draw_block('green')
        if self.is_delete:
            self.draw_lines('red')
            self.up_draw_block('red')
        pygame.draw.circle(self.display_surface, 'green', self.origin, 10 * self.scale)
        self.player.draw()
        draw_text(f'x: {self.player.x} y: {self.player.y}', color='black', size=20)
        draw_text(f'col: {self.player.col} row: {self.player.row}', color='black', size=20, y=30)
        draw_text(f'size: {self.scale}', color='black', size=20, y=50)
        draw_text(f'col: {self.col} row: {self.row}', color='black', size=20, y=70)

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

    def get_world_pos(self, distance: vec2):
        scale = 64 / (self.scale * 64)

        col = int((distance.x + 32) / 64)
        row = int((distance.y + 32) / 64)

        col -= 1 if distance.x < -64 / 2 else 0
        row -= 1 if distance.y < -64 / 2 else 0

        return col, row

    def on_update(self):
        self.size = int(64 * self.scale)
        self.offset = vec2(-self.player.x, -self.player.y)

        scale_offset = vec2(self.offset.x * self.scale, self.offset.y * self.scale)

        self.origin = vec2(self.half_width, self.half_height) + scale_offset

        scale = 64 / (self.scale * 64)

        self.mouse_pos = (vec2(pygame.mouse.get_pos()) - self.origin) * scale

        self.col, self.row = self.get_world_pos(self.mouse_pos)

        self.player.update(self.scale)

        self.player.col, self.player.row = self.get_world_pos(vec2(self.player.x, self.player.y))

    def up_draw_block(self, color: str | tuple[int, int, int]):
        x = self.col * self.size + self.origin.x - self.size / 2
        y = self.row * self.size + self.origin.y - self.size / 2

        surface = pygame.Surface((self.size, self.size))
        surface.fill(color)
        surface.set_alpha(30)
        rect = surface.get_rect()
        rect.topleft = (x, y)

        self.display_surface.blit(surface, rect)

    def draw_block(self):
        def create():
            if state != 'null':
                x = col * self.size + self.origin.x - self.size / 2
                y = row * self.size + self.origin.y - self.size / 2

                surface = pygame.Surface((self.size, self.size))
                surface.fill('yellow')
                rect = surface.get_rect()
                rect.topleft = (x, y)

                self.display_surface.blit(surface, rect)

        for keys, values in self.block_list.items():
            col = keys[0]
            row = keys[1]
            state = ''
            for key, value in values.items():
                match key:
                    case 'state':
                        state = value

            create()

    def add_block(self):
        cell = (self.col, self.row)
        def read_dirt():
            if not self.block_list[cell]:
                self.block_list[cell] = {'state': 'Cell'}
            else:
                pass

        if cell in self.block_list:
            read_dirt()
        else:
            self.block_list[cell] = {}
            read_dirt()

    def remove_block(self):
        cell = (self.col, self.row)

        if cell in self.block_list:
            self.block_list[cell] = {'state': 'null'}

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
        self.mouse_event()

    def scale_event(self,event):
        if event.type == pygame.MOUSEWHEEL:
            self.scale += event.y * 0.25
        self.scale = max(0.5, min(self.scale, 2.0))

    def mouse_event(self):
        if pygame.mouse.get_pressed()[0]:
            if self.is_create:
                self.add_block()
            if self.is_delete:
                self.remove_block()

    def on_exit(self): ...

    def update_surface(self):
        super().update_surface()