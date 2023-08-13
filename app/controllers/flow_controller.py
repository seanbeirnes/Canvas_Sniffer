from controllers.app_view_controller import App_View_Controller

# Controls the folow between the initial setup view and the main view of the application.

class Flow_Controller():
    def __init__(self, master, app_data) -> None:
        self.master = master
        self.app_data = app_data

    def init(self):
        app_view_controller = App_View_Controller(
            master = self.master, 
            app_data = self.app_data
            )
        
        app_view_controller.init()