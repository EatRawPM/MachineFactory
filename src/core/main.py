from src.core.scene.run_scene import RunScene
from src.core.scene.menu_scene import MenuScene
from src.core.scene.game_scene import GameScene
from src.core.scene.scene_manager import SceneManager
from src.core.scene.save_scene import *
from src.core.objects.animations.animation import Animation
from src.data.assets import icon_image
import sys
import pygame

save_init()

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('MachineFactory')
        pygame.display.set_icon(icon_image)

        set_scene('manager', SceneManager())
        set_scene('menu', MenuScene())
        set_scene('run', RunScene())
        set_scene('game', GameScene())

        self.surface_display = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

        self.scene_manager = get_scene('manager')
        self.run_scene = get_scene('run')
        self.menu_scene = get_scene('menu')
        self.game_scene = get_scene('game')

    def update(self):
        self.scene_manager.on_update()
        self.clock.tick(60)
        self.surface_display.fill('black')
        self.scene_manager.on_draw()
        pygame.display.update()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.scene_manager.on_exit()
                pygame.quit()
                sys.exit()
            self.scene_manager.on_input(event)

    def run(self):
        self.scene_manager.set_current_scene(get_scene('run'))
        self.scene_manager.on_enter()
        while True:
            self.update()
            self.handle_event()