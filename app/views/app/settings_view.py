# Main import
import customtkinter as ctk

# Componenets improt
from components.frames.app_view_frame import app_view_frame
from components.frames.app_view_card import app_view_card

class Settings_View():

    def __init__(self, master) -> None:
        self.master = master
        self.frame = app_view_frame(self.master)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)

        self.card_row_0 = app_view_card(self.frame, row=0)
        self.card_row_1 = app_view_card(self.frame, row=1)
        self.card_row_2 = app_view_card(self.frame, row=2)
        self.card_row_3 = app_view_card(self.frame, row=3)

    def hide(self):
        self.frame.grid_remove()
        