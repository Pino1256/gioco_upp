import arcade
import random

class Ingrandimento (arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("./assetss/ingrandimento.png", scale = 1)

        self.percentuale_spawn: int = 0.10
        self.scle_plus: int = 0.2

        self.center_x = x
        self.center_y = y