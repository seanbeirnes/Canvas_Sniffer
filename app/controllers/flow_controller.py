from controllers.app_view_controller import App_View_Controller

# Controls the folow between the initial setup view and the main view of the application.

class Flow_Controller():
    def __init__(self, master) -> None:
        self.master = master

    def init(self):
        app_view_controller = App_View_Controller(self.master)
        app_view_controller.init()