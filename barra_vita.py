import arcade

HEALTHBAR_WIDTH = 100
HEALTHBAR_HEIGHT = 15
TEXT_OFFSET_Y = 20  # distanza del testo sopra la barra

class BarraVita:
    def __init__(self, max_health, x, y):
        self.max_health = max_health
        self.cur_health = max_health
        self.x = x
        self.y = y

    def draw_health_number(self):
        arcade.draw_text(
            f"{self.cur_health}/{self.max_health}",
            self.x,
            self.y + TEXT_OFFSET_Y,
            arcade.color.WHITE,
            14
        )

    def draw_health_bar(self):
        ratio = max(0, min(1, self.cur_health / self.max_health))

        # Rettangolo rosso (sfondo)
        arcade.draw_lbwh_rectangle_filled(
            self.x, 
            self.y, 
            HEALTHBAR_WIDTH, 
            HEALTHBAR_HEIGHT, 
            arcade.color.RED
        )

        # Rettangolo verde (vita attuale)
        arcade.draw_lbwh_rectangle_filled(
            self.x, 
            self.y, 
            HEALTHBAR_WIDTH * ratio, 
            HEALTHBAR_HEIGHT, 
            arcade.color.GREEN
        )
