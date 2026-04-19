import arcade
import random
import math
import time

from enemy import Enemy
from bullet import Bullet

from sprite_animato import SpriteAnimato
from cura import Cura
from barra_vita import BarraVita
# from pausa import PauseView
#from menuLVL import MenuLvlView
from ingrandimento import Ingrandimento
from boss1 import Boss1
from esperienza import Exp
from arcade.gui import (
    UIManager, 
    UITextureButton, 
    UIAnchorLayout, 
    UIView
)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class player(SpriteAnimato):
    def __init__(self):
        super().__init__(scale = 1.50)
        file_animazioni = {
            "su": "assetss/run_up.png",
            "giu": "assetss/run_down.png",
            "destra": "assetss/run_right.png",
            "sinistra": "assetss/run_left.png",
            "fermo" : "assetss/run_idle.png"
        }
    
        for dir, percorso in file_animazioni.items(): #dir = direzione
            self.aggiungi_animazione(
                nome = f"run_{dir}",
                percorso = percorso,
                frame_width = 96,
                frame_height = 80,
                num_frame = 8,
                colonne = 8,
                durata = 1,
                riga = 0
            )
        
        self.direzione = "giu"
        self.change_x = 0
        self.change_y = 0
    
        self.ultima_animazione = ""
    
    def update_animation(self, delta_time):
        if self.change_y > 0:
            self.direzione = "su"
        elif self.change_y < 0:
            self.direzione = "giu"
        elif self.change_x > 0:
            self.direzione = "destra"
        elif self.change_x < 0:
            self.direzione = "sinistra"
        elif self.change_x == 0 and self.change_y == 0:
            self.direzione = "fermo"

        if self.change_x != 0 or self.change_y != 0:
            self.imposta_animazione(f"run_{self.direzione}")
            nuova_anim = f"run_{self.direzione}"
            if self.ultima_animazione != nuova_anim:
                self.imposta_animazione(nuova_anim)
                self.ultima_animazione = nuova_anim
            
        else:
            self.direzione = "fermo"
            self.imposta_animazione(f"run_{self.direzione}")
            nuova_anim = f"run_{self.direzione}"         

        super().update_animation(delta_time)    

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.DARK_GREEN)

        # livelli abilità
        self.lvl_proiettile = 1
        self.lvl_bomba = 1
        self.lvl_corsa = 1
        self.proiettile_lvl = 0

        self.livello_per_vita: int = 3

        self.nemico = None
        self.lista_nemico = arcade.SpriteList()
        self.numero_da_spawnare: int = 1
        
        self.nemici_morti: int = 0
        self.nemici_da_killare: int = 5
        self.enemy_killati_per_exp: int = 0
        self.exp_per_prossimo_livello: int = 5

        # pipistrello
        self.pipistrello = None
        self.lista_pipistrello = arcade.SpriteList()
        self.numero_da_spawnare2: int = 1

        # nemico 3
        self.scheletro = None
        self.lista_scheletro = arcade.SpriteList()
        self.numero_da_spawnare3: int = 1

        # boss 1
        self.boss1 = None
        self.lista_boss1 = arcade.SpriteList()

        self.potere = None
        self.lista_potere = arcade.SpriteList()

        # cura
        self.lista_cura = arcade.SpriteList()

        # ingrandimento
        self.lista_ingrandimento = arcade.SpriteList()

        self.personaggio = None
        self.lista_personaggio = arcade.SpriteList()
        self.logic_spawn_nemy1: bool = True
        self.livello_personaggio: int = 0
        self.livello: int = 2
        self.danno = 2
        self.danno_personaggio: int = 10
        self.logic_proiettile = False
        self.logic_bomba = False
        self.logic_corsa = False

        self.spawn_bomba = False

        self.start_sprite = None
        self.lista_tasto_play = arcade.SpriteList()

        # alcune cose di bomba
        self.lista_bomba = arcade.SpriteList()
        self.esplosione: int = 250
        self.bomba_spawn = 0
        self.temp_spawn_bomba = 4

        # movimento
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.M_pressed = False

        self.velocita = 4.7
        self.vita_personaggio: int = 100

        # Timer per lo spawn dei nemici
        self.time_since_spawn = 0
        self.time_since_spawn_2 = 0
        self.time_since_spawn_3 = 0

        self.potere_spawn: int = 0
        self.temp_spawn_pot = 3
        self.quantita_pot: int = 1

        # tempo per sawn enemy
        self.spawn_rate = 5.0  # Un nemico ogni 5 secondi
        self.spawn_rate_2 = 3.5 #un pipistrello ogni 2 secondi
        self.spawn_rate_3 = 2.5

        self.temp_per_spawn = 2 # livello per abbreviare lo spawn rate del nemicoi 1

        self.temp_danno_boss1 = 1

        self.danno_bomba = 10

        # gestione danni
        # self.ultimo_danno = 0
        self.intervallo_danno = 1.0

        #camera
        self.camera = arcade.camera.Camera2D()
        self.ui_camera = arcade.camera.Camera2D()

        self.barra_vita = BarraVita(max_health=100, x=515, y=self.height - 25, HEALTHBAR_WIDTH = 170, HEALTHBAR_HEIGHT = 20)
        self.exp = Exp(max_exp=self.exp_per_prossimo_livello, x = 10, y = self.height - 25)

        self.spawn_boss1 = True

        self.setup()
        

    def setup(self): # player

        self.personaggio = player()
        self.lista_personaggio.append(self.personaggio)
 
    def bomba(self): # abilita del player bomba

        c4 = arcade.Sprite("./assetss/bomb.png")
        c4.center_x = self.personaggio.center_x
        c4.center_y = self.personaggio.center_y
        c4.time_created = time.time()
        c4.scale = 0.3
        self.lista_bomba.append(c4)

    def spawn_cura(self, x, y):
    
        if random.random() <= 0.1:
            nuova_cura = Cura(x, y)
            self.lista_cura.append(nuova_cura)
    
    def spawn_ingrandimento(self, x, y):
        if random.random() <= 0.1:
            nuovo_ingrandimento = Ingrandimento(x, y)
            self.lista_ingrandimento.append(nuovo_ingrandimento)

    def on_draw(self):

        self.clear()

        self.camera.use()
        self.lista_nemico.draw()
        self.lista_personaggio.draw()
        self.lista_pipistrello.draw()
        self.lista_bomba.draw()
        self.lista_potere.draw()
        self.lista_boss1.draw()
        self.lista_cura.draw()
        self.lista_scheletro.draw()
        self.lista_boss1.draw_hit_boxes(arcade.color.RED, line_thickness=2)
        for boss1 in self.lista_boss1:
            boss1.barra_vita_boss.draw_health_bar()

        self.ui_camera.use()
        arcade.draw_text(f"punteggio: {self.nemici_morti}", 10, SCREEN_HEIGHT - 50, arcade.color.BLACK, 20)
        arcade.draw_text(f"livello: {self.livello_personaggio}", 10, SCREEN_HEIGHT - 70, arcade.color.BLACK, 20)

        # self.ui_camera.use()
        self.barra_vita.draw_health_bar()
        self.barra_vita.draw_health_number()

        # self.ui_camera.use()
        self.exp.draw_exp_bar()
        self.exp.draw_exp_number()



    def on_update(self, delta_time):

        # Calcola movimento in base ai tasti premuti
        cx = 0
        cy = 0

        self.lista_personaggio.update()           # Muove fisicamente il player nello schermo
        self.personaggio.update_animation(delta_time) # Fa muovere le gambe al player

        self.lista_nemico.update_animation(delta_time)
        self.lista_pipistrello.update_animation(delta_time)
        self.lista_scheletro.update_animation(delta_time)

        self.lista_nemico.update(delta_time)
        self.lista_pipistrello.update(delta_time)
        self.lista_scheletro.update(delta_time)
        self.lista_boss1.update(delta_time)

        if self.up_pressed: cy += self.velocita
        if self.down_pressed: cy -= self.velocita
        if self.left_pressed: cx -= self.velocita
        if self.right_pressed: cx += self.velocita
        
        # Applica movimento
        self.personaggio.change_x = cx
        self.personaggio.change_y = cy
        
        # Flip orizzontale in base alla direzione
        if cx < 0: 
            self.personaggio.scale = 1.50
        elif cy > 0:
            self.personaggio.scale = 1.50

        #aumento del livello del personaggio
        if self.enemy_killati_per_exp >= self.exp_per_prossimo_livello:

            self.livello_personaggio +=1
            self.enemy_killati_per_exp = 0
            self.exp_per_prossimo_livello += 3
            self.exp.max_exp = self.exp_per_prossimo_livello
            from menuLVL import MenuLvlView
            self.window.show_view(MenuLvlView(self))

            self.bullet = Bullet(self.personaggio)
            self.bullet.danno_proiettile = self.bullet.danno_proiettile*1.20
            self.danno_bomba = self.danno_bomba*1.20

            if self.livello_personaggio >= self.livello_per_vita:
                self.livello_per_vita += 3
                if self.vita_personaggio >= self.barra_vita.max_health:
                    self.vita_personaggio += 20
                self.barra_vita.max_health += 20  

            if self.livello_personaggio >= 21:
                self.logic_spawn_nemy1 = False

            if self.spawn_rate > 0.5:
                if self.livello_personaggio >= self.temp_per_spawn:
                    self.temp_per_spawn += 2
                    self.spawn_rate -= 0.5
            
        if self.livello_personaggio >= 5:
            self.spawn_bomba = True

        if self.logic_proiettile == True:
            if not((self.temp_spawn_pot == 0.5) and (self.quantita_pot == 3)):
                if self.temp_spawn_pot == 0.5:
                    self.quantita_pot += 1
                    print("quantita proiettili spawnati",self.quantita_pot)
                else:
                    self.temp_spawn_pot -= 0.5
                    print("tempo spawn pot",self.temp_spawn_pot)
                
            self.logic_proiettile =False
            # self.proiettile_lvl += 1
        
        if self.velocita <= 5.6:
            if self.logic_corsa == True:
                print("velocità:", self.velocita)
                self.velocita += 0.3
            self.logic_corsa = False

        if self.logic_bomba == True and self.spawn_bomba == True:
            if self.temp_spawn_bomba == 0.5:
                self.esplosione += 100
                print("esplosione", self.esplosione) 
            else:
                self.temp_spawn_bomba -= 0.5
                print("tempo spawn bomba", self.temp_spawn_bomba)
            
            self.logic_bomba = False
            
        # Livello del personaggio + nemici in più
        if self.livello_personaggio >= self.livello:
            self.livello = self.livello_personaggio + 2
            self.numero_da_spawnare += 2
            self.numero_da_spawnare2 += 2
            self.numero_da_spawnare3 += 2

        # Spawn dei nemici 1
        self.time_since_spawn += delta_time
        if self.logic_spawn_nemy1 == True:
            if self.time_since_spawn >= self.spawn_rate:
                for _ in range(self.numero_da_spawnare):
                    enemy = Enemy()
                    self.lista_nemico.append(enemy)
                self.time_since_spawn = 0

        # #Spawn dei nemici 2
        self.time_since_spawn_2 += delta_time
        if (self.livello_personaggio >= 11) and (self.time_since_spawn_2 >= self.spawn_rate_2):
            for _ in range(self.numero_da_spawnare2):
                from enemy_2 import Enemy_2
                enemy_2 = Enemy_2()
                self.lista_pipistrello.append(enemy_2)
            self.time_since_spawn_2 = 0
        
        # spawn dei nemici 3
        self.time_since_spawn_3 += delta_time
        if (self.livello_personaggio >= 21) and (self.time_since_spawn_3 >= self.spawn_rate_2):
            for _ in range(self.numero_da_spawnare3):
                from enemy3 import Enemy3
                enemy_3 = Enemy3()
                self.lista_scheletro.append(enemy_3)
            self.time_since_spawn_3 = 0
            
        #Spawn boss1
        if (self.livello_personaggio >= 10) and (self.spawn_boss1 == True ):
            boss1 = Boss1()
            self.lista_boss1.append(boss1)
            self.spawn_boss1 = False
        
        # movimento dei nemici verso il giocatore
        for enemy in self.lista_nemico:
            enemy.movimento_verso_giocatore(self.personaggio.center_x, self.personaggio.center_y)

        for enemy_2 in self.lista_pipistrello:
            enemy_2.movimento_verso_giocatore(self.personaggio.center_x, self.personaggio.center_y)

        for enemy_3 in self.lista_scheletro:
            enemy_3.movimento_verso_giocatore(self.personaggio.center_x, self.personaggio.center_y)
            enemy_3.update_animation(delta_time)
        
        for boss1 in self.lista_boss1:
            boss1.movimento_verso_giocatore(self.personaggio.center_x, self.personaggio.center_y)
            boss1.update_bar()
        
        self.barra_vita.cur_health = self.vita_personaggio

        self.exp.cur_exp = self.enemy_killati_per_exp 

        # self.ultimo_danno += delta_time
        tutte_enmy_list = [
            (self.lista_nemico, 5), 
            (self.lista_pipistrello, 10), 
            (self.lista_scheletro, 15)
        ]

        for lista, _ in tutte_enmy_list:
            for nemico in lista:
                nemico.time_since_last_hit_player += delta_time

        for lista, danno in tutte_enmy_list:
            nemici_toccati = arcade.check_for_collision_with_list(self.personaggio, lista)
            
            for nemico in nemici_toccati:
                if nemico.time_since_last_hit_player >= 1.0:
                    self.vita_personaggio -= danno
                    nemico.vita -= self.danno
                    # nemico.take_damage(self.danno)
                    nemico.time_since_last_hit_player = 0.0
                    # nemico.time_since_last_hit = 0.0
                    
                
                # for _ in nemici_toccati:
                # if 
                # nemico.vita -= self.danno
                        
                if nemico.vita <= 0:
                    self.spawn_cura(nemico.center_x, nemico.center_y)
                    self.spawn_ingrandimento(nemico.center_x, nemico.center_y)
                    nemico.kill()
                    self.nemici_morti += 1
                    self.enemy_killati_per_exp += 1

        
        #collisioni con boss 1
        self.temp_danno_boss1 += delta_time
        for boss1 in self.lista_boss1[:]:
            if arcade.check_for_collision(boss1, self.personaggio):
                if self.temp_danno_boss1 >= 1:
                    self.vita_personaggio -= 25
                    self.temp_danno_boss1 = 0
                    boss1.take_damage(self.danno)

                if boss1.vita <= 0:
                    boss1.kill()
                    self.nemici_morti += 10
                    self.enemy_killati_per_exp += 10  

        self.lista_potere.update()
        
        tempo_attuale = time.time()

        self.potere_spawn += delta_time

        # spawn potere
        if self.potere_spawn >= self.temp_spawn_pot:
            for _ in range(self.quantita_pot):
                proiettile = Bullet(self.personaggio)
                self.lista_potere.append(proiettile)
            self.potere_spawn = 0

        self.bomba_spawn += delta_time

        # spawn bomba
        if self.spawn_bomba == True:
            if self.bomba_spawn >= self.temp_spawn_bomba:
                self.bomba()
                self.bomba_spawn = 0

        # collisione con il proiettile
        for proiettile in self.lista_potere[:]:

            for pipistrello in self.lista_pipistrello[:]:
                if arcade.check_for_collision(proiettile, pipistrello):
                    pipistrello.vita -= proiettile.danno_proiettile

                    if pipistrello.vita <= 0:

                        self.spawn_cura(pipistrello.center_x, pipistrello.center_y)
                        self.spawn_ingrandimento(pipistrello.center_x, pipistrello.center_y)
                        
                        pipistrello.kill()
                        self.nemici_morti += 2
                        self.enemy_killati_per_exp += 2

                    proiettile.kill()


            for enemy in self.lista_nemico[:]:
                if arcade.check_for_collision(proiettile, enemy):
                    enemy.vita -= proiettile.danno_proiettile

                    if enemy.vita <= 0:

                        self.spawn_cura(enemy.center_x, enemy.center_y)
                        self.spawn_ingrandimento(enemy.center_x, enemy.center_y)

                        enemy.kill()
                        self.nemici_morti += 1
                        self.enemy_killati_per_exp += 1

                    proiettile.kill()
            
            for boss1 in self.lista_boss1[:]:
                if arcade.check_for_collision(proiettile, boss1):
                    boss1.vita -= proiettile.danno_proiettile
                    boss1.take_damage(10)

                    if boss1.vita <= 0:
                        boss1.kill()
                        self.nemici_morti += 10
                        self.enemy_killati_per_exp += 10   
                    proiettile.kill()

            for scheletro in self.lista_scheletro[:]:
                if arcade.check_for_collision(proiettile, scheletro):
                    scheletro.vita -= proiettile.danno_proiettile

                    if scheletro.vita <= 0:

                        self.spawn_cura(scheletro.center_x, scheletro.center_y)
                        self.spawn_ingrandimento(scheletro.center_x, scheletro.center_y)
                        
                        scheletro.kill()
                        self.nemici_morti += 3
                        self.enemy_killati_per_exp += 3

                    proiettile.kill()

        #esplosione bomba
        for c4 in self.lista_bomba:
            if tempo_attuale - c4.time_created >= 2:
                

                for pipistrello in self.lista_pipistrello[:]:
                    distanza = arcade.get_distance_between_sprites(c4, pipistrello)
                    if arcade.check_for_collision(c4, pipistrello):
                        pipistrello.vita -= self.danno_bomba

                        if pipistrello.vita <= 0:

                            self.spawn_cura(pipistrello.center_x, pipistrello.center_y)
                            self.spawn_ingrandimento(pipistrello.center_x, pipistrello.center_y)
                            
                            pipistrello.kill()
                            self.nemici_morti += 2
                            self.enemy_killati_per_exp += 2

                for enemy in self.lista_nemico[:]:
                    distanza = arcade.get_distance_between_sprites(c4, enemy)
                    if distanza <= self.esplosione:
                        enemy.vita -= self.danno_bomba

                        if enemy.vita <= 0:
                            
                            self.spawn_cura(enemy.center_x, enemy.center_y)
                            self.spawn_ingrandimento(enemy.center_x, enemy.center_y)
                            
                            enemy.kill()
                            self.nemici_morti += 1
                            self.enemy_killati_per_exp += 1

                for boss1 in self.lista_boss1[:]:
                    distanza = arcade.get_distance_between_sprites(c4, boss1)
                    if distanza <= self.esplosione:
                        boss1.vita -= self.danno_bomba

                        if boss1.vita <= 0:
                            boss1.kill()
                            self.nemici_morti += 10
                            self.enemy_killati_per_exp += 10

                for scheletro in self.lista_scheletro[:]:
                    distanza = arcade.get_distance_between_sprites(c4, scheletro)
                    if distanza <= self.esplosione:
                        scheletro.vita -= self.danno_bomba

                        if scheletro.vita <= 0:
                            
                            self.spawn_cura(scheletro.center_x, scheletro.center_y)
                            self.spawn_ingrandimento(scheletro.center_x, scheletro.center_y)
                            
                            scheletro.kill()
                            self.nemici_morti += 1
                            self.enemy_killati_per_exp += 1

                c4.remove_from_sprite_lists()
        
        #gestione della cura 
        cure_colpite = arcade.check_for_collision_with_list(self.personaggio, self.lista_cura)
        for cure in cure_colpite:
            self.vita_personaggio += cure.quant_cura

            if self.vita_personaggio >= self.barra_vita.max_health:
                self.vita_personaggio = self.barra_vita.max_health

            cure.kill()
        
        ingrandimenti_colpiti = arcade.check_for_collision_with_list(self.personaggio, self.lista_ingrandimento)
        for ingrandimenti in ingrandimenti_colpiti:
            for i in range(4):
                bullet_ = Bullet(self.personaggio, scala = 0.3)
                self.lista_potere.append(bullet_)
            ingrandimenti.kill()
                

        if self.vita_personaggio <= 0:
            from gameover import GameOver
            over = GameOver()
            self.window.show_view(over)

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
        elif tasto == arcade.key.ESCAPE:
            from pausa import PauseView
            pausa = PauseView(self)
            self.window.show_view(pausa)
        elif tasto == arcade.key.M:
            from menuLVL import MenuLvlView
            menuLVL = MenuLvlView(self)
            self.window.show_view(menuLVL)
        
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