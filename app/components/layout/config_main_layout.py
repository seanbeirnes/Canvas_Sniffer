import customtkinter as ctk

def config_main_layout(master) -> None:
    master.columnconfigure(0,minsize=216, weight=1)
    master.columnconfigure(1, weight=1000)
    master.rowconfigure(0, minsize=40, weight=1)      
    master.rowconfigure(1, minsize=560, weight=1000)