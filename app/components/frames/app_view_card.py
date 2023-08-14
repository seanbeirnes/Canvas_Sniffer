import customtkinter as ctk
from config.global_config import Global as G

def app_view_card(master, row):
    frame = ctk.CTkFrame(
            master=master, 
            corner_radius=16,
            fg_color=G.color.COLOR_DARK
            )
    
    frame.grid(row = row, column = 0, sticky=ctk.NSEW, pady=(0, G.pad.p_md), padx=0)
    
    return frame