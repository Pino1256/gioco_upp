import arcade
from gioco import gioconeVew

class MenuView (arcade.View):
    def on_draw(self):
        self.clear()
        arcade.draw_text("IL GIOCO  DEI GIOCHI", 480, 350,
                         arcade.color.WHITE, font_size=48, anchor_x="center")

        arcade.draw_text("Premi INVIO per iniziare", 480, 250,
                         arcade.color.LIGHT_GRAY, font_size=20, anchor_x="center")
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RETURN:
            # passo alla schermata di gioco
            game_view = gioconeVew()
            game_view.setup()
            self.window.show_view(game_view)
