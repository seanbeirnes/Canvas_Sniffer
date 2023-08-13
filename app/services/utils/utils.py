class Window_Utils():
    def center_window(win) -> None:
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

class Image_Utils():
    def get_image(url, size):
        from pathlib import Path
        from customtkinter import CTkImage
        from PIL import Image

        path = Path(__file__).parent / url

        img = Image.open(path)
        img = img.resize((img.width // 4, img.height // 4), resample=Image.LANCZOS)

        return CTkImage(img, size=size)