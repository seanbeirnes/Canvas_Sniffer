import customtkinter as ctk
from config.global_config import Global as G

from services.utils.utils import Image_Utils

from components.frames.sidebar_frame import sidebar_frame
from components.buttons.sidebar_button import Sidebar_Button



class Sidebar():
    def __init__(self, master) -> None:
        self.master = master

    def init(self) -> None:
        self.sidebar = sidebar_frame(master=self.master)

        label_logo = ctk.CTkLabel(master=self.sidebar, image=Image_Utils.get_image("../../assets/logos/canvas-sniffer-logo.png", (118, 47)), text="")
        label_logo.pack(fill="both", pady=G.pad.p_md, padx=G.pad.p_md)

        self.button_searchCourse = Sidebar_Button(master=self.sidebar,
                                                  text="Search Course",
                                                  light_image_url="../../assets/icons/course/course_light.png",
                                                  dark_image_url="../../assets/icons/course/course_dark.png",
                                                  command=None)
        self.button_searchCourse.init()

        self.button_searchCourses = Sidebar_Button(master=self.sidebar,
                                                   text="Search Courses",
                                                   light_image_url="../../assets/icons/courses/courses_light.png",
                                                   dark_image_url="../../assets/icons/courses/courses_dark.png",
                                                   command=None)
        self.button_searchCourses.init()

        self.button_settings = Sidebar_Button(master=self.sidebar,
                                                   text="Settings",
                                                   light_image_url="../../assets/icons/gear/gear_light.png",
                                                   dark_image_url="../../assets/icons/gear/gear_dark.png",
                                                   command=None)
        self.button_settings.init()

        self.button_reset = Sidebar_Button(master=self.sidebar,
                                                   text="Reset",
                                                   light_image_url="../../assets/icons/refresh/refresh_light.png",
                                                   dark_image_url="../../assets/icons/refresh/refresh_dark.png",
                                                   command=None)
        self.button_reset.init()

        self.button_help = Sidebar_Button(master=self.sidebar,
                                                   text="Help",
                                                   light_image_url="../../assets/icons/help/help_light.png",
                                                   dark_image_url="../../assets/icons/help/help_dark.png",
                                                   command=None)
        self.button_help.init()

        self.button_about = Sidebar_Button(master=self.sidebar,
                                                   text="About",
                                                   light_image_url="../../assets/icons/info/info_light.png",
                                                   dark_image_url="../../assets/icons/info/info_dark.png",
                                                   command=None)
        self.button_about.init()

        label_version = ctk.CTkLabel(master=self.sidebar, text=G.about.info, justify="left")
        label_version.pack(side="bottom", padx=G.pad.p_md, pady=G.pad.p_md)