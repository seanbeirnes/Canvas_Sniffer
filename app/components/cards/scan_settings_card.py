# Main import
import customtkinter as ctk
from config.global_config import Global as G

# Components import
from components.cards.app_view_card import app_view_card
from components.buttons.toggle_button import Toggle_Button

class Scan_Settings_Card():
    def __init__(self, master, row) -> None:
        self.master = master
        self.card = app_view_card(self.master, row=row)

        # Configure card grid layout
        self.card.columnconfigure(0, weight=4)
        self.card.columnconfigure(1, weight=1)
        self.card.rowconfigure(0, weight=1)
        self.card.rowconfigure(1, weight=100)

        # Add heading
        label_settings = ctk.CTkLabel(self.card, text="Settings", font=G.font.get_card_heading())
        label_settings.grid(row = 0, column = 0, sticky=ctk.NW, padx=G.pad.p_md, pady=G.pad.p_sm)


        # Left Frame
        self.frame_left = ctk.CTkFrame(self.card, fg_color=G.color.COLOR_DARK_1, corner_radius=8)
        self.frame_left.grid(row = 1, column = 0, sticky = ctk.NSEW, padx=G.pad.p_md, pady=(0, G.pad.p_md))

        self.frame_left.columnconfigure(0, weight=1)
        self.frame_left.rowconfigure(0, weight=1)
        self.frame_left.rowconfigure(1, weight=10)
        self.frame_left.rowconfigure(2, weight=1)

        label_search_terms = ctk.CTkLabel(self.frame_left, text="Search Terms")
        label_search_terms.grid(row = 0, column = 0, sticky = ctk.N, padx=G.pad.p_md, pady=G.pad.p_sm)

        self.textbox = ctk.CTkTextbox(self.frame_left, height=72)
        self.textbox.grid(row=1, column = 0, sticky = ctk.NSEW, padx=G.pad.p_md, pady=(0, G.pad.p_sm))

        self.toggle_case_sensitive = Toggle_Button(master=self.frame_left, row=2, column=0, text="Case Sensitive")

        # Right Frame
        self.frame_right = ctk.CTkFrame(self.card, fg_color=G.color.COLOR_DARK_1, corner_radius=8)
        self.frame_right.grid(row = 1, column = 1, sticky = ctk.NSEW, padx=(0, G.pad.p_md), pady=(0, G.pad.p_md))

        # Toggle buttons for all, announcements, assignments, discussions, pages, module items
        # Dropdown for default, published, unpublished, student visible

