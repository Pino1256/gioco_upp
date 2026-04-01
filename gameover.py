import arcade


class GameOver (arcade.View):
    def on_draw(self):
        self.clear()
        arcade.draw_text("GAME OVER", 480, 350,
                         arcade.color.WHITE, font_size=48, anchor_x="center")

        arcade.draw_text("Premi INVIO per restartare", 480, 250,
                         arcade.color.LIGHT_GRAY, font_size=20, anchor_x="center")
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RETURN:
            from gameview import GameView
            # passo alla schermata di gioco
            game_view = GameView()
            self.window.show_view(game_view)