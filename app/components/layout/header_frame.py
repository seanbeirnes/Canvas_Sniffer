import customtkinter as ctk
from config.global_config import Global as G

def header_frame(master):
    frame = frame_header = ctk.CTkFrame(
            master=master, 
            height=40,
            corner_radius=0,
            fg_color=G.color.COLOR_DARK
            )
        
    frame_header.pack(fill="both")
    
    return frame