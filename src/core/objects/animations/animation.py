import pygame
from pygame import SurfaceType
from pygame.transform import scale
from src.core.objects.images.image import Image
from src.imports.walk_file import imports_files
import time

class Animation(Image):
    def __init__(self, screen: SurfaceType, folder: str,nowint: int = 0, maxint: int = 1,timer: int = 1, size: tuple[float, float] = None, x: int=0, y: int=0):
        self.images = imports_files(folder)
        self.image = self.images[nowint]
        self.nowint = nowint
        self.maxint = maxint
        self.screen = screen
        self.timer = timer
        super().__init__(self.screen, self.image, size, x, y)

        self.times = time.time()

    def update(self):
        self.nowint = 0 if self.nowint == self.maxint else + 1
        self.image = self.images[self.nowint]

    def draw(self):
        super().draw()
        self.update()