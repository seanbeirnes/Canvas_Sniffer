import customtkinter as ctk
from config.global_config import Global as G

def header_frame(master):
    frame = ctk.CTkFrame(
        master=master, 
        height=40,
        corner_radius=0,
        fg_color=G.color.COLOR_DARK
        )
        
    frame.grid(row = 0, column = 0, sticky=ctk.NSEW, columnspan = 2)
    
    return frame