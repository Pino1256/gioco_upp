import arcade
import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
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

class giocone(arcade.Window):
    def __init__(self, larghezza, altezza, titolo):
        super().__init__(larghezza, altezza, titolo)

        self.nemico = None
        self.lista_nemico = arcade.SpriteList()

        self.personaggio = None
        self.lista_personaggio = arcade.SpriteList()

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.M_pressed = False

        self.velocita = 4
        self.vita_personaggio= 5

        # Timer per lo spawn dei nemici
        self.time_since_spawn = 0
        self.spawn_rate = 2.0  # Un nemico ogni 5 secondi

        self.setup()

    def setup(self):

        self.personaggio = arcade.Sprite("./assetss/persona.png")
        self.personaggio.center_x = 300
        self.personaggio.center_y = 100
        self.personaggio.scale = 0.09
        self.lista_personaggio.append(self.personaggio)
    
    def on_draw(self):

        self.clear()
        arcade.draw_text(f"vita: {self.vita_personaggio}", 10, SCREEN_HEIGHT -30, arcade.color.WHITE, 20)
        self.lista_nemico.draw()
        self.lista_personaggio.draw()

    def on_update(self, delta_time):

        # Calcola movimento in base ai tasti premuti
        change_x = 0
        change_y = 0
        
        if self.up_pressed:
            change_y += self.velocita
        if self.down_pressed:
            change_y -= self.velocita
        if self.left_pressed:
            change_x -= self.velocita
        if self.right_pressed:
            change_x += self.velocita
        
        # Applica movimento
        self.personaggio.center_x += change_x
        self.personaggio.center_y += change_y
        
        # Flip orizzontale in base alla direzione
        if change_x < 0: 
            self.personaggio.scale = (0.09, 0.09)
        elif change_x > 0:
            self.personaggio.scale = (-0.09, 0.09)

        # Spawn dei nemici
        self.time_since_spawn += delta_time
        if self.time_since_spawn >= self.spawn_rate:
            enemy = Enemy()
            self.lista_nemico.append(enemy)
            self.time_since_spawn = 0
        
        for enemy in self.lista_nemico:
            enemy.movimento_verso_giocatore(self.personaggio.center_x, self.personaggio.center_y)
        
        for enemy in self.lista_nemico[:]:

            #controlla collisioni con il personaggio
            if arcade.check_for_collision(enemy, self.personaggio):
                self.vita_personaggio -= 1
                enemy.kill()
                if self.vita_personagsgio == 0:
                    arcade.close_window()
                    

    def on_key_press(self, tasto, modificatori):

        if tasto in (arcade.key.UP, arcade.key.W):
            self.up_pressed = True
        elif tasto in (arcade.key.DOWN, arcade.key.S):
            self.down_pressed = True
        elif tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = True
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = True
    
    def on_key_release(self, tasto, modificatori):

        """Gestisce il rilascio dei tasti"""

        if tasto in (arcade.key.UP, arcade.key.W):
            self.up_pressed = False
        elif tasto in (arcade.key.DOWN, arcade.key.S):
            self.down_pressed = False
        elif tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = False
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = False

def main():

    gioco = giocone(SCREEN_WIDTH, SCREEN_HEIGHT, "non è babbo")
    arcade.run()

if __name__ == "__main__":
    main()