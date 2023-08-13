import customtkinter as ctk
from config.global_config import Global as G

def static_header_text_label(master, text):
    label = ctk.CTkLabel(master=master, text=text, text_color=G.color.COLOR_ACCENT)

    label.pack(side="left", padx=(16, 0))
    
    return label