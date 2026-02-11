import arcade
from nemico_globale import Enemy_general

class Enemy_2(Enemy_general):
    def __init__(self):
        super().__init__("./assetss/pipistrello.png", scale=0.09, velocita_nemico = 3, vita= 20 )