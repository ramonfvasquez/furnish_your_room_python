import tkinter as tk
from tkinter import ttk

import furnish
import furniture
import room


class FurnishYourRoom:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Furnish Your Room")
        self.root.resizable(False, False)

        self.container = tk.Frame(self.root)
        self.container.pack(fill=tk.BOTH)

        self.frm_room = tk.Frame(self.container)
        self.frm_room.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)

        self.cnv_room = tk.Canvas(self.frm_room, width=400, height=400, bg="brown")
        self.cnv_room.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.frm_right_side = tk.Frame(self.container)
        self.frm_right_side.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)

        self.frm_room_size = tk.LabelFrame(self.frm_right_side, text="Room Size")
        self.frm_room_size.grid(
            row=0, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW
        )

        self.size = tk.StringVar()
        self.size_300x300 = tk.Radiobutton(
            self.frm_room_size,
            text="300x300",
            variable=self.size,
            value="300x300",
            command=lambda: [
                room.set_room_size(self.size, self.cnv_room),
                self.enable_entry(),
            ],
        )
        self.size_300x300.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.size_400x400 = tk.Radiobutton(
            self.frm_room_size,
            text="400x400",
            variable=self.size,
            value="400x400",
            command=lambda: [
                room.set_room_size(self.size, self.cnv_room),
                self.enable_entry(),
            ],
        )
        self.size_400x400.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.size_500x500 = tk.Radiobutton(
            self.frm_room_size,
            text="500x500",
            variable=self.size,
            value="500x500",
            command=lambda: [
                room.set_room_size(self.size, self.cnv_room),
                self.enable_entry(),
            ],
        )
        self.size_500x500.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.size_600x600 = tk.Radiobutton(
            self.frm_room_size,
            text="600x600",
            variable=self.size,
            value="600x600",
            command=lambda: [
                room.set_room_size(self.size, self.cnv_room),
                self.enable_entry(),
            ],
        )
        self.size_600x600.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.size_other = tk.Radiobutton(
            self.frm_room_size,
            text="Other",
            variable=self.size,
            value="other",
            command=self.enable_entry,
        )
        self.size_other.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.other = tk.StringVar()
        self.ent_other = tk.Entry(
            self.frm_room_size, textvariable=self.other, state="disabled", width=8
        )
        self.ent_other.grid(row=2, column=1, padx=5, pady=5)

        self.btn_set_size = tk.Button(
            self.frm_room_size,
            text="Set",
            command=lambda: room.set_room_size(self.other, self.cnv_room),
        )
        self.btn_set_size.grid(row=2, column=2, padx=5, pady=5, sticky=tk.NSEW)

        self.frm_furniture = tk.LabelFrame(self.frm_right_side, text="Furniture")
        self.frm_furniture.grid(
            row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW
        )

        self.cmb_furniture = ttk.Combobox(
            self.frm_furniture, values=furniture.get_pieces(), width=15
        )
        self.cmb_furniture.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)

        self.lbl_furniture = tk.Label(self.frm_furniture, anchor=tk.W)
        self.lbl_furniture.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.frm_coords = tk.LabelFrame(self.frm_right_side, text="Coordinates")
        self.frm_coords.grid(
            row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW
        )

        tk.Label(self.frm_coords, text="X:").grid(
            row=0, column=0, padx=5, pady=5, sticky=tk.E
        )
        self.x = tk.IntVar()
        self.x.set(100)
        self.xcoord = tk.Entry(self.frm_coords, textvariable=self.x, width=5)
        self.xcoord.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)

        tk.Label(self.frm_coords, text="Y:").grid(
            row=0, column=2, padx=5, pady=5, sticky=tk.E
        )
        self.y = tk.IntVar()
        self.y.set(100)
        self.ycoord = tk.Entry(self.frm_coords, textvariable=self.y, width=5)
        self.ycoord.grid(row=0, column=3, padx=5, pady=5, sticky=tk.NSEW)

        self.btn_insert = tk.Button(
            self.frm_right_side,
            text="Insert",
            command=lambda: [
                self.furnish.insert(
                    self.cnv_room, self.cmb_furniture, (self.x.get(), self.y.get())
                )
            ],
        )
        self.btn_insert.grid(row=3, column=0, padx=5, pady=5, sticky=tk.NSEW)

        self.btn_undo = tk.Button(self.frm_right_side, text="Undo", command=self.undo)
        self.btn_undo.grid(row=3, column=1, padx=5, pady=5, sticky=tk.NSEW)

        self.furnish = furnish.Furnish()

        self.default_values()
        self.bindings()

        self.root.mainloop()

    def bindings(self):
        self.cmb_furniture.bind(
            "<<ComboboxSelected>>",
            lambda e: furniture.show_piece(
                self.lbl_furniture, self.cmb_furniture.get()
            ),
        )

    def default_values(self):
        self.size.set("400x400")
        self.cmb_furniture.current(0)
        furniture.show_piece(self.lbl_furniture, self.cmb_furniture.get())

    def enable_entry(self):
        if self.size.get() == "other":
            self.ent_other["state"] = "normal"
            self.ent_other.focus()
        else:
            self.ent_other["state"] = "disabled"

    def undo(self):
        if self.furnish.furniture:
            for k in self.furnish.furniture[-1].keys():
                self.cnv_room.delete(k)
            self.furnish.furniture.remove(self.furnish.furniture[-1])


def main():
    app = FurnishYourRoom()


if "__main__" in __name__:
    main()
