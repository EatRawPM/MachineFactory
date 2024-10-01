from time import time
from src.core.tool.draw import draw_text
from src.core.scene.core.scene import Scene
from src.core.scene.core.save_scene import *

import pygame

class RunScene(Scene):
    def __init__(self):
        super().__init__()
        self.scene_manager = get_scene('manager')

        self._time = time()
        self.times = 0

    def on_enter(self): ...

    def on_update(self):
        clock = time() - self._time
        self.times += clock
        self._time = time()
        if self.times >= 3:
            self.scene_manager.switch_scene('menu')

    def on_input(self, event): ...

    def on_draw(self):
        draw_text('操做提示',x=int(self.half_width - 75), y=int(self.half_height - 200))
        draw_text('WASD移动',x=int(self.half_width - 75), y=int(self.half_height - 150))
        draw_text('滚轮缩放',x=int(self.half_width - 75), y=int(self.half_height - 100))
        draw_text('q键删除', x=int(self.half_width - 75), y=int(self.half_height - 50))
        draw_text('e键建造', x=int(self.half_width - 75), y=int(self.half_height))
        draw_text('esc退出', x=int(self.half_width - 75), y=int(self.half_height + 50))

    def on_exit(self): ...

    def update_surface(self):
        super().update_surface()