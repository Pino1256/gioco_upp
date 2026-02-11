import arcade
import random
import math

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

class Enemy_general(arcade.Sprite):
    def __init__(self, image_file, scale, velocita_nemico, vita):
        
        super().__init__(image_file, scale)

        self.velocita_nemico = velocita_nemico
        self.vita = vita
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
            self.center_x += self.velocita_nemico * (direzione_x / distanza)
            self.center_y += self.velocita_nemico * (direzione_y / distanza)