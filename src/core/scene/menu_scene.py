from src.core.scene.scene import Scene
from src.core.tool.draw import draw_text
from src.core.scene.save_scene import *
from pygame import KEYDOWN

class MenuScene(Scene):
    def __init__(self):
        super().__init__()
        self.scene_manager = get_scene('manager')

    def on_enter(self):
        print('进入主页面')

    def on_update(self):
        print('主页面正在运行')

    def on_input(self, event):
        if event.type == KEYDOWN:
            self.scene_manager.switch_scene('game')

    def on_draw(self):
        draw_text('主页面绘图')

    def on_exit(self):
        print('退出主页面')