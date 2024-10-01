from src.core.scene.core.scene import Scene
from src.core.scene.core.save_scene import *

class SceneManager(Scene):
    def __init__(self):
        super(SceneManager, self).__init__()
        self.current_scene = Scene()
        self.scene_type = ["run","menu", "game"]

    def set_current_scene(self,scene):
        self.current_scene.on_exit()
        self.current_scene = scene

    def switch_scene(self, type):
        self.current_scene.on_exit()
        match type:
            case "run":
                self.current_scene = get_scene("run")
            case "menu":
                self.current_scene = get_scene("menu")
            case "game":
                self.current_scene = get_scene("game")
        self.current_scene.on_enter()

    def on_enter(self):
        self.current_scene.on_enter()

    def on_update(self):
        self.current_scene.on_update()

    def on_draw(self):
        self.current_scene.on_draw()

    def on_input(self, event):
        self.current_scene.on_input(event)

    def on_exit(self):
        self.current_scene.on_exit()

    def update_surface(self):
        self.current_scene.update_surface()