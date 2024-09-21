import pygame
from src.core.map.map import Map
from pygame.math import Vector2 as vec2

class Ground(Map):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()

        self.origin = vec2(0, 0)
        self.direction = vec2(0, 0)
        self.speed = 20

        self.yan = vec2(1280 / 2, 720 / 2)

        self.origins = 1.0
        self.size = int(64 * self.origins)

        self.z_y = 720 - (self.yan.y + self.size / 2)
        self.f_y = self.yan.y - self.size / 2

        self.z_x = 1280 - (self.yan.x + self.size / 2)
        self.f_x = self.yan.x - self.size / 2

        self.is_create = False
        self.is_delete = False
    def on_enter(self): ...
    def draw_lines(self, color: str):
        for i in range(int(self.z_y / self.size + 1)):
            pygame.draw.line(self.surface, color, (0, self.yan.y + self.size / 2 + i * self.size), (1280, self.yan.y + self.size / 2 + i * self.size))
        for i in range(int(self.f_y / self.size + 1)):
            pygame.draw.line(self.surface, color, (0, self.yan.y - self.size / 2 - i * self.size), (1280, self.yan.y - self.size / 2 - i * self.size))

        for i in range(int(self.z_x / self.size + 1)):
            pygame.draw.line(self.surface, color, (self.yan.x + self.size / 2 + i * self.size, 0), (self.yan.x + self.size / 2 + i * self.size, 720))
        for i in range(int(self.f_x / self.size + 1)):
            pygame.draw.line(self.surface, color, (self.yan.x - self.size / 2 - i * self.size, 0), (self.yan.x - self.size / 2 - i * self.size, 720))
    def on_update(self):
        self.origin += self.direction
        self.size = int(64 * self.origins)

        self.z_y = 720 - (self.yan.y + self.size / 2)
        self.f_y = self.yan.y - self.size / 2

        self.z_x = 1280 - (self.yan.x + self.size / 2)
        self.f_x = self.yan.x - self.size / 2

        self.yan = vec2(1280 / 2, 720 / 2) + (-self.origin * self.speed)
    def on_draw(self):
        if self.is_create:
            pygame.draw.circle(self.surface, 'green', self.yan, 10)
            self.draw_lines('black')
        if self.is_delete:
            pygame.draw.circle(self.surface, 'red', self.yan, 10)
            self.draw_lines('red')
    def on_input(self, event):
        def input():
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
        if event.type == pygame.MOUSEWHEEL:
            if self.origins <= 0.5 and event.y == -1:
                self.origins = 0.5
            elif self.origins >= 2.0 and event.y == 1:
                self.origins = 2.0
            else:
                self.origins += event.y * 0.25
        input()
    def on_exit(self): ...