# Main import
import customtkinter as ctk
from config.global_config import Global as G
from views.app.search_courses_view import Search_Courses_View

# Componenet import
from components.layout.header import Header
from components.layout.sidebar import Sidebar

# Views improt
from views.app.search_course_view import Search_Course_View
from views.app.search_courses_view import Search_Courses_View
from views.app.settings_view import Settings_View
from views.app.help_view import Help_View
from views.app.about_view import About_View

# Controlls the main view of the app. Includes the header and main layout.

class App_View_Controller():
    def __init__(self, master, app_data) -> None:
        self.master = master
        self.app_data = app_data
        self.state = G.states.app_view.none

        self.view = None

        self.header = Header(master=self.master, app_status=self.app_data.app_status)

        self.sidebar = Sidebar(master=self.master, btn_callback=self.setState)
    
    def update(self, app_data):
        self.app_data = app_data
        self.header.update(self.app_data.app_status)

    def reset_view(self):
        if self.view:
            self.view.hide()

    def setState(self, state):
        self.reset_view()
        if state == G.states.app_view.course:
            self.view = Search_Course_View(self.master)
        elif state == G.states.app_view.courses:
            self.view = Search_Courses_View(self.master) 
        elif state == G.states.app_view.settings:
            self.view = Settings_View(self.master)
        elif state == G.states.app_view.reset:
            # Remind user this will reset all settings and cannot be undone
            # Ask if ok to proceed?
            # Reset app settings and take user back to startup flow
            pass
        elif state == G.states.app_view.help:
            self.view = Help_View(self.master)   
        elif state == G.states.app_view.about:
            self.view = About_View(self.master)
        
        self.state = state