import arcade

class MenuLvlView (arcade.View):
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
        if key == arcade.key.Z:

            # aggiungere +1 lvl del proiettile
            self.window.lvl_proiettile +=1
            from gameview import GameView
            # passo alla schermata di gioco
            game_view = GameView()
            self.window.show_view(game_view)

        if key == arcade.key.X:

            # aggiungere +1 lvl della bomba
            self.window.lvl_bomba += 1
            from gameview import GameView
            game_view = GameView()
            self.window.show_view(game_view)
            
        if key == arcade.key.C:

            # aggiungere +1 lvl della corsa
            self.window.lvl_corsa += 1
            from gameview import GameView
            game_view = GameView()
            self.window.show_view(game_view)

