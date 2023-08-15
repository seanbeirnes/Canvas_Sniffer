# Main import
import customtkinter as ctk
from config.global_config import Global as G

# Components import
from components.cards.app_view_card import app_view_card
from components.buttons.dropdown_menu import Dropdown_Menu

class Scan_Course_Card():
    def __init__(self, master, row) -> None:
        self.master = master
        self.card = app_view_card(self.master, row=row)

        self.card.columnconfigure(0, weight=1)
        self.card.columnconfigure(1, weight=100)
        self.card.rowconfigure(0, weight=1)
        self.card.rowconfigure(1, weight=1)
        self.card.rowconfigure(2, weight=100)