import tkinter as tk                
from tkinter import PhotoImage
from tkinter import messagebox


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