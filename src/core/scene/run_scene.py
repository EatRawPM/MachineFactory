from time import time

from src.core.scene.core.scene import Scene
from src.core.scene.core.save_scene import *


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

    def on_draw(self): ...

    def on_exit(self): ...