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
    
    def init(self):
        self.header = Header(master=self.master, app_status=self.app_data.app_status)
        self.header.init()

        self.sidebar = Sidebar(master=self.master)
        self.sidebar.init()

    def update(self, app_data):
        self.app_data = app_data
        self.header.update(self.app_data.app_status)
