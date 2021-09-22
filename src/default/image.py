# pip install Pillow
from PIL import Image, ImageDraw


class ImageDrawer:

    image_name = "image/"
    image = None
    drawing = None

    def __init__(self, image_name, width=640, height=480):
        """ Permet d'initialiser une nouvelle image

        Parameters
        ----------
        image_name: `str`
            Le nom de l'image avec son extension (généralement .png). Celle ci sera enregistrée dans le répertoire image
        width: `int`
            Longueur de l'image créée
        height: `int`
            Hauteur de l'image créée
        """
        # Enregistre le nom de l'image pour la sauvegarder plus tard
        self.image_name += image_name if len(image_name.split(".")) >= 2 else image_name + ".png"

        # Initialise l'image
        self.image = Image.new("RGB", (width, height), (3, 17, 34))
        self.drawing = ImageDraw.Draw(self.image)

    def draw(self, shapes):
        """Dessine la liste de formes envoyées

        Parameters
        ----------
        shapes: `list
            liste des formes à dessiner
        """
        # Pour chaque forme dans l liste de forme, la dessine
        for shape in shapes:
            shape.draw(self.drawing)

    def save(self):
        """Fonction permettant de dessiner l'image
        """
        # sauvegarde l'image
        self.image.save(self.image_name)