import pygame
from pygame import SurfaceType
from pygame.sprite import Sprite
from pygame.transform import scale

class Image(Sprite):
    def __init__(self, screen: SurfaceType, path: str | SurfaceType, size: tuple[float, float] = None, x: int=0, y: int=0):
        super().__init__()
        self.screen = screen
        if type(path) == SurfaceType:
            self.image = path
        else:
            self.image = pygame.image.load(path).convert_alpha()
        print(self.image)
        if size is None:
            self.size = self.image.get_size()[0], self.image.get_size()[1]
        else:
            self.size = size
        self.image = scale(self.image, self.size)

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x, y

    def draw(self):
        self.screen.blit(self.image, self.rect)