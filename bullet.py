import arcade
import random
import math
import time

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

class Bullet(arcade.Sprite):
    def __init__ (self, player):
        super().__init__("./assetss/power.png", scale = 0.2)

        self.center_x = player.center_x
        self.center_y = player.center_y

        self.angolo = random.uniform(0, 360)
        self.angolo_rad = math.radians(self.angolo)
        self.distanza = random.randint(100, 350)

        self.speed = 15

    def update(self, delta_time: float = 1/60):
        self.center_x += math.cos(self.angolo_rad) * self.speed
        self.center_y += math.sin(self.angolo_rad) * self.speed
    
