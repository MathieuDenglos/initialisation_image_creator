from src.default import box

from PIL import Image, ImageDraw, ImageFont


class DMItext(box.BoxDrawer):

    box_box = None
    text_box = None

    def __init__(self, x, y, text_text, text_size, text, fill=False):
        """Permet d'initialiser la boite à dessiner

        Parameters
        ----------
        x : `int`
            coordonnée x initiale
        y : `int`
            hauteur de la boite
        text_text: `string`
            le texte affiché sur le texte
        text_size: `int`
            la taille en pixel du texte du checkbutton
        text : `string`
            texte à afficher au milieu de la boite
        fill : `bool`
            la boite doit-elle être remplie en bleu clair
        """
        drawing = ImageDraw.Draw(Image.new("RGB", (640, 480), (3, 17, 34)))
        text_w, text_h = drawing.textsize(text_text, font=ImageFont.truetype("arial.ttf", text_size))
        super().__init__(x, y, text_w, text_h + 2, text, fill)
