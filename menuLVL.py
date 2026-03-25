import arcade
from gameview import GameView

class MenuLvlView (arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view #riferimento della partita in corso


    def on_draw(self):
        self.clear()

        arcade.draw_text("Menu LVL", 480, -1500,
                         arcade.color.WHITE, font_size=48, anchor_x="center")
        
        arcade.draw_text("premi il tasto Z per far aumentare il livello del proiettile", 480, 1000,
                         arcade.color.WHITE, font_size=48, anchor_x="center")
        
        arcade.draw_text("sasasas", 480, -600,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        
        arcade.draw_text("ffdsg", 480, -9400,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        

    def on_key_press(self, key, modifiers):
        from gameview import GameView
        if key == arcade.key.Z:
            if self.window.proiettile_lvl <= 7:
                # aggiungere +1 lvl del proiettile
                self.window.lvl_proiettile +=1
                self.window.proiettile_lvl += 1
            self.window.show_view(self.game_view)

        if key == arcade.key.X:

            # aggiungere +1 lvl della bomba
            self.window.lvl_bomba += 1
            self.window.show_view(self.game_view)
            
        if key == arcade.key.C:

            # aggiungere +1 lvl della corsa
            self.window.lvl_corsa += 1
            self.window.show_view(self.game_view)
            