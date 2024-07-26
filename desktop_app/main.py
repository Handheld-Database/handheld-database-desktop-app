import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import PhotoImage
from tkinter import messagebox


# Application to make contributing to the Handheld Database easier.
# WORK IN PROGRESS

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Making the windows which will contain the containers
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("1024x768")
        # Setting the minimum and maximum size of the window.
        self.minsize(1024,768)
        self.maxsize(1024,768)
        # Setting the title of the app.
        self.title("Handheld Database")
        # Setting the icon of the app.
        self.iconbitmap("./desktop_app/images/favicon.ico")
       

        # Making the container to store the windows and switch between them
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu_Window, Platfrom_Window, System_Window, Game_Window):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu_Window")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


# Making the main menu window
class Menu_Window(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        title = tk.Label(self, text="WELCOME!", font=('Arial', 32))
        title.pack(pady=20)

        lbl1 = tk.Label(self, text="""This application is for contributing to the Handheld Database.
Please select what you want to add to the database.
WORK IN PROGRESS""", font=('Arial', 28), anchor="center")
        lbl1.pack(pady=10)

        #------------------------------------------------------------------------------------------
        # Importing images for the buttons
        platform_Img = PhotoImage(file="./desktop_app/images/platform.png") # https://www.vecteezy.com/vector-art/3331132-hand-holding-portable-video-game-console-vector-icon
        system_Img = PhotoImage(file="./desktop_app/images/system.png") # https://www.flaticon.com/free-icon/emulator_8560002
        game_Img = PhotoImage(file="./desktop_app/images/game.png") # https://www.freepik.com/icon/game_12595961#fromView=keyword&page=1&position=3&uuid=b4f88723-ace5-456f-8a25-f54ac9151ca2

        # Making a frame for the buttons.
        buttonframe = tk.Frame(self)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)

        # Add Plafrom button.
        platform = tk.Button(buttonframe, image=platform_Img, command=lambda: controller.show_frame("Platfrom_Window"))  
        platform.img = platform_Img
        platform.grid(row=0, column=0,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        platform_Lbl = tk.Label(buttonframe, text="PLATFORM", font=('Arial', 32))
        platform_Lbl.grid(row=1, column=0)
        # Add System button.
        system = tk.Button(buttonframe, image=system_Img, command=lambda: controller.show_frame("System_Window"))  
        system.img = system_Img
        system.grid(row=0, column=1,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        system_Lbl = tk.Label(buttonframe, text="SYSTEM", font=('Arial', 32))
        system_Lbl.grid(row=1, column=1)
        # Add game button.
        game = tk.Button(buttonframe, image=game_Img, command=lambda: controller.show_frame("Game_Window"))
        game.img = game_Img
        game.grid(row=0, column=2, sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        game_Lbl = tk.Label(buttonframe, text="GAME", font=('Arial', 32))
        game_Lbl.grid(row=1, column=2)
        buttonframe.pack(pady=40)
        #------------------------------------------------------------------------------------------

        tk.Label(self, text="""For the Handheld-Database
Made by meeeaCH""", font=('Arial', 18), justify="center").pack()

        # Making the HELP button
        help = tk.Button(self, text="HELP", font=('Arial', 12), command=self.help_Btn_Func) 
        help.pack(side="right", padx=20, pady=12)
        self.pack()

    # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """In this section you can chose what you want to add to the database.
-Click the "PLATFORM" button to add a new platfrom. (For example: R36S, TSP)
-Click the "SYSTEM" button to add a new system to a platform. (For example: PSP, GBA)
-Click the "GAME" button to add a new game to a system.
"""
        messagebox.showinfo("Main Menu Info", main_menu) 


# Making the Platfrom window
class Platfrom_Window(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Platfrom Window Temp
You will be able to add New Platfroms to the database""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Menu_Window"))
        button.pack()

# Making the System window
class System_Window(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""System Window Temp
You will be able to add new system to the existing platfroms""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Menu_Window"))
        button.pack()


# Making the Game window
class Game_Window(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Game Window Temp
You will be able to add games to the existing system in existing platfroms
Yo will be able to scrap Images and Overviwes of games""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Menu_Window"))
        button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()