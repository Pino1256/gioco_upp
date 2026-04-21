import arcade
from gameview import GameView

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MenuLvlView (arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view # partita in corso


    def on_draw(self):
        self.clear()

        arcade.draw_text("Menu LVL", SCREEN_WIDTH // 2, 500,
                         arcade.color.WHITE, font_size=40, anchor_x="center")
        
        arcade.draw_text("Premi Z: + Livello Proiettile", SCREEN_WIDTH // 2, 400,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        
        arcade.draw_text("Premi X: + Livello Bomba", SCREEN_WIDTH // 2, 350,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        
        arcade.draw_text("Premi C: + Livello Corsa", SCREEN_WIDTH // 2, 300,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        
        arcade.draw_text("Premi V: + Livello spada", SCREEN_WIDTH // 2, 200,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Z:

            self.game_view.logic_proiettile = True
            self.window.show_view(self.game_view)

        if key == arcade.key.X:

            self.game_view.logic_bomba = True
            self.window.show_view(self.game_view)
            
        if key == arcade.key.C:

            self.game_view.logic_corsa = True
            self.window.show_view(self.game_view)
        
        if key == arcade.key.V:

            self.game_view.aumento_spada = True
            self.window.show_view(self.game_view)