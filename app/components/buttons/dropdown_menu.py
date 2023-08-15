# Main import
import customtkinter as ctk
from config.global_config import Global as G

class Dropdown_Menu():
    def __init__(self, master, values, placeholder, row, column) -> None:
        self.dropdownMenu = ctk.CTkOptionMenu(master=master, 
                                              values=values,
                                              corner_radius=8,
                                              fg_color=G.color.COLOR_PRIMARY_2,
                                              button_color=G.color.COLOR_PRIMARY_3,
                                              dropdown_hover_color=G.color.COLOR_PRIMARY_1
                                              )
        self.dropdownMenu.set(placeholder)
        self.dropdownMenu.grid(row = row, column = column, sticky=ctk.NW, padx=G.pad.p_md, pady=G.pad.p_sm)

    def set_width(self, width):
        self.dropdownMenu.configure(width=width)