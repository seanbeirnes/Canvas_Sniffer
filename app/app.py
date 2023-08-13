import customtkinter as ctk
from controllers.flow_controller import Flow_Controller


# Create window
window = ctk.CTk()
window.title("Canvas Sniffer")
window.minsize(width=800, height=600)

flow_controller = Flow_Controller(window)
flow_controller.init()

# Run
window.mainloop()