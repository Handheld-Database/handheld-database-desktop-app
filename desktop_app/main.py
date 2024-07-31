import tkinter as tk                
from tkinter import font as tkfont  
from tkinter import PhotoImage
from tkinter import messagebox


# Application to make contributing to the Handheld Database easier.
# WORK IN PROGRESS

# Base of the application
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
        for F in (Menu_Window, Platfrom_Window, System_Window, Game_Window, Game_W_Manual, Game_W_Automatic):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu_Window")

    # Change whitch window is shown by the page name.
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()  # Lifts the appropriate frame to the top, so it is shown.

# Main Menu window UI
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
        
        tk.Label(self, text="""ALPHA BUILD""", font=('Arial', 10, 'bold'), justify="center").pack(side="right")

        # Making the HELP button
        help = tk.Button(self, text="Help", font=('Arial', 10), command=self.help_Btn_Func) 
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

# Platfrom window UI
class Platfrom_Window(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Platfrom Window Temp
You will be able to add New Platfroms to the database""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",
                           command=lambda: controller.show_frame("Menu_Window"))
        button.pack(anchor = "s", side="left", padx=20, pady=12)

        # Making the HELP button
        help = tk.Button(self, text="Help", font=('Arial', 10), command=self.help_Btn_Func) 
        help.pack(anchor = "s", side="right", padx=20, pady=12)
        
    # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """HERE GOES THE HELP FOR THIS SECTION.
"""
        messagebox.showinfo("Platfrom Info", main_menu) 

# System window UI
class System_Window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""System Window Temp
You will be able to add new system to the existing platfroms""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",
                           command=lambda: controller.show_frame("Menu_Window"))
        button.pack(anchor = "s", side="left", padx=20, pady=12)

        # Making the HELP button
        help = tk.Button(self, text="Help", font=('Arial', 10), command=self.help_Btn_Func) 
        help.pack(anchor = "s", side="right", padx=20, pady=12)
        
    # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """HERE GOES THE HELP FOR THIS SECTION.
"""
        messagebox.showinfo("System Info", main_menu) 

# Main Game window UI
class Game_Window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Main Game Window Temp
You will be able to choose what mode you want to add games to the database.""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # Load images
        manual_game_Img = PhotoImage(file="./desktop_app/images/add.png")  # https://www.pngwing.com/en/free-png-xmbqc
        import_game_Img = PhotoImage(file="./desktop_app/images/import.png")  # https://www.pngwing.com/en/free-png-yxgyl

        # Making a frame for the buttons.
        buttonframe = tk.Frame(self)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)

        # Add Manual Game contribution button
        manual_game = tk.Button(buttonframe, text="Add Game", image=manual_game_Img, command=lambda: controller.show_frame("Game_W_Manual"))  
        manual_game.img = manual_game_Img
        manual_game.grid(row=0, column=0,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        manual_game_Lbl = tk.Label(buttonframe, text="Add Game", font=('Arial', 32))
        manual_game_Lbl.grid(row=1, column=0)

        # Add Automatic Game contribution button, import from .CSV files
        import_game = tk.Button(buttonframe, text="Import Game(s)", image=import_game_Img, command=lambda: controller.show_frame("Game_W_Automatic"))  
        import_game.img = import_game_Img
        import_game.grid(row=0, column=1,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        import_game_Lbl = tk.Label(buttonframe, text="Import Game(s)", font=('Arial', 32))
        import_game_Lbl.grid(row=1, column=1)
        buttonframe.pack(pady=20)

        button = tk.Button(self, text="Go Back", font=('Arial', 10),
                           command=lambda: controller.show_frame("Menu_Window"))
        button.pack(anchor = "s", side="left", padx=20, pady=12)

        # Making the HELP button
        help = tk.Button(self, text="HELP", font=('Arial', 10), command=self.help_Btn_Func) 
        help.pack(anchor = "s", side="right", padx=20, pady=12)
        

    # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """HERE GOES THE HELP FOR THIS SECTION.
"""
        messagebox.showinfo("Game Main Menu Info", main_menu) 

# Manual Game window UI
class Game_W_Manual(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Manual Game Window Temp
You will be able to add games to the database manually.""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
#-------------------------------------------------------------------------------------

# -------- HERE GOES THE UI

#-------------------------------------------------------------------------------------
        button = tk.Button(self, text="Go Back",
                           command=lambda: controller.show_frame("Game_Window"))
        button.pack(anchor = "s", side="left", padx=20, pady=12)

        # Making the HELP button
        help = tk.Button(self, text="HELP", font=('Arial', 10), command=self.help_Btn_Func) 
        help.pack(anchor = "s", side="right", padx=20, pady=12)
        
    # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """HERE GOES THE HELP FOR THIS SECTION.
"""
        messagebox.showinfo("Game Manual Menu Info", main_menu) 
       
# Automatic Game window UI
class Game_W_Automatic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Import Game Window Temp
You will be able to import games from .CSV files.""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
#-------------------------------------------------------------------------------------

# -------- HERE GOES THE UI

#-------------------------------------------------------------------------------------
        button = tk.Button(self, text="Go Back",
                           command=lambda: controller.show_frame("Game_Window"))
        button.pack(anchor = "s", side="left", padx=20, pady=12)
        
        # Making the HELP button
        help = tk.Button(self, text="HELP", font=('Arial', 10), command=self.help_Btn_Func) 
        help.pack(anchor = "s", side="right", padx=20, pady=12)
        

    # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """HERE GOES THE HELP FOR THIS SECTION.
"""
        messagebox.showinfo("Game Automatic Menu Info", main_menu) 




if __name__ == "__main__":
    app = App()
    app.mainloop()