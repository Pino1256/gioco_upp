import arcade
import random

class Cura (arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("./assetss/cura.png", scale = 1)

        self.durata: int = 4
        self.percentuale_spawn: int = 0.10
        self.quant_cura: int = 30

        self.center_x = x
        self.center_y = y
