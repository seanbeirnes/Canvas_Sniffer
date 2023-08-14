# Main import
import customtkinter as ctk
from config.global_config import Global as G
from views.app.search_courses_view import Search_Courses_View

# Componenet import
from components.layout.header import Header
from components.layout.sidebar import Sidebar

# Views improt
from views.app.help_view import Help_View

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
            # show relevant view
            pass
        elif state == G.states.app_view.courses:
            # show relevant view
            pass   
        elif state == G.states.app_view.settings:
            # show relevant view   
            pass 
        elif state == G.states.app_view.reset:
            # show relevant view  
            pass
        elif state == G.states.app_view.help:
            self.view = Help_View(self.master)   
        elif state == G.states.app_view.about:
            # show relevant view
            pass
        
        self.state = state
        print({self.state})