import customtkinter as ctk
from config.global_config import Global as G

def app_view_frame(master):
    frame = ctk.CTkFrame(
            master=master, 
            corner_radius=16,
            fg_color=G.color.COLOR_DARK
            )
    
    frame.grid(row = 1, column = 1, sticky=ctk.NSEW, pady=G.pad.p_md, padx=(0,G.pad.p_md))
    
    return frame