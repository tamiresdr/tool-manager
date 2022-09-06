from tkinter import Button

from PIL import Image, ImageTk

from tool_manager.color_map import color_map


def build_menu_button(frame_master, row, column, text, image, bcolor, fcolor, cmd):
    image = Image.open(image)
    image = image.resize((35, 35), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    button = Button(
        frame_master,
        text=text,
        width=250,
        height=50,
        fg=color_map['text'],
        border=0,
        bg=fcolor,
        activeforeground=color_map['text'],
        activebackground=bcolor,
        command=cmd,
        image=image,
        compound='left',
        anchor='w',
        highlightthickness=0,
    )

    button.image = image   # fix tkinter bug

    def on_entering(e):
        button['background'] = bcolor
        button['foreground'] = color_map['text']

    def on_leaving(e):
        button['background'] = fcolor
        button['foreground'] = color_map['text']

    button.bind('<Enter>', on_entering)
    button.bind('<Leave>', on_leaving)

    button.grid(row=row, column=column)
