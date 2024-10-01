from src.surface.SurfaceBase import SurfaceBase

class UI(SurfaceBase):
    def __init__(self):
        super().__init__()
    def draw(self): ...
    def update_surface(self):
        super().update_surface()