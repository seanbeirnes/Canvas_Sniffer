# Main import
import customtkinter as ctk
from config.global_config import Global as G

# Components import
from components.cards.app_view_card import app_view_card
from components.buttons.toggle_button import Toggle_Button
from components.buttons.dropdown_menu import Dropdown_Menu

class Scan_Settings_Card():
    def __init__(self, master, row) -> None:
        self.master = master
        self.card = app_view_card(self.master, row=row)

        # Configure card grid layout
        self.card.columnconfigure(0, weight=4)
        self.card.columnconfigure(1, weight=1)
        self.card.rowconfigure(0, weight=1)
        self.card.rowconfigure(1, weight=100)
        self.card.rowconfigure(2, weight=8)

        # Add heading
        label_settings = ctk.CTkLabel(self.card, text="Settings", font=G.font.get_card_heading())
        label_settings.grid(row = 0, column = 0, sticky=ctk.NW, padx=G.pad.p_md, pady=G.pad.p_sm)


        # Left Frame
        self.frame_left = ctk.CTkFrame(self.card, fg_color=G.color.COLOR_DARK_1, corner_radius=8)
        self.frame_left.grid(row = 1, column = 0, rowspan = 2, sticky = ctk.NSEW, padx=G.pad.p_md, pady=(0, G.pad.p_md))

        self.frame_left.columnconfigure(0, weight=1)
        self.frame_left.rowconfigure(0, weight=1)
        self.frame_left.rowconfigure(1, weight=100)
        self.frame_left.rowconfigure(2, weight=1)

        label_search_terms = ctk.CTkLabel(self.frame_left, text="Search Terms")
        label_search_terms.grid(row = 0, column = 0, sticky = ctk.N, padx=G.pad.p_md, pady=G.pad.p_sm)

        self.textbox = ctk.CTkTextbox(self.frame_left, height=72)
        self.textbox.grid(row=1, column = 0, sticky = ctk.NSEW, padx=G.pad.p_md, pady=(0, G.pad.p_sm))
        self.textbox.insert("0.0", "Type in search terms here.\nEach new line is a new search term.")

        self.toggle_case_sensitive = Toggle_Button(master=self.frame_left, row=2, column=0, text="Case Sensitive")

        # Right Frame
        self.frame_right = ctk.CTkFrame(self.card, fg_color=G.color.COLOR_DARK_1, corner_radius=8)
        self.frame_right.grid(row = 1, column = 1, sticky = ctk.NSEW, padx=(0, G.pad.p_md), pady=(0, G.pad.p_md))

        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.rowconfigure(0, weight=1)
        self.frame_right.rowconfigure(1, weight=1)
        self.frame_right.rowconfigure(2, weight=1)
        self.frame_right.rowconfigure(3, weight=1)
        self.frame_right.rowconfigure(4, weight=1)
        self.frame_right.rowconfigure(5, weight=1)
        self.frame_right.rowconfigure(6, weight=1000)

        label_items_scanned = ctk.CTkLabel(self.frame_right, text="Items Scanned")
        label_items_scanned.grid(row = 0, column = 0, sticky = ctk.N, padx=G.pad.p_md, pady=G.pad.p_sm)

        self.toggle_announcements = Toggle_Button(master=self.frame_right, row=1, column=0, text="Announcements", active=True)
        self.toggle_assignments = Toggle_Button(master=self.frame_right, row=2, column=0, text="Assignments", active=True)
        self.toggle_discussions = Toggle_Button(master=self.frame_right, row=3, column=0, text="Discussions", active=True)
        self.toggle_pages = Toggle_Button(master=self.frame_right, row=4, column=0, text="Pages", active=True)
        self.toggle_moduleItems = Toggle_Button(master=self.frame_right, row=5, column=0, text="Module Items", pady=(0, G.pad.p_sm), active=True)

        # Bottom Frame
        self.frame_bottom = ctk.CTkFrame(self.card, fg_color=G.color.COLOR_DARK_1, corner_radius=8)
        self.frame_bottom.grid(row = 2, column = 1, sticky = ctk.NSEW, padx=(0, G.pad.p_md), pady=(0, G.pad.p_md))

        self.frame_bottom.columnconfigure(0, weight=1)
        self.frame_bottom.rowconfigure(0, weight=1)
        self.frame_bottom.rowconfigure(1, weight=1)

        label_scan_mode = ctk.CTkLabel(self.frame_bottom, text="Scan Mode")
        label_scan_mode.grid(row = 0, column = 0, sticky = ctk.N, padx=G.pad.p_md, pady=(G.pad.p_sm,0))

        self.dropdown_selectCourse = Dropdown_Menu(master=self.frame_bottom,
                                              values=["Default", "Published", "Unpublished", "Student Visible"],
                                              placeholder="Select mode...",
                                              row=1,
                                              column=0)
        self.dropdown_selectCourse.set_width(width=168)

