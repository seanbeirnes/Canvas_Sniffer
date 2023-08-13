from controllers.app_view_controller import App_View_Controller

from components.layout.config_main_layout import config_main_layout

# Controls the folow between the initial setup view and the main view of the application.

class Flow_Controller():
    def __init__(self, master, app_data) -> None:
        self.master = master
        self.app_data = app_data

    def init(self):
        self.show_main_app()

    def show_main_app(self):
        config_main_layout(self.master)

        app_view_controller = App_View_Controller(
            master = self.master, 
            app_data = self.app_data
            )