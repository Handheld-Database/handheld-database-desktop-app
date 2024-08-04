import tkinter as tk                

# Import the windows 
from UI import Game_Window
from UI import Game_W_Manual
from UI import Game_W_Automatic
from UI import Platfrom_Window
from UI import System_Window
from UI import Menu_Window

from UI import app_manager as manager

# Application to make contributing to the Handheld Database easier.
# WORK IN PROGRESS

# Base of the application
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Making the windows which will contain the containers
        self.geometry("1024x768")
        # Setting the minimum and maximum size of the window.
        self.minsize(1024,768)
        self.maxsize(1024,768)
        # Setting the title of the app.
        self.title("Handheld Database")
        # Setting the icon of the app.
        self.iconbitmap("./desktop_app/materials/favicon.ico")

        # Making the container to store the windows and switch between them
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        
        self.frames = {}
        for F in (Menu_Window.Menu_Window, Platfrom_Window.Platfrom_Window, System_Window.System_Window, Game_Window.Game_Window, Game_W_Manual.Game_W_Manual, Game_W_Automatic.Game_W_Automatic):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu_Window")

    # Change whitch window is shown by the page name.
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()  # Lifts the appropriate frame to the top, so it is shown.



if __name__ == "__main__":
    app = App()
    app.mainloop()