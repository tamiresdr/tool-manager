from tkinter import ttk

from PIL import Image, ImageTk

from tool_manager.color_map import color_map


def booking_page(frame_master):
    style = ttk.Style()
    style.configure('MainPageBooking.TFrame', background=color_map['background_central'])

    frame_page_booking = ttk.Frame(frame_master, style='MainPageBooking.TFrame')
    frame_page_booking.grid_rowconfigure(0, weight=1)
    frame_page_booking.grid_columnconfigure(0, weight=1)

    image = Image.open('tool_manager/images/work_in_progress.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    label = ttk.Label(
        frame_page_booking,
        text='[Reservas] Ops! Esta página ainda está em construção.',
        image=image,
        compound='top',
        background=color_map['background_central'],
        foreground=color_map['text'],
        font='Arial',
    )
    label.image = image   # fix tkinter bug

    frame_page_booking.grid(row=0, column=0, sticky='ewns')
    label.grid(row=0, column=0)
