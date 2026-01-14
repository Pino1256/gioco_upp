import arcade
import random
import math

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
velocita_nemico = 2

class Enemy(arcade.Sprite):
    def __init__(self):

        super().__init__("./assetss/nemico.png", scale=0.09)

        # Spawna su un bordo casuale dello schermo con un margine
        self.margin = -50
        self.edge = random.randint(0,3)

        if self.edge == 0:  # alto
            self.center_x = random.randint(self.margin, SCREEN_WIDTH - self.margin)
            self.center_y = SCREEN_HEIGHT - self.margin
        elif self.edge == 1:  # destra
            self.center_x = SCREEN_WIDTH - self.margin
            self.center_y = random.randint(self.margin, SCREEN_HEIGHT - self.margin)
        elif self.edge == 2:  # basso
            self.center_x = random.randint(self.margin, SCREEN_WIDTH - self.margin)
            self.center_y = self.margin
        elif self.edge == 3:  # sinistra
            self.center_x = self.margin
            self.center_y = random.randint(self.margin, SCREEN_HEIGHT - self.margin)

    def movimento_verso_giocatore(self, player_x, player_y):
        # calcola la direzione verso il personaggio
        direzione_x = player_x - self.center_x
        direzione_y = player_y - self.center_y
        distanza = math.hypot(direzione_x,direzione_y) # calcola l'ipotenusa

        if distanza > 0:
            self.center_x += velocita_nemico * (direzione_x / distanza)
            self.center_y += velocita_nemico * (direzione_y / distanza)
