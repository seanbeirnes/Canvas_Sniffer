# Main import
import customtkinter as ctk
from config.global_config import Global as G

class Toggle_Button():
    states = {"inactive": 0,
              "active": 1}
    
    def __init__(self, master, row, column, text, active=False) -> None:
        self.master=master
        self.active=False
        self.toggle_button = ctk.CTkSwitch(self.master, 
                                           text=text, 
                                           text_color=G.color.COLOR_DARK_3, 
                                           progress_color=G.color.COLOR_PRIMARY_1, 
                                           fg_color=G.color.COLOR_DARK_3,
                                           command=self.select,
                                           )
        self.toggle_button.grid(row=row, column = column, sticky = ctk.NW, padx=G.pad.p_md, pady=G.pad.p_sm)
        if active:
            self.toggle_button.toggle()

    def select(self):
        if self.active:
            self.toggle_button.configure(text_color=G.color.COLOR_DARK_3)
            self.active = False
        else:
            self.toggle_button.configure(text_color=G.color.COLOR_LIGHT)
            self.active = True