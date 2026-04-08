import arcade
from nemico_globale import Enemy_general
from gameview import GameView
from sprite_animato import SpriteAnimato

class Enemy_2(Enemy_general, SpriteAnimato):
    def __init__(self):
        Enemy_general.__init__(self, "./assetss/pipistrello.png", scale = 2, velocita_nemico = 3, vita= 20)
        SpriteAnimato.__init__(self, scale = 2)

        file_animazioni = [
            {"nome": "destra",   "file": "assetss/run_but.png", "flip": True},
            {"nome": "sinistra", "file": "assetss/run_but.png", "flip": False},
        ]
    
        for anim in file_animazioni: 
            self.aggiungi_animazione(
                nome = f"run_{anim['nome']}",
                percorso = anim['file'],
                frame_width = 64,
                frame_height = 64,
                num_frame = 8,
                colonne = 8,
                durata = 1,
                riga = 0,
                specchia = anim['flip']
            )
        
        self.direzione = "destra"      
    
    def update_animation(self, delta_time):

        if self.change_x > 0:
            self.direzione = "destra"
        elif self.change_x < 0:
            self.direzione = "sinistra"

        self.imposta_animazione(f"run_{self.direzione}")

        super().update_animation(delta_time) 
