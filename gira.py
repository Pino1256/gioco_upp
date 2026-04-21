import arcade
import random
import math
import time

class AbilitaGira (arcade.Sprite):
    def __init__(self, player, scala = 0.5):
        super().__init__("./assetss/spada.png", scale = scala)

        self.player = player

        self.danno_spada = 10
        self.raggio = 100
        self.velocita_rot = 100

        self.angolo = random.uniform(0, 360)
        self.angolo_rad = math.radians(self.angolo)

        self.time = 0.5

        self.center_x = self.player.center_x + self.raggio
        self.center_y = self.player.center_y + self.raggio
    
    def update(self, delta_time):

        self.angolo += self.velocita_rot * delta_time

        self.angolo_rad = math.radians(self.angolo)

        self.center_x = self.player.center_x + math.cos(self.angolo_rad) * self.raggio
        self.center_y = self.player.center_y + math.sin(self.angolo_rad) * self.raggio