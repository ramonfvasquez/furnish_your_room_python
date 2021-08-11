def set_room_size(option, canvas):
    coords = option.get().split("x")
    x = coords[0]
    y = coords[1]
    canvas.config(width=x, height=y)
