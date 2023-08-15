# Main import
import customtkinter as ctk
from config.global_config import Global as G

# Components import
from components.cards.app_view_card import app_view_card
from components.buttons.dropdown_menu import Dropdown_Menu

class Settings_Card():
    def __init__(self, master, row) -> None:
        self.master = master
        self.card = app_view_card(self.master, row=row)

        self.card.columnconfigure(0, weight=10)
        self.card.columnconfigure(1, weight=2)
        self.card.rowconfigure(0, weight=1)
        self.card.rowconfigure(1, weight=100)

        label_settings = ctk.CTkLabel(self.card, text="Settings", font=G.font.get_card_heading())
        label_settings.grid(row = 0, column = 0, sticky=ctk.NW, padx=G.pad.p_md, pady=G.pad.p_sm)

        frame_left = ctk.CTkLabel(self.card, )

