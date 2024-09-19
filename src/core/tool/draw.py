import pygame
from src.data.assets import default_font_path

pygame.init()

def draw_text(text, font: str = default_font_path, color: str | tuple[int, int, int] | tuple[int, int, int, int] = 'white', x: int = 10, y: int = 10, size: int = 30):
    surface = pygame.display.get_surface()
    Font = pygame.font.Font(font, size)
    surf_font = Font.render(str(text), True, color)
    surface.blit(surf_font, (x, y))