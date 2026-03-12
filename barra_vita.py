import arcade

HEALTHBAR_WIDTH = 170
HEALTHBAR_HEIGHT = 20
TEXT_OFFSET_Y = 5  # distanza del testo sopra la barra

class BarraVita:
    def __init__(self, max_health, x, y, HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT):
        self.max_health = max_health
        self.cur_health = max_health
        self.HEALTHBAR_WIDTH = HEALTHBAR_WIDTH
        self.HEALTHBAR_HEIGHT = HEALTHBAR_HEIGHT
        self.x = x
        self.y = y

    def draw_health_number(self):
        arcade.draw_text(
            f"{self.cur_health}/{self.max_health}",
            self.x,
            self.y + TEXT_OFFSET_Y,
            arcade.color.BLACK,
            14
        )

    def draw_health_bar(self):
        ratio = max(0, min(1, self.cur_health / self.max_health))

        # Rettangolo rosso (sfondo)
        arcade.draw_lbwh_rectangle_filled(
            self.x, 
            self.y, 
            self.HEALTHBAR_WIDTH, 
            self.HEALTHBAR_HEIGHT, 
            arcade.color.RED
        )

        # Rettangolo verde (vita attuale)
        arcade.draw_lbwh_rectangle_filled(
            self.x, 
            self.y, 
            self.HEALTHBAR_WIDTH * ratio, 
            self.HEALTHBAR_HEIGHT, 
            arcade.color.TEA_GREEN
        )
