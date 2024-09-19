from os.path import join
from pygame.image import load
from src.data.path import base_path

assets_path = join(base_path, 'assets')

image_path = join(assets_path, 'images')
icon_path = join(image_path, 'icons')

fonts_path = join(assets_path, 'fonts')

#images
icon_image = load(join(icon_path, 'icon.png'))

#fonts
default_font_path = join(fonts_path, 'default.ttf')