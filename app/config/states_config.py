class App_View_Controller_States():
    none = 0
    course = 100
    courses = 200
    settings = 300
    reset = 400
    help = 500
    about = 600

class Sidebar_Button_States():
    normal = 0
    active = 1
    disabled = 3

class Sidebar_States():
    none = 0
    search_course = 10
    search_courses = 20
    settings = 30
    reset = 40
    help = 50
    about = 60

class States():
    app_view = App_View_Controller_States()
    sidebar_btn = Sidebar_Button_States()
    sidebar = Sidebar_States()
