from components.frames.header_frame import header_frame
from components.labels.static_header_text_label import static_header_text_label
from components.labels.static_header_text_value_label import static_header_text_value_label

class Header():
    def __init__(self, master, app_status) -> None:
        self.master = master
        self.canvasInstance = app_status.canvas_instance_url
        self.status = app_status.status

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

    def update(self, app_status):
        self.canvasInstance = app_status.canvas_instance_url
        self.status = app_status.status

        self.label_canvasInstance_value.configure(text = self.canvasInstance)
        self.label_status_value.configure(text = self.status)