from src.core.scene.scene import Scene
from src.core.tool.draw import draw_text
from src.core.scene.save_scene import *
from src.core.map.ground import Ground
from pygame import KEYDOWN
import pygame

pygame.init()

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.scene_manager = get_scene('manager')
        self.ground_map = Ground()

    def on_enter(self):
        print('进入游戏')

    def on_update(self):
        print('游戏正在运行')

    def on_input(self, event):
        if event.type == KEYDOWN:
            pass
        self.ground_map.on_input(event)

    def on_draw(self):
        self.surface.fill('white')
        self.ground_map.on_draw()

    def on_exit(self):
        print('退出游戏')