import customtkinter as ctk
from config.global_config import Global as G

from services.utils.utils import Image_Utils

from components.frames.sidebar_frame import sidebar_frame
from components.buttons.sidebar_button import Sidebar_Button



class Sidebar():
    def __init__(self, master, btn_callback) -> None:
        self.master = master
        self.__btn_callback = btn_callback
        self.state = G.states.sidebar.none

        self.sidebar = sidebar_frame(master=self.master)

        label_logo = ctk.CTkLabel(master=self.sidebar, image=Image_Utils.get_image("../../assets/logos/canvas-sniffer-logo.png", (118, 47)), text="")
        label_logo.pack(fill="both", pady=G.pad.p_md, padx=G.pad.p_md)

        self.button_searchCourse = Sidebar_Button(master=self.sidebar,
                                                  text="Search Course",
                                                  light_image_url="../../assets/icons/course/course_light.png",
                                                  dark_image_url="../../assets/icons/course/course_dark.png",
                                                  command=lambda: self.setState(G.states.sidebar.search_course))

        self.button_searchCourses = Sidebar_Button(master=self.sidebar,
                                                   text="Search Courses",
                                                   light_image_url="../../assets/icons/courses/courses_light.png",
                                                   dark_image_url="../../assets/icons/courses/courses_dark.png",
                                                   command=lambda: self.setState(G.states.sidebar.search_courses))

        self.button_settings = Sidebar_Button(master=self.sidebar,
                                                   text="Settings",
                                                   light_image_url="../../assets/icons/gear/gear_light.png",
                                                   dark_image_url="../../assets/icons/gear/gear_dark.png",
                                                   command=lambda: self.setState(G.states.sidebar.settings))

        self.button_reset = Sidebar_Button(master=self.sidebar,
                                                   text="Reset",
                                                   light_image_url="../../assets/icons/refresh/refresh_light.png",
                                                   dark_image_url="../../assets/icons/refresh/refresh_dark.png",
                                                   command=lambda: self.setState(G.states.sidebar.reset))

        self.button_help = Sidebar_Button(master=self.sidebar,
                                                   text="Help",
                                                   light_image_url="../../assets/icons/help/help_light.png",
                                                   dark_image_url="../../assets/icons/help/help_dark.png",
                                                   command=lambda: self.setState(G.states.sidebar.help))

        self.button_about = Sidebar_Button(master=self.sidebar,
                                                   text="About",
                                                   light_image_url="../../assets/icons/info/info_light.png",
                                                   dark_image_url="../../assets/icons/info/info_dark.png",
                                                   command=lambda: self.setState(G.states.sidebar.about))

        label_version = ctk.CTkLabel(master=self.sidebar, text=G.about.info, justify="left")
        label_version.pack(side="bottom", padx=G.pad.p_md, pady=G.pad.p_md)

    def reset_buttons(self):
        self.button_searchCourse.setState(G.states.sidebar_btn.normal)
        self.button_searchCourses.setState(G.states.sidebar_btn.normal)
        self.button_settings.setState(G.states.sidebar_btn.normal)
        self.button_reset.setState(G.states.sidebar_btn.normal)
        self.button_help.setState(G.states.sidebar_btn.normal)
        self.button_about.setState(G.states.sidebar_btn.normal)

    def setState(self, state):
        if state == G.states.sidebar.search_course:
            self.reset_buttons()
            self.button_searchCourse.setState(G.states.sidebar_btn.active)
            self.__btn_callback(state=G.states.app_view.course)
            self.state = state
        elif state == G.states.sidebar.search_courses:
            self.reset_buttons()
            self.button_searchCourses.setState(G.states.sidebar_btn.active)
            self.__btn_callback(state=G.states.app_view.courses)
            self.state = state
        elif state == G.states.sidebar.settings:
            self.reset_buttons()
            self.button_settings.setState(G.states.sidebar_btn.active)
            self.__btn_callback(state=G.states.app_view.settings)
            self.state = state
        elif state == G.states.sidebar.reset:
            self.reset_buttons()
            self.button_reset.setState(G.states.sidebar_btn.active)
            self.__btn_callback(state=G.states.app_view.reset)
            self.state = state
        elif state == G.states.sidebar.help:
            self.reset_buttons()
            self.button_help.setState(G.states.sidebar_btn.active)
            self.__btn_callback(state=G.states.app_view.help)
            self.state = state
        elif state == G.states.sidebar.about:
            self.reset_buttons()
            self.button_about.setState(G.states.sidebar_btn.active)
            self.__btn_callback(state=G.states.app_view.about)
            self.state = state