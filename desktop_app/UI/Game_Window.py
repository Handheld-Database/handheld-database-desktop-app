import tkinter as tk                  
from tkinter import PhotoImage
from tkinter import messagebox


class Game_Window(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="""Main Game Window Temp
You will be able to choose what mode you want to add games to the database.""", font=('Arial', 18)) 
            label.pack(side="top", fill="x", pady=10)

            # Load images
            manual_game_Img = PhotoImage(file="./desktop_app/materials/add.png")  # https://www.pngwing.com/en/free-png-xmbqc
            import_game_Img = PhotoImage(file="./desktop_app/materials/import.png")  # https://www.pngwing.com/en/free-png-yxgyl

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