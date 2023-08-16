# Main import
import customtkinter as ctk
from config.global_config import Global as G

# Components import
from components.cards.app_view_card import app_view_card
from components.buttons.dropdown_menu import Dropdown_Menu

class Select_Course_card():
    def __init__(self, master, row) -> None:
        self.master = master
        self.card = app_view_card(self.master, row=row)

        self.card.columnconfigure(0, weight=1)
        self.card.columnconfigure(1, weight=100)
        self.card.rowconfigure(0, weight=1)
        self.card.rowconfigure(1, weight=1)
        self.card.rowconfigure(2, weight=100)

        label_select_course = ctk.CTkLabel(self.card, text="Select Course", font=G.font.get_card_heading())
        label_select_course.grid(row = 0, column = 0, sticky=ctk.NW, padx=G.pad.p_md, pady=G.pad.p_sm)

        dropdown_selectCourse = Dropdown_Menu(master=self.card,
                                              values=["Course ID", "SIS ID"],
                                              placeholder="Select by...",
                                              row=2,
                                              column=0)
        dropdown_selectCourse.set_width(width=168)

        entry_selectCourse = ctk.CTkEntry(self.card,
                                          width=2000,
                                          corner_radius=8,
                                          fg_color=G.color.COLOR_DARK_3)
        entry_selectCourse.grid(row = 2, column = 1, sticky=ctk.NW, padx=G.pad.p_md, pady=G.pad.p_sm)