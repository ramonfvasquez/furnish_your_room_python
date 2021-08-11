import os

from PIL import Image, ImageTk

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
FURNITURE = STATIC_ROOT + "furniture/"


class Armchair:
    image = FURNITURE + "armchair.png"


class Chair:
    image = FURNITURE + "chair.png"


class Couch:
    image = FURNITURE + "couch.png"


class Desk:
    image = FURNITURE + "desk.png"


class DoubleBed:
    image = FURNITURE + "double-bed.png"


class PCChair:
    image = FURNITURE + "pc-chair.png"


class PCDesk:
    image = FURNITURE + "pc-desk.png"


class Table:
    image = FURNITURE + "table.png"


def get_pieces():
    return [
        "Armchair",
        "Chair",
        "Couch",
        "Desk",
        "Double Bed",
        "PC Chair",
        "PC Desk",
        "Table",
    ]


def show_piece(label, piece):
    file_name = "%s%s.png" % (FURNITURE, piece.replace(" ", "-").lower())
    im = Image.open(file_name).resize((16, 16))
    img = ImageTk.PhotoImage(im)
    label["image"] = img
    label.image = img
