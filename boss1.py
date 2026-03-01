import arcade
from nemico_globale import Enemy_general
from barra_vita import BarraVita

class Boss1(Enemy_general,BarraVita):
    def __init__(self):

        super().__init__("./assetss/boss1.png", scale = 0.2, velocita_nemico = 2, vita = 50)

        self.barra_vita = BarraVita(max_health=100, x=515, y=self.center_y + 20)
