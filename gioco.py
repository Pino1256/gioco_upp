import arcade
import random
import math
from enemy import Enemy
from bullet import Bullet
from enemy_2 import Enemy_2
import time
from barra_vita import BarraVita

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

class giocone(arcade.Window):
    def __init__(self, larghezza, altezza, titolo):
        super().__init__(larghezza, altezza, titolo)

        arcade.set_background_color(arcade.color.WHITE)

        self.nemico = None
        self.lista_nemico = arcade.SpriteList()
        self.numero_da_spawnare = 1
        self.nemici_morti: int = 0
        self.nemici_da_killare: int = 5

        self.pipistrello = None
        self.lista_pipistrello = arcade.SpriteList()

        self.potere = None
        self.lista_potere = arcade.SpriteList()

        self.personaggio = None
        self.lista_personaggio = arcade.SpriteList()
        self.livello_personaggio: int = 1
        self.livello: int = 2

        # alcune cose di bomba
        self.lista_bomba = arcade.SpriteList()

        # movimento
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.M_pressed = False

        self.velocita = 5
        self.vita_personaggio = 100

        # Timer per lo spawn dei nemici
        self.time_since_spawn = 0
        self.time_since_spawn_2 = 0
        self.spawn_rate = 5.0  # Un nemico ogni 5 secondi
        self.spawn_rate_2 = 2.0 #un pipistrello ogni 2 secondi

        self.camera = arcade.camera.Camera2D()

        self.ui_camera = arcade.camera.Camera2D()

        self.barra_vita = BarraVita(max_health=100, x=20, y=self.height - 40)

        self.setup()

    def setup(self): # player

        self.personaggio = arcade.Sprite("./assetss/persona.png")
        self.personaggio.center_x = 300
        self.personaggio.center_y = 100
        self.personaggio.scale = 0.08
        self.lista_personaggio.append(self.personaggio)
    
    def bomba(self): # abilita del player bomba

        c4 = arcade.Sprite("./assetss/bomb.png")
        c4.center_x = self.personaggio.center_x
        c4.center_y = self.personaggio.center_y
        c4.time_created = time.time()
        c4.scale = 0.3
        self.lista_bomba.append(c4)
            
    def on_draw(self):

        self.clear()

        self.camera.use()
        self.lista_nemico.draw()
        self.lista_personaggio.draw()
        self.lista_pipistrello.draw()
        self.lista_bomba.draw()
        self.lista_potere.draw()

        self.ui_camera.use()
        arcade.draw_text(f"vita: {self.vita_personaggio}", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 20)

        self.ui_camera.use()
        arcade.draw_text(f"punteggio: {self.nemici_morti}", 10, SCREEN_HEIGHT - 50, arcade.color.BLACK, 20)

        self.ui_camera.use()
        arcade.draw_text(f"livello: {self.livello_personaggio}", 10, SCREEN_HEIGHT - 70, arcade.color.BLACK, 20)

        self.ui_camera.use()
        self.barra_vita.draw_health_bar()
        self.barra_vita.draw_health_number()



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
            self.personaggio.scale = (0.08, 0.08)
        elif change_x > 0:
            self.personaggio.scale = (-0.08, 0.08)

        #aumento del livello del personaggio
        if self.nemici_morti >= self.nemici_da_killare:
            self.nemici_da_killare += 5
            self.livello_personaggio +=1

        # Livello del personaggio + nemici in più
        if self.livello_personaggio == self.livello:
            self.livello = self.livello_personaggio + 2
            self.numero_da_spawnare += 2

        # Spawn dei nemici 1
        self.time_since_spawn += delta_time
        if self.time_since_spawn >= self.spawn_rate:
            for _ in range(self.numero_da_spawnare):
                enemy = Enemy()
                self.lista_nemico.append(enemy)
            self.time_since_spawn = 0

        # Spawn dei nemici 2
        self.time_since_spawn_2 += delta_time
        if self.time_since_spawn_2 >= self.spawn_rate_2:
            enemy_2 = Enemy_2()
            self.lista_pipistrello.append(enemy_2)
            self.time_since_spawn_2 = 0
        
        for enemy in self.lista_nemico:
            enemy.movimento_verso_giocatore(self.personaggio.center_x, self.personaggio.center_y)

        for enemy_2 in self.lista_pipistrello:
            enemy_2.movimento_verso_giocatore(self.personaggio.center_x, self.personaggio.center_y)
        
        self.barra_vita.cur_health = self.vita_personaggio

        for enemy in self.lista_nemico[:]:

            #controlla collisioni con il personaggio
            if arcade.check_for_collision(enemy, self.personaggio):
                self.vita_personaggio -= 1
                enemy.kill()
                self.nemici_morti += 1
                if self.vita_personaggio == 0:
                    arcade.close_window()

        self.lista_potere.update()
        
        tempo_attuale = time.time()

        for proiettile in self.lista_potere[:]:
            for enemy in self.lista_nemico[:]:
                if arcade.check_for_collision(proiettile, enemy):
                    enemy.kill()
                    proiettile.kill()
                    self.nemici_morti += 1

        for bomba in self.lista_bomba[:]:
            for enemy in self.lista_nemico[:]:
                if arcade.check_for_collision(bomba, enemy):
                    enemy.kill()
                    self.nemici_morti += 1

        for c4 in self.lista_bomba:
            if tempo_attuale - c4.time_created >= 2:
                c4.remove_from_sprite_lists()
                for enemy in self.lista_nemico[:]:
                    distanza = arcade.get_distance_between_sprites(c4, enemy)
                    if distanza <= 250:
                        enemy.kill()
                        self.nemici_morti += 1

        self.camera.position = self.personaggio.center_x, self.personaggio.center_y                


    def on_key_press(self, tasto, modificatori):

        if tasto in (arcade.key.UP, arcade.key.W):
            self.up_pressed = True
        elif tasto in (arcade.key.DOWN, arcade.key.S):
            self.down_pressed = True
        elif tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = True
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = True
        elif tasto == arcade.key.Z:
            self.bomba()
        elif tasto == arcade.key.Q:
            self.Q_pressed = True
            proiettile = Bullet(self.personaggio)
            self.lista_potere.append(proiettile)
            
        
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
        elif tasto == arcade.key.Q:
            self.Q_pressed = False    

def main():

    gioco = giocone(SCREEN_WIDTH, SCREEN_HEIGHT, "non è babbo")
    arcade.run()

if __name__ == "__main__":
    main()