from src.default import box, image


def main():
    complete_layout = image.ImageDrawer("e")
    complete_layout.draw([box.BoxDrawer(20, 20, 120, 40, "Oui", False)])
    complete_layout.save()


if __name__ == "__main__":
    main()
