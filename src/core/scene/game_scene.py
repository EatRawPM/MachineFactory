from src.core.scene.core.scene import Scene
from src.core.scene.core.save_scene import *
from src.core.map.ground import Ground
import pygame

pygame.init()

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.scene_manager = get_scene('manager')
        self.ground_map = Ground()

    def on_enter(self):
        self.ground_map.on_enter()

    def on_update(self):
        self.ground_map.on_update()

    def on_input(self, event):
        self.ground_map.on_input(event)

    def on_draw(self):
        self.surface.fill('white')
        self.ground_map.on_draw()

    def on_exit(self):
        self.ground_map.on_exit()