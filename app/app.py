# Main import
import customtkinter as ctk
from config.global_config import Global as G
from controllers.flow_controller import Flow_Controller

# Utils import
from services.utils.utils import Window_Utils

# Data import
from services.data import data

# Create window
window = ctk.CTk(fg_color=G.color.COLOR_DARK_3)

window.title("Canvas Sniffer")
window.minsize(width=918, height=688)

Window_Utils.center_window(window)

# Load data
app_status = data.App_Status(
    canvas_instance_url = "https://something.instructure.com",
    status = "Ready"
)

app_data = data.App_Data(app_status=app_status, app_message=None, callback_function=None)

flow_controller = Flow_Controller(window, app_data)
flow_controller.init()

# Run
window.mainloop()