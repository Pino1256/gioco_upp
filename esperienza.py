import arcade

HEALTHBAR_WIDTH = 500
HEALTHBAR_HEIGHT = 20
TEXT_OFFSET_Y = 5  # distanza del testo sopra la barra

class Exp:
    def __init__(self, max_exp, x, y):
        self.max_exp = max_exp
        self.cur_exp = 0
        self.x = x
        self.y = y

    def draw_exp_number(self):
        arcade.draw_text(
            f"{self.cur_exp}/{self.max_exp}",
            self.x,
            self.y + TEXT_OFFSET_Y,
            arcade.color.RED,
            14
        )

    def draw_exp_bar(self):
        ratio = max(0, min(1, self.cur_exp / self.max_exp))

        # Rettangolo nero (sfondo)
        arcade.draw_lbwh_rectangle_filled(
            self.x, 
            self.y, 
            HEALTHBAR_WIDTH, 
            HEALTHBAR_HEIGHT, 
            arcade.color.BLACK
        )

        # Rettangolo blu (exp attuale)
        arcade.draw_lbwh_rectangle_filled(
            self.x, 
            self.y, 
            HEALTHBAR_WIDTH * ratio, 
            HEALTHBAR_HEIGHT, 
            arcade.color.BLUE
        )