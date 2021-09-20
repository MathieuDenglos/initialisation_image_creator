# pip install Pillow
from src.default import box, image


def general_layout():
    general_layout_image = image.ImageDrawer("general_layout.png")
    general_layout_image.draw([box.BoxDrawer(0, 0, 640, 480, ""),                       # contour de l'application
                               box.BoxDrawer(0, 0, 640, 15, "(640x15)"),                # bande vide supérieure
                               box.BoxDrawer(0, 465, 640, 15, "(640x15)"),              # bande vide inférieure
                               box.BoxDrawer(0, 415, 640, 50, "bb\n(640x50)"),          # zone bb
                               box.BoxDrawer(580, 15, 60, 400, "rb\n(60x400)"),         # zone rb
                               box.BoxDrawer(0, 15, 580, 400, "page_rb\n(580x400)")])   # zone page_rb
    general_layout_image.save()


def detailed_layout():
    detailed_layout_image = image.ImageDrawer("detailed_layout.png")
    detailed_layout_image.draw([box.BoxDrawer(0, 0, 640, 480, ""),                      # contour de l'application
                                box.BoxDrawer(0, 0, 640, 15, "(640x15)"),               # bande vide supérieure
                                box.BoxDrawer(0, 465, 640, 15, "(640x15)"),             # bande vide inférieure
                                box.BoxDrawer(0, 415, 640, 50, "")] +                   # zone bb
                                [box.BoxDrawer(120*(i-1) + (160 if i > 1 else 0), 415, 120, 50, "bb" + str(i) + "\n(120x50)")
                                 for i in [1, 2, 3, 4]] +                                  # boutons zone bb
                                [box.BoxDrawer(580, 15, 60, 400, "")] +                 # zone rb
                                [box.BoxDrawer(580, 15+50*(i-1), 60, 50, "rb" + str(i) + "\n(60x50)")
                                 for i in range(1, 9)] +
                                [box.BoxDrawer(0, 15, 580, 400, "page_rb\n(580x400)")]) # zone page_rb
    detailed_layout_image.save()
