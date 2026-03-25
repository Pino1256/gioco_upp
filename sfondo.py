import arcade
import arcade.future.background as background

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800

class Parallax:
    def __init__(self):

        bg_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.backgrounds = background.ParallaxGroup() #gruppo che gesisce i layer

        #layer
        self.backgrounds.add_from_file("./assets/cielo.png", size = bg_size, depth = 10.0)
        self.backgrounds.add_from_file("./assets/montagne.png", size = bg_size, depth = 10.0)
        self.backgrounds.add_from_file("./assets/alberi.png", size = bg_size, depth = 10.0)
    
    def draw(self):
        self.backgrounds.draw()
