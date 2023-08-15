# Main import
import customtkinter as ctk
from config.global_config import Global as G

# Componenets import
from components.frames.app_view_frame import app_view_frame
from components.cards.select_course_card import Select_Course_card
from components.cards.scan_settings_card import Scan_Settings_Card
from components.cards.scan_course_card import Scan_Course_Card

class Search_Course_View():

    def __init__(self, master) -> None:
        self.master = master
        self.frame = app_view_frame(self.master)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=50)
        self.frame.rowconfigure(2, weight=10)

        self.card_row_0 = Select_Course_card(self.frame, row=0)
        self.card_row_1 = Scan_Settings_Card(self.frame, row=1)
        self.card_row_2 = Scan_Course_Card(self.frame, row=2)

    def hide(self):
        self.frame.grid_remove()
        