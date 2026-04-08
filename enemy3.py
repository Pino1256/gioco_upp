import arcade
from nemico_globale import Enemy_general
from gameview import GameView
from sprite_animato import SpriteAnimato

class Enemy3(Enemy_general, SpriteAnimato):
    def __init__(self):
        Enemy_general.__init__(self, "./assetss/scheletro.png", scale = 1, velocita_nemico = 3.20, vita= 30)
        SpriteAnimato.__init__(self, scale = 1)

        file_animazioni = [
            {"nome": "destra",   "file": "assetss/scheletro.png", "flip": False},
            {"nome": "sinistra", "file": "assetss/scheletro.png", "flip": True},
        ]
    
        for anim in file_animazioni: 
            self.aggiungi_animazione(
                nome = f"run_{anim['nome']}",
                percorso = anim['file'],
                frame_width = 96,
                frame_height = 64,
                num_frame = 10,
                colonne = 10,
                durata = 1,
                riga = 0,
                specchia = anim['flip']
            )
        
        self.direzione = "destra"
        self.change_x = 0
        self.change_y = 0        
    
    def update_animation(self, delta_time):

        if self.change_x > 0:
            self.direzione = "destra"
        elif self.change_x < 0:
            self.direzione = "sinistra"

        self.imposta_animazione(f"run_{self.direzione}")

        super().update_animation(delta_time)   