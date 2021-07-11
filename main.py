# pip install Pillow
from PIL import Image, ImageDraw, ImageFont


def general_layout():
    # Création de l'image
    image = Image.new("RGB", (640, 480), (3, 17, 34))
    drawing = ImageDraw.Draw(image)

    # Bande supérieure et inférieure
    drawing.rectangle([0, 0, 639, 14], width=1, outline=(255, 255, 255))
    drawing.rectangle([0, 465, 639, 479], width=1, outline=(255, 255, 255))
    w, h = drawing.textsize("(640x15)")
    drawing.text((0 + (640 - w) / 2, 0 + (15 - h) / 2), "(640x15)",
                 align="center", font=ImageFont.truetype("arial.ttf", 12))
    drawing.text((0 + (640 - w) / 2, 465 + (15 - h) / 2), "(640x15)",
                 align="center", font=ImageFont.truetype("arial.ttf", 12))

    # Zone bbX
    drawing.rectangle([0, 415, 639, 464], width=1, outline=(255, 255, 255))
    w, h = drawing.textsize("bb\n(640x50)")
    drawing.multiline_text((0 + (640 - w) / 2, 415 + (50 - h) / 2), "bb\n(640x50)",
                           align="center", font=ImageFont.truetype("arial.ttf", 12))

    # Zone rbX
    drawing.rectangle([580, 15, 639, 414], width=1, outline=(255, 255, 255))
    w, h = drawing.textsize("rb\n(60x400)")
    drawing.multiline_text((580 + (60 - w) / 2, 15 + (400 - h) / 2), "rb\n(60x400)",
                           align="center", font=ImageFont.truetype("arial.ttf", 12))

    # Zone page_rbX
    drawing.rectangle([0, 15, 579, 414], width=1, outline=(255, 255, 255))
    w, h = drawing.textsize("page_rb\n(580x400)")
    drawing.multiline_text((0 + (580 - w) / 2, 15 + (400 - h) / 2), "page_rb\n(580x400)",
                           align="center", font=ImageFont.truetype("arial.ttf", 12))

    # Sauvegarde l'image
    image.save('general_layout.png')


def detailed_layout():
    # Création de l'image
    image = Image.new("RGB", (640, 480), (3, 17, 34))
    drawing = ImageDraw.Draw(image)

    # Bande supérieure et inférieure
    drawing.rectangle([0, 0, 639, 14], width=1, outline=(255, 255, 255))
    drawing.rectangle([0, 465, 639, 479], width=1, outline=(255, 255, 255))
    w, h = drawing.textsize("(640x15)")
    drawing.text((0 + (640 - w) / 2, 0 + (15 - h) / 2), "(640x15)",
                 align="center", font=ImageFont.truetype("arial.ttf", 12))
    drawing.text((0 + (640 - w) / 2, 465 + (15 - h) / 2), "(640x15)",
                 align="center", font=ImageFont.truetype("arial.ttf", 12))

    # Zone bb
    w, h = drawing.textsize("bbX\n(580x50)")
    for index in range(1, 5):
        x0 = 120 * (index - 1) + 160 * (index > 1)
        x1 = 120 * index - 1 + 160 * (index > 1)
        drawing.rectangle([x0, 415, x1, 464], width=1, outline=(255, 255, 255))
        drawing.multiline_text((x0 + (120 - w) / 2, 415 + (50 - h) / 2), "bb" + str(index) + "\n(120x50)",
                               align="center", font=ImageFont.truetype("arial.ttf", 12))

    # Zone rbX
    w, h = drawing.textsize("rbX\n(60x50)")
    for index in range(1, 9):
        y0 = 15 + 50 * (index - 1)
        y1 = 15 + 50 * index - 1
        drawing.rectangle([580, y0, 639, y1], width=1, outline=(255, 255, 255))
        drawing.multiline_text((580 + (60 - w) / 2, y0 + (50 - h) / 2), "rb" + str(index) + "\n(60x50)",
                               align="center", font=ImageFont.truetype("arial.ttf", 12))

    # Zone page_rbX
    drawing.rectangle([0, 15, 579, 414], width=1, outline=(255, 255, 255))
    w, h = drawing.textsize("\n(580x400)")
    drawing.multiline_text((0 + (580 - w) / 2, 15 + (400 - h) / 2), "page_rb\n(580x400)",
                           align="center", font=ImageFont.truetype("arial.ttf", 12))

    # Sauvegarde l'image
    image.save('detailed_layout.png')


def main():
    general_layout()
    # detailed_layout()


if __name__ == "__main__":
    main()