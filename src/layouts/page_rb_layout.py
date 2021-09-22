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
                                DMIcombobox(50, 39, 280, 50, "rb1_A\n(280x50)"),
                                DMIcheckbutton(50, 104, 20, "Connecté à Renard ?", 12, "rb1_B (280x20)"),
                                DMIcheckbutton(335, 104, 20, "Connecté par une caméra ?", 12, "rb1_C (300x20)"),
                                DMItext(50, 145, "Interface pupitre", 12, "rb1_D"),
                                DMIcombobox(50, 169, 280, 60, "rb1_D\n(280x50)"),
                                DMItext(50, 236, "Niveau de registre", 12, "rb1_E"),
                                DMIbutton(50, 260, 111, 50, "rb1_E\n(111x50)"),
                                DMItext(225, 236, "Langue", 12, "rb1_F"),
                                DMIcombobox(225, 260, 111, 50, "rb1_F\n(111x50)"),
                                DMIcheckbutton(50, 369, 20, "Affichage en direct des données du train ?", 12, "rb1_H (320*20)"),
                                DMIcheckbutton(50, 329, 20, "Activation du PCC (Poste de Commande Centralisé) ?", 12, "rb1_G (280x20)")])
    page_rb1_layout_image.save()


def page_rb5():
    page_rb5_layout_image = image.ImageDrawer("page_rb5_layout.png")
    page_rb5_layout_image.draw([box.BoxDrawer(0, 0, 640, 480, ""),                      # contour de l'application
                                box.BoxDrawer(0, 0, 640, 15, "(640x15)", True),         # bande vide supérieure
                                box.BoxDrawer(0, 465, 640, 15, "(640x15)", True),       # bande vide inférieure
                                box.BoxDrawer(0, 415, 640, 50, "bb\n(640x50)", True),   # zone bb
                                box.BoxDrawer(580, 15, 60, 400, "rb\n(60x400)", True),  # zone rb
                                box.BoxDrawer(0, 15, 580, 400, "")])                    # zone page_rb
    page_rb5_layout_image.draw([DMIbutton(54, 15, 46, 40, "rb5_A\n(46x40)"),
                                DMIbutton(100, 15, 380, 40, "rb5_B\n(380x40)"),
                                DMIbutton(480, 15, 46, 40, "rb5_C\n(48x40)"),
                                DMIbutton(54, 55, 472, 76, "rb5_D.1\n(472x76)"),
                                DMIbutton(54, 131, 472, 76, "rb5_D.2\n(472x76)"),
                                DMIbutton(54, 207, 472, 76, "rb5_D.3\n(472x76)"),
                                DMIbutton(54, 283, 472, 76, "rb5_D.4\n(472x76)"),
                                DMIbutton(434, 359, 46, 40, "rb5_E\n(46x40)"),
                                DMIbutton(480, 359, 46, 40, "rb5_F\n(46x40)"),
                                DMIcheckbutton(15, 379, 20, "Eteindre les écrans qui ne sont pas utilisés ?)", 12, "rb5_G (400x20)")])
    page_rb5_layout_image.save()

def screen_parameters_item():
    screen_parameters_layout = image.ImageDrawer("screen_parameters.png", 472, 76)
    screen_parameters_layout.draw([DMIbutton(0, 0, 472, 76, ""),
                                   DMItext(14, 14, "AHHHHHHHHHHHHHHHHHHHHHHHHHHHH", 12, "SPI_A (300x14)"),
                                   DMIcheckbutton(346, 10, 20, "Plein écran ?    ", 12, "SPI_B (60x20)"),
                                   DMIcombobox(1, 45, 100, 30, "SPI_C\n(100x30)"),
                                   DMIvalueinput(134, 45, 60, 30, "SPI_D\n(60x30)"),
                                   DMIvalueinput(218, 45, 60, 30, "SPI_E\n(60x30)"),
                                   DMIvalueinput(325, 45, 60, 30, "SPI_F\n(60x30)"),
                                   DMIvalueinput(411, 45, 60, 30, "SPI_G\n(60x30)")])
    screen_parameters_layout.save()


