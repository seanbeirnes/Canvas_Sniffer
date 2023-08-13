# Creates data objects with all necessary information that
# can be passed up and down the different application layers.

class App_Status():
    def __init__(self,
                 status,
                 canvas_instance_url,
                 ) -> None:
        self.status = status
        self.canvas_instance_url = canvas_instance_url
        
class App_Message():
    def __init__(self,
                 type,
                 text) -> None:
        self.type = type
        self.text = text
     
class App_Data():
    def __init__(
            self,
            # Takes App_Status data object
            app_status,
            app_message,
            callback_function
            ) -> None:
        self.app_status = app_status
        self.app_message = app_message
        self.callback_function = callback_function