import arcade


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view #riferimento della partita in corso
    
    def on_draw(self):
        self.game_view.on_draw()
    
        arcade.draw_rect_filled(
            arcade.XYWH(480, 270, 960, 540),
            (0, 0, 0, 150)  # nero semitrasparente
        )
    
        arcade.draw_text("PAUSA", 480, 350,
                         arcade.color.WHITE, font_size=48, anchor_x="center")
        arcade.draw_text("INVIO: Riprendi    ESC: Menu principale",
                         480, 250, arcade.color.LIGHT_GRAY, font_size=16, anchor_x="center")
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RETURN:
            self.window.show_view(self.game_view)
        elif key == arcade.key.ESCAPE:
            from menu import MenuView
            self.window.show_view(MenuView())