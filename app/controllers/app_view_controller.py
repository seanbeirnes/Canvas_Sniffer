# Main import
import customtkinter as ctk
from config.global_config import Global as G
from views.app.search_courses_view import Search_Courses_View

# Componenet import
from components.layout.header_frame import header_frame

from components.labels.static_header_text_label import static_header_text_label
from components.labels.static_header_text_value_label import static_header_text_value_label


# Controlls the main view of the app. Includes the header and main layout.

class App_View_Controller():
    def __init__(self, master) -> None:
        self.master = master
        self.canvasInstance = "https://something.instructure.com"
        self.status = "Ready"
    
    def init(self):
        self.frame_header = header_frame(self.master)

        self.label_canvasInstance = static_header_text_label(
            master=self.frame_header,
            text="Canvas Instance: "
            )
        
        self.label_canvasInstance_value = static_header_text_value_label(
            master=self.frame_header,
            text=self.canvasInstance
        )
        
        self.label_status = static_header_text_label(
            master=self.frame_header,
            text="Status: "
            )
        
        self.label_status_value = static_header_text_value_label(
            master=self.frame_header,
            text=self.status
        )