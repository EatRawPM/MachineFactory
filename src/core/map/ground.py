from src.core.map.map import Map

class Ground(Map):
    def __init__(self):
        super().__init__()

    def on_draw(self): ...