import arcade
from menu import MenuView

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "non è babbo")

        self.lvl_proiettile = 1
        self.lvl_bomba = 1
        self.lvl_corsa = 1
        
        menu = MenuView()
        self.show_view(menu)

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()