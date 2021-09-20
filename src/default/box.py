# pip install Pillow
from PIL import ImageFont


class BoxDrawer:

    xy = []
    text = ""
    fill = False

    def __init__(self, x, y, width, height, text, fill=False):
        """Permet d'initialiser la boite à dessiner

        Parameters
        ----------
        x : `int`
            coordonnée x initiale
        y : `int`
            hauteur de la boite
        width : `int`
            coordonnée y initiale
        height : `ìnt`
            largeur de la boite
        text : `string`
            texte à afficher au milieu de la boite
        fill : `bool`
            la boite doit-elle être remplie en bleu clair
        """
        self.xy = [x, y, x + width - 1, y + height - 1]
        self.text = text
        self.fill = not not fill

    def draw(self, drawing):
        """Permet de dessiner la boite

        drawing : `ImageDrawing`
            Le dessin sur lequel il faut ajouter la forme
        """
        # Dessine le rectangle
        drawing.rectangle([self.xy[0], self.xy[1], self.xy[2], self.xy[3]],
                          width=1,
                          outline=(255, 255, 255),
                          fill=(97, 193, 193) if self.fill else (3, 17, 34))

        # Dessine le texte
        w, h = drawing.textsize(self.text)
        drawing.multiline_text((self.xy[0] + (self.xy[2]-self.xy[0]-w)/2, self.xy[1] + (self.xy[3]-self.xy[1]-h)/2),
                               self.text,
                               align="center",
                               font=ImageFont.truetype("arial.ttf", 12))
