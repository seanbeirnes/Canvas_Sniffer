# Main import
import customtkinter as ctk
from config.global_config import Global as G

# Componenets import
from components.frames.app_view_frame import app_view_frame
from components.cards.app_view_card import app_view_card
from components.cards.select_course_card import Select_Course_card

class Search_Course_View():

    def __init__(self, master) -> None:
        self.master = master
        self.frame = app_view_frame(self.master)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=3)
        self.frame.rowconfigure(2, weight=1)

        self.card_row_0 = Select_Course_card(self.frame, row=0)
        self.card_row_1 = app_view_card(self.frame, row=1)
        self.card_row_2 = app_view_card(self.frame, row=2)

        label_settings = ctk.CTkLabel(self.card_row_1, text="Settings", font=G.font.get_card_heading())
        label_settings.grid(row = 0, column = 0, sticky=ctk.NW, padx=G.pad.p_md, pady=G.pad.p_sm)

    def hide(self):
        self.frame.grid_remove()
        