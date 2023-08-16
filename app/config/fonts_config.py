class Fonts():
    def get_card_heading(self):
        import customtkinter as ctk
        return ctk.CTkFont(family=None, size=16, weight="bold")
    
    def get_xs_font(self):
        import customtkinter as ctk
        return ctk.CTkFont(family=None, size=8, weight="bold")