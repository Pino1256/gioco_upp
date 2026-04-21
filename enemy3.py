import arcade
from nemico_globale import Enemy_general
from gameview import GameView
from sprite_animato import SpriteAnimato
import random

class Enemy3(Enemy_general, SpriteAnimato):
    def __init__(self, edge=None):

        if edge is None:
            edge = random.randint(0, 3)

        Enemy_general.__init__(self, "./assetss/scheletro.png", scale = 1, velocita_nemico = 3.20, vita= 30, edge = edge)
        SpriteAnimato.__init__(self, scale = 1)

        self.cooldown = 0.2
        self.time_since_last_hit = 0.0
        self.time_since_last_hit_player = 0.0

        file_animazioni = {
            "destra": "assetss/run_scheletro.png",
            "sinistra" : "assetss/run_scheletr2.png"
        }
    
        for dir, percorso in file_animazioni.items(): 
            self.aggiungi_animazione(
                nome = f"run_{dir}",
                percorso = percorso,
                frame_width = 96,
                frame_height = 64,
                num_frame = 10,
                colonne = 10,
                durata = 1,
                riga = 0,
            )
        
        self.direzione = "destra"

        self.ultima_animazione = ""

    
    def update_animation(self, delta_time):

        if self.change_x > 0:
            self.direzione = "destra"
        elif self.change_x < 0:
            self.direzione = "sinistra"

        if self.change_x != 0 or self.change_y != 0:
            self.imposta_animazione(f"run_{self.direzione}")
            nuova_anim = f"run_{self.direzione}"
            if self.ultima_animazione != nuova_anim:
                self.imposta_animazione(nuova_anim)
                self.ultima_animazione = nuova_anim

        super().update_animation(delta_time)   

    def can_take_damage(self):
        return self.time_since_last_hit >= self.cooldown
    
    def take_damage(self, amount):
        if self.can_take_damage():
            self.vita -= amount 
            self.time_since_last_hit = 0.0