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
        self.state = G.states.sidebar_btn.normal

        self.button = ctk.CTkButton(master=self.master, image=self.__light_image, corner_radius=100, fg_color=G.color.COLOR_PRIMARY_2, hover_color=G.color.COLOR_PRIMARY_1, text_color_disabled=G.color.COLOR_DARK, text=self.text, compound="right", command=self.command)
        self.button.pack(padx=G.pad.p_sm, pady=G.pad.p_sm, fill="x")

    def setState(self, state):
        if state == G.states.sidebar_btn.active:
            self.button.configure(fg_color=G.color.COLOR_ACCENT, 
                                  hover_color=G.color.COLOR_ACCENT,
                                  state="disabled",
                                  image=self.__dark_image)
            self.state = state
        elif state == G.states.sidebar_btn.normal:
            self.button.configure(fg_color=G.color.COLOR_PRIMARY_2,
                                  hover_color=G.color.COLOR_PRIMARY_1,
                                  state="normal",
                                  image=self.__light_image)
            self.state = state