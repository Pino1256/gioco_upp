import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MenuView (arcade.View):
    def __init__(self):
        super().__init__()

        self.sfondo_menu = None
        self.lista_sfondo = arcade.SpriteList()

        self.sfondo()

    def sfondo(self):
        self.sfondo_menu = arcade.Sprite("assetss/menu_upp.png")
        self.sfondo_menu.center_x = SCREEN_WIDTH // 2
        self.sfondo_menu.center_y = SCREEN_HEIGHT // 2
        self.sfondo_menu.scale = 0.8
        self.lista_sfondo.append(self.sfondo_menu)


    def on_draw(self):
        self.clear()
        self.lista_sfondo.draw()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RETURN:
            from gameview import GameView
            # passo alla schermata di gioco
            game_view = GameView()
            self.window.show_view(game_view)
