# Main import
import customtkinter as ctk
from config.global_config import Global as G
from views.app.search_courses_view import Search_Courses_View

# Componenet import
from components.layout.header import Header
from components.layout.sidebar import Sidebar
# Controlls the main view of the app. Includes the header and main layout.

class App_View_Controller():
    def __init__(self, master, app_data) -> None:
        self.master = master
        self.app_data = app_data
        self.state = G.states.app_view.none

        self.header = Header(master=self.master, app_status=self.app_data.app_status)

        self.sidebar = Sidebar(master=self.master, btn_callback=self.setState)
    
    def update(self, app_data):
        self.app_data = app_data
        self.header.update(self.app_data.app_status)

    def setState(self, state):
        if state == G.states.app_view.course:
            # show relevant view
            self.state = state
        elif state == G.states.app_view.courses:
            # show relevant view
            self.state = state       
        elif state == G.states.app_view.settings:
            # show relevant view
            self.state = state     
        elif state == G.states.app_view.reset:
            # show relevant view
            self.state = state     
        elif state == G.states.app_view.help:
            # show relevant view
            self.state = state     
        elif state == G.states.app_view.about:
            # show relevant view
            self.state = state
        
        print({self.state})