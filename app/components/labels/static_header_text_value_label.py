import customtkinter as ctk
from config.global_config import Global as G

def static_header_text_value_label(master, text):
    label = ctk.CTkLabel(master=master, text=text, text_color=G.color.COLOR_LIGHT)

    label.pack(side="left")
    
    return label