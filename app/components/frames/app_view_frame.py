import customtkinter as ctk
from config.global_config import Global as G

def app_view_frame(master):
    frame = ctk.CTkFrame(
            master=master, 
            corner_radius=0,
            fg_color="transparent"
            )
    
    frame.grid(row = 1, column = 1, sticky=ctk.NSEW, pady=(G.pad.p_md, 0), padx=(0,G.pad.p_md))
    
    return frame