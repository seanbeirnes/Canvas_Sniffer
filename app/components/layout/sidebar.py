from components.frames.sidebar_frame import sidebar_frame

class Sidebar():
    def __init__(self, master) -> None:
        self.master = master

    def init(self) -> None:
        self.sidebar = sidebar_frame(master=self.master)