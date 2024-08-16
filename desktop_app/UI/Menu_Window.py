import tkinter as tk                
from tkinter import PhotoImage
from tkinter import messagebox
try:
        from UI.Manager import App_Manager
except ImportError:
        print("Menu_Window.py - Coudn't import App_Manager!")


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
        platform_Img = PhotoImage(file="./desktop_app/materials/platform.png") # https://www.vecteezy.com/vector-art/3331132-hand-holding-portable-video-game-console-vector-icon
        system_Img = PhotoImage(file="./desktop_app/materials/system.png") # https://www.flaticon.com/free-icon/emulator_8560002
        game_Img = PhotoImage(file="./desktop_app/materials/game.png") # https://www.freepik.com/icon/game_12595961#fromView=keyword&page=1&position=3&uuid=b4f88723-ace5-456f-8a25-f54ac9151ca2

        # Making a frame for the buttons.
        buttonframe = tk.Frame(self)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)

        # Add Plafrom button.
        platform = tk.Button(buttonframe, image=platform_Img, command=lambda: self.path_check("Platfrom_Window"))  
        platform.img = platform_Img
        platform.grid(row=0, column=0,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        platform_Lbl = tk.Label(buttonframe, text="PLATFORM", font=('Arial', 32))
        platform_Lbl.grid(row=1, column=0)
        # Add System button.
        system = tk.Button(buttonframe, image=system_Img, command=lambda: self.path_check("System_Window"))  
        system.img = system_Img
        system.grid(row=0, column=1,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        system_Lbl = tk.Label(buttonframe, text="SYSTEM", font=('Arial', 32))
        system_Lbl.grid(row=1, column=1)
        # Add game button.
        game = tk.Button(buttonframe, image=game_Img, command=lambda: self.path_check("Game_Window"))
        game.img = game_Img
        game.grid(row=0, column=2, sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        game_Lbl = tk.Label(buttonframe, text="GAME", font=('Arial', 32))
        game_Lbl.grid(row=1, column=2)
        buttonframe.pack(pady=20)
        #------------------------------------------------------------------------------------------

        tk.Label(self, text="""ALPHA BUILD
For the Handheld-Database
Made by meeeaCH""", font=('Arial', 14), justify="center").pack()
        
        # Button for browsing and choosing a directory.
        path_button = tk.Button(self, text="BROWSE", command=self.set_Directory_Path)
        path_button.pack(side="left", pady=10)

        # A Label to show the choosen directory.
        path_lable = tk.Entry(self, font=('Arial', 10, 'bold'), justify="center")
        self.default_text = tk.StringVar()
        self.default_text.set("PATH TO THE DIRECTORY")
        path_lable.config(state = "disabled", textvariable = self.default_text, width=120)
        path_lable.pack(side="left", padx=5, pady=10)

        

        # Making the HELP button.
        help = tk.Button(self, text="HELP", command=self.help_Btn_Func) 
        help.pack(side="right", padx=10, pady=10)
        self.pack()

# Sets the directory of the database and shows it in the entry
    def set_Directory_Path(self):
        self.default_text.set(App_Manager.set_directory())
        # For testing ---
        App_Manager.list_platforms()
        App_Manager.list_systems_in_platfroms("tsp")
        # ------

    def path_check(self, page):
        message = """Set the PATH to the Database directory."""
        if(App_Manager.database_root_path[0] == None):
                messagebox.showwarning("Main Menu Info", message)
        else:
              self.controller.show_frame(page)
              
        
              

    # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """In this section you can chose what you want to add to the database.
-Click the "PLATFORM" button to add a new platfrom. (For example: R36S, TSP)
-Click the "SYSTEM" button to add a new system to a platform. (For example: PSP, GBA)
-Click the "GAME" button to add a new game to a system.
"""
        messagebox.showinfo("Main Menu Info", main_menu)

 