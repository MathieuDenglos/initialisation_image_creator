from src.default import box, image

from src.default.DMItext import *
from src.default.DMIcheckbutton import *
from src.default.DMIvalueinput import *
from src.default.DMIcombobox import *
from src.default.DMIbutton import *


def page_rb1():
    page_rb1_layout_image = image.ImageDrawer("page_rb1_layout.png")
    page_rb1_layout_image.draw([box.BoxDrawer(0, 0, 640, 480, ""),                      # contour de l'application
                                box.BoxDrawer(0, 0, 640, 15, "(640x15)", True),         # bande vide supérieure
                                box.BoxDrawer(0, 465, 640, 15, "(640x15)", True),       # bande vide inférieure
                                box.BoxDrawer(0, 415, 640, 50, "bb\n(640x50)", True),   # zone bb
                                box.BoxDrawer(580, 15, 60, 400, "rb\n(60x400)", True),  # zone rb
                                box.BoxDrawer(0, 15, 580, 400, "")])                    # zone page_rb
    page_rb1_layout_image.draw([DMItext(50, 15, "Pupitre", 12, "rb1_A"),
                                DMIcombobox(50, 39, 280, 50, "rb1_A"),
                                DMIcheckbutton(335, 104, 20, "Connecté par une caméra ?", 12, "rb1_B"),
                                DMIcheckbutton(50, 104, 20, "Connecté à Renard ?", 12, "rb1_C"),
                                DMItext(50, 145, "Interface pupitre", 12, "rb1_D"),
                                DMIcombobox(50, 169, 280, 60, "rb1_D"),
                                DMItext(225, 236, "Langue", 12, "rb1_F"),
                                DMIcombobox(225, 260, 111, 50, "rb1_F"),
                                DMItext(50, 236, "Niveau de registre", 12, "rb1_E"),
                                DMIbutton(50, 260, 111, 50, "rb1_E"),
                                DMIcheckbutton(50, 369, 20, "Affichage en direct des données du train ?", 12, "rb1_G"),
                                DMIcheckbutton(50, 329, 20, "Activation du PCC (Poste de Commande Centralisé) ?", 12, "rb1_H")])
    page_rb1_layout_image.save()


