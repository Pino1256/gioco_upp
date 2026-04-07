import arcade
from nemico_globale import Enemy_general
from barra_vita import BarraVita
from sprite_animato import SpriteAnimato

class Boss1(Enemy_general, SpriteAnimato):
    def __init__(self):

        Enemy_general.__init__(self, "./assetss/run_golem.png", scale = 0.2, velocita_nemico = 2, vita = 50)
        SpriteAnimato.__init__(self, scale = 1)

        file_animazioni = [
            {"nome": "destra",   "file": "assetss/run_golem.png", "flip": False},
            {"nome": "sinistra", "file": "assetss/run_golem.png", "flip": True},
        ]

        for anim in file_animazioni: 
            self.aggiungi_animazione(
                nome = f"run_{anim['nome']}",
                percorso = anim['file'],
                frame_width = 90,
                frame_height = 64,
                num_frame = 10,
                colonne = 10,
                durata = 1,
                riga = 0,
                specchia = anim['flip']
            )
        
        self.direzione = "destra"  

        self.max_vita = self.vita

        # Barra sopra la testa (posizione iniziale)
        self.barra_vita_boss = BarraVita(
            max_health=self.max_vita,
            x=self.center_x,
            y=self.center_y,
            HEALTHBAR_WIDTH = 100,
            HEALTHBAR_HEIGHT = 10
        )
    

    def update_bar(self):
        # La barra segue il boss
        self.barra_vita_boss.x = self.center_x - 50
        self.barra_vita_boss.y = self.center_y + 80
        self.barra_vita_boss.cur_health = self.vita

    def take_damage(self, amount):
        self.vita -= amount
        self.barra_vita_boss.cur_health = self.vita

    def update_animation(self, delta_time):

        if self.change_x > 0:
            self.direzione = "destra"
        elif self.change_x < 0:
            self.direzione = "sinistra"

        self.imposta_animazione(f"run_{self.direzione}")

        super().update_animation(delta_time)   
