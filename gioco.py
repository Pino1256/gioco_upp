import arcade

class giocone(arcade.Window):
    def __init__(self, larghezza, altezza, titolo):
        super().__init__(larghezza, altezza, titolo)

        self.personaggio = None
        self.lista_personaggio = arcade.SpriteList()

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.M_pressed = False

        self.velocita = 4

        self.setup()

    def setup(self):

        self.personaggio = arcade.Sprite("./assetss/idle_000.png")
        self.personaggio.center_x = 300
        self.personaggio.center_y = 100
        self.personaggio.scale = 0.2
        self.lista_personaggio.append(self.personaggio)
    
    def on_draw(self):
        self.clear()
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
            self.personaggio.scale = (0.2, 0.2)
        elif change_x > 0:
            self.personaggio.scale = (-0.2, 0.2)

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

    gioco = giocone(600, 600, "non è babbo")
    arcade.run()

if __name__ == "__main__":
    main()