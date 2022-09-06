from tkinter import Tk, ttk

from tool_manager.booking.views import booking_page
from tool_manager.color_map import color_map
from tool_manager.home.views import home_page
from tool_manager.statistic.views import statistics_page
from tool_manager.tools.views import tools_page
from tool_manager.users.views import users_page
from tool_manager.utils import build_menu_button


class Application(Tk):
    def __init__(self):
        super().__init__()

        # ROOT
        self.title('Tool Manager')
        self.geometry('1320x700')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # STYLE
        style = ttk.Style()
        style.configure('MainFrame.TFrame', background='blue')
        style.configure('MainMenu.TFrame', background=color_map['background_menu'])
        style.configure('MainPage.TFrame', background='orange')

        # PAGES
        frame_master = ttk.Frame(self, style='MainFrame.TFrame')
        frame_master.grid_rowconfigure(0, weight=1)
        frame_master.grid_columnconfigure(1, weight=1)

        frame_menu = ttk.Frame(frame_master, style='MainMenu.TFrame', width=300)

        frame_page = ttk.Frame(frame_master, style='MainPage.TFrame')
        frame_page.grid_rowconfigure(0, weight=1)
        frame_page.grid_columnconfigure(0, weight=1)

        # GRID WIDGETS
        frame_master.grid(row=0, column=0, sticky='ewns')
        frame_menu.grid(row=0, column=0, sticky='wns')
        frame_page.grid(row=0, column=1, sticky='ewns')

        home_page(frame_master=frame_page)
        self.build_menu(frame_master=frame_page, frame_menu=frame_menu)

    def build_menu(self, frame_master, frame_menu):
        build_menu_button(
            frame_menu,
            row=0,
            column=0,
            text='Home',
            image='tool_manager/images/home.png',
            bcolor=color_map['background_central'],
            fcolor=color_map['background_menu'],
            cmd=lambda: home_page(frame_master),
        )
        build_menu_button(
            frame_menu,
            row=1,
            column=0,
            text='Estatísticas',
            image='tool_manager/images/statistics.png',
            bcolor=color_map['background_central'],
            fcolor=color_map['background_menu'],
            cmd=lambda: statistics_page(frame_master),
        )
        build_menu_button(
            frame_menu,
            row=2,
            column=0,
            text='Reservas',
            image='tool_manager/images/booking.png',
            bcolor=color_map['background_central'],
            fcolor=color_map['background_menu'],
            cmd=lambda: booking_page(frame_master),
        )
        build_menu_button(
            frame_menu,
            row=3,
            column=0,
            text='Ferramentas',
            image='tool_manager/images/tools.png',
            bcolor=color_map['background_central'],
            fcolor=color_map['background_menu'],
            cmd=lambda: tools_page(frame_master),
        )
        build_menu_button(
            frame_menu,
            row=4,
            column=0,
            text='Usuários',
            image='tool_manager/images/users.png',
            bcolor=color_map['background_central'],
            fcolor=color_map['background_menu'],
            cmd=lambda: users_page(frame_master),
        )
