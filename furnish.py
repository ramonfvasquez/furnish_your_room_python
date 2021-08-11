import tkinter as tk
from PIL import Image, ImageTk

import furniture


class Furnish:
    furniture = []

    def insert(self, canvas, combobox, coords):
        piece = str_to_class(combobox.get().replace(" ", ""))

        x, y = coords

        im = Image.open(piece.image).resize((64, 64))
        self.img = ImageTk.PhotoImage(im)
        obj = canvas.create_image(x, y, anchor=tk.CENTER, image=self.img)
        canvas.image = self.img

        self.furniture.append({obj: canvas.image})


def str_to_class(class_name):
    return getattr(furniture, class_name)
