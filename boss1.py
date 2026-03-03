import arcade
from nemico_globale import Enemy_general
from barra_vita import BarraVita

class Boss1(Enemy_general):
    def __init__(self):

        super().__init__("./assetss/boss1.png", scale = 0.2, velocita_nemico = 2, vita = 50)

        self.max_vita = self.vita

        # Barra sopra la testa (posizione iniziale)
        self.barra_vita_boss = BarraVita(
            max_health=self.max_vita,
            x=self.center_x,
            y=self.center_y + 60
        )

    def update_bar(self):
        # La barra segue il boss
        self.barra_vita_boss.x = self.center_x
        self.barra_vita_boss.y = self.center_y + 60
        self.barra_vita_boss.cur_health = self.vita

    def take_damage(self, amount):
        self.vita -= amount
        self.barra_vita_boss.cur_health = self.vita
