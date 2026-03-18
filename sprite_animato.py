import arcade

class SpriteAnimato(arcade.Sprite):
    def __init__(self, scala: float = 1.0):
        super().__init__(scale=scala)
        self.animazioni = {}          # nome -> dizionario con textures, durata_frame, loop
        self.animazione_corrente = None
        self.animazione_default = None
        self.tempo_frame = 0.0
        self.indice_frame = 0

    def aggiungi_animazione(
        self,
        nome: str,
        percorso: str,
        frame_width: int,
        frame_height: int,
        num_frame: int,
        colonne: int,
        durata: float,
        loop: bool = True,
        default: bool = False,
        riga: int = 0,
    ):
        """
        Carica uno spritesheet e registra l'animazione con il nome dato.

        loop    : se True l'animazione riparte dall'inizio quando finisce
        default : se True questa è l'animazione di riposo (quella a cui si
                  torna automaticamente quando una animazione non in loop finisce)
        riga    : riga dello spritesheet da cui estrarre i frame (0 = prima riga)
        """
        sheet = arcade.load_spritesheet(percorso)
        offset = riga * colonne
        tutti = sheet.get_texture_grid(
            size=(frame_width, frame_height),
            columns=colonne,
            count=offset + num_frame,
        )
        self._registra(nome, tutti[offset:], durata, loop, default)

    def _registra(self, nome, textures, durata, loop, default=False):
        """Usato internamente per registrare texture già caricate."""
        self.animazioni[nome] = {
            "textures": textures,
            "durata_frame": durata / len(textures),
            "loop": loop,
        }
        if default or self.animazione_default is None:
            self.animazione_default = nome
        if self.animazione_corrente is None:
            self._vai(nome)

    def imposta_animazione(self, nome: str):
        """Cambia animazione (ignorata se è già quella attiva, evita reset del frame)."""
        if nome != self.animazione_corrente:
            self._vai(nome)

    def _vai(self, nome: str):
        self.animazione_corrente = nome
        self.indice_frame = 0
        self.tempo_frame = 0.0
        self.texture = self.animazioni[nome]["textures"][0]

    def update_animation(self, delta_time: float = 1 / 60):
        anim = self.animazioni[self.animazione_corrente]
        self.tempo_frame += delta_time

        if self.tempo_frame < anim["durata_frame"]:
            return  # non è ancora il momento di cambiare frame

        self.tempo_frame -= anim["durata_frame"]
        prossimo = self.indice_frame + 1

        if prossimo < len(anim["textures"]):
            # Frame successivo nello stesso ciclo
            self.indice_frame = prossimo
        elif anim["loop"]:
            # Fine ciclo: ricominciamo da capo
            self.indice_frame = 0
        else:
            # Animazione finita e non looppa: torna alla default
            self._vai(self.animazione_default)
            return

        self.texture = anim["textures"][self.indice_frame]