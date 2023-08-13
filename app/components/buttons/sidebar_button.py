import customtkinter as ctk
from config.global_config import Global as G
from services.utils.utils import Image_Utils

class Sidebar_Button():
    def __init__(self,
                 master,
                 text,
                 light_image_url,
                 dark_image_url,
                 command
                 ) -> None:
        
        self.__light_image = Image_Utils.get_image(light_image_url, (20,20))
        self.__dark_image = Image_Utils.get_image(dark_image_url, (20,20))
        self.master = master
        self.text = text
        self.command = command

        self.button = ctk.CTkButton(master=self.master, image=self.__light_image, corner_radius=100, fg_color=G.color.COLOR_PRIMARY_2, hover_color=G.color.COLOR_PRIMARY_1, text_color_disabled=G.color.COLOR_DARK, text=self.text, compound="right", command=self.command)
        self.button.pack(padx=G.pad.p_sm, pady=G.pad.p_sm, fill="x")