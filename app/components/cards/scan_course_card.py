# Main import
import customtkinter as ctk
from config.global_config import Global as G

# Components import
from components.cards.app_view_card import app_view_card
from components.buttons.dropdown_menu import Dropdown_Menu

class Scan_Course_Card():
    def __init__(self, master, row) -> None:
        self.master = master
        self.card = app_view_card(self.master, row=row)

        self.card.columnconfigure(0, weight=100)
        self.card.columnconfigure(1, weight=1)
        self.card.rowconfigure(0, weight=1)
        self.card.rowconfigure(1, weight=1)
        self.card.rowconfigure(2, weight=1)
        self.card.rowconfigure(3, weight=1)
        self.card.rowconfigure(4, weight=1)
        self.card.rowconfigure(5, weight=1)

        scan_button = ctk.CTkButton(self.card, height=32, text="Start Scan", corner_radius=8, fg_color=G.color.COLOR_ACCENT, text_color=G.color.COLOR_DARK_2, hover_color=G.color.COLOR_LIGHT)
        scan_button.grid(row = 0, column = 0, columnspan=2, sticky = ctk.N, padx=G.pad.p_md, pady=(G.pad.p_md, 0))

        label_total_progress = ctk.CTkLabel(self.card, text="Scanning course 4 of 20")
        label_total_progress.grid(row = 1, column = 0, sticky = ctk.NW, padx=G.pad.p_md, pady=(0,G.pad.p_sm))

        progressBar_total = ctk.CTkProgressBar(self.card, 
                                               fg_color=G.color.COLOR_DARK_3, 
                                               progress_color=G.color.COLOR_PRIMARY_2)
        progressBar_total.grid(row = 2, column = 0, sticky = ctk.NSEW, padx=(G.pad.p_md, 0), pady=(0,G.pad.p_sm))
        progressBar_total.set(value=0.112) #Sets progress bar percentage

        label_progressBar_total_text = ctk.CTkLabel(self.card, text="11.2%", text_color=G.color.COLOR_PRIMARY_1)
        label_progressBar_total_text.grid(row = 2, column = 1, sticky = ctk.NSEW, padx=G.pad.p_sm, pady=(0,G.pad.p_sm))

        label_task_progress = ctk.CTkLabel(self.card, text="Scanning page 22 of 200")
        label_task_progress.grid(row = 3, column = 0, columnspan=2, sticky = ctk.NW, padx=G.pad.p_md, pady=(0,G.pad.p_sm))

        progressBar_task = ctk.CTkProgressBar(self.card, 
                                               fg_color=G.color.COLOR_DARK_3, 
                                               progress_color=G.color.COLOR_PRIMARY_2)
        progressBar_task.grid(row = 4, column = 0, sticky = ctk.NSEW, padx=(G.pad.p_md, 0), pady=(0,G.pad.p_sm))
        progressBar_task.set(value=0.112) #Sets progress bar percentage

        label_progressBar_total_task = ctk.CTkLabel(self.card, text="11.2%", text_color=G.color.COLOR_PRIMARY_1)
        label_progressBar_total_task.grid(row = 4, column = 1, sticky = ctk.NSEW, padx=G.pad.p_sm, pady=(0,G.pad.p_sm))

        label_task_message = ctk.CTkLabel(self.card, text="Scanning page #234234 in course 'Title of Course'", font=G.font.get_xs_font())
        label_task_message.grid(row = 5, column = 0, columnspan=2, sticky = ctk.NW, padx=G.pad.p_md, pady=(0,G.pad.p_sm))