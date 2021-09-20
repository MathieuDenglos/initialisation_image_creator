from src.default import box

from PIL import Image, ImageDraw, ImageFont


class DMIcheckbutton:

    box_box = None
    text_box = None

    def __init__(self, x, y, box_lenght, checkbutton_text, text_size, text, fill=False):
        """Permet d'initialiser la boite à dessiner

        Parameters
        ----------
        x : `int`
            coordonnée x initiale
        y : `int`
            hauteur de la boite
        box_lenght: `int`
            longueur de la boite
        checkbutton_text: `string`
            texte à côté du checkbutton
        text_size: `int`
            la taille en pixel du texte du checkbutton
        text : `string`
            texte à afficher au milieu de la boite
        fill : `bool`
            la boite doit-elle être remplie en bleu clair
        """
        # Initialise la boite pour la boite du checkbutton
        self.box_box = box.BoxDrawer(x, y, box_lenght, box_lenght, "", fill)

        # Initialise la boite pour le texte du checkbutton
        drawing = ImageDraw.Draw(Image.new("RGB", (640, 480), (3, 17, 34)))
        text_w, text_h = drawing.textsize(checkbutton_text, font=ImageFont.truetype("arial.ttf", text_size))
        text_x = x + box_lenght + text_size
        text_y = y + (box_lenght - text_h)/2
        self.text_box = box.BoxDrawer(text_x, text_y - 1, text_w, text_h + 4, text, fill)

    def draw(self, drawing):
        """Permet de dessiner la boite

        drawing : `ImageDrawing`
            Le dessin sur lequel il faut ajouter la forme
        """
        self.text_box.draw(drawing)
        self.box_box.draw(drawing)