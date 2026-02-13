import arcade
from nemico_globale import Enemy_general

class Enemy(Enemy_general):
    def __init__(self):

        super().__init__("./assetss/nemicocompresso.png", scale = 0.2, velocita_nemico = 2, vita = 10)
