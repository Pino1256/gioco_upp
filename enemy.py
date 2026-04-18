import arcade
from nemico_globale import Enemy_general
from sprite_animato import SpriteAnimato

class Enemy(Enemy_general, SpriteAnimato):
    def __init__(self,):

        Enemy_general.__init__(self, "./assetss/nemicocompresso.png", scale = 2, velocita_nemico = 2, vita = 10)
        SpriteAnimato.__init__(self, scale = 1.5)

        self.cooldown = 1.0
        self.time_since_last_hit = 0.0
        self.time_since_last_hit_player = 0.0

        file_animazioni = [
            {"nome": "destra",   "file": "assetss/run_slime.png", "flip": False},
            {"nome": "sinistra", "file": "assetss/run_slime.png", "flip": True},
        ]
    
        for anim in file_animazioni: #dir = direzione
            self.aggiungi_animazione(
                nome = f"run_{anim['nome']}",
                percorso = anim['file'],
                frame_width = 48,
                frame_height = 48,
                num_frame = 12,
                colonne = 12,
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

    def update(self, delta_time):
        self.time_since_last_hit += delta_time
        self.time_since_last_hit_player += delta_time
        
        super().update()
    
    def can_take_damage(self):
        return self.time_since_last_hit >= self.cooldown
    
    def take_damage(self, amount):
        # if self.can_take_damage():
        #     self.vita -= amount 
        #     self.time_since_last_hit = 0.0

        if self.time_since_last_hit >= self.cooldown:
            self.vita -= amount 
            self.time_since_last_hit = 0.0