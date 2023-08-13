# Main import
import customtkinter as ctk
from config.global_config import Global as G
from views.app.search_courses_view import Search_Courses_View

# Componenet import
from components.layout.header_frame import header_frame
from components.labels.static_header_text_label import static_header_text_label


# Controlls the main view of the app. Includes the header and main layout.

class App_View_Controller():
    def __init__(self, master) -> None:
        self.master = master
    
    def init(self):
        self.frame_header = header_frame(self.master)

        self.label_canvasInstance = static_header_text_label(
            master=self.frame_header,
            text="Canvas Instance: "
            )