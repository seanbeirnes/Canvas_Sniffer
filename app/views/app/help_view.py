import customtkinter as ctk

from components.frames.app_view_frame import app_view_frame

class Help_View():

    def __init__(self, master) -> None:
        self.master = master
        self.frame = app_view_frame(self.master)

    def hide(self):
        self.frame.grid_remove()
        