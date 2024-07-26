import tkinter as tk
import tkinter as ttk
from tkinter import PhotoImage
from tkinter import messagebox

menu_switcher = 1

class App(tk.Tk):
    def __init__(self, title, size, iconmap):
        # Main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        self.maxsize(size[0],size[1])
        self.iconbitmap(iconmap)

        # Widgets
        #self.menu = Menu(self)
        #self.game = Game(self)

        match menu_switcher:
            case 0:
                self.game = Game(self)
            case _:
                self.menu = Menu(self)


        # Run
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self, text="WELCOME!", font=('Arial', 32))
        title.pack(pady=20)
        lbl1 = ttk.Label(self, text="""This application is for contributing to the Handheld Database.
Please select what you want to add to the database.""", font=('Arial', 28), anchor="center")
        lbl1.pack(pady=10)
        
        #------------------------------------------------------------------------------------------
        # Importing images for the buttons
        platform_Img = ttk.PhotoImage(file="./desktop_app/images/platform.png") # https://www.vecteezy.com/vector-art/3331132-hand-holding-portable-video-game-console-vector-icon
        system_Img = PhotoImage(file="./desktop_app/images/system.png") # https://www.flaticon.com/free-icon/emulator_8560002
        game_Img = ttk.PhotoImage(file="./desktop_app/images/game.png") # https://www.freepik.com/icon/game_12595961#fromView=keyword&page=1&position=3&uuid=b4f88723-ace5-456f-8a25-f54ac9151ca2
        #----------------------------------------------------------------------------
        # Making a frame for the buttons.
        buttonframe = ttk.Frame(self)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        #----------------------------------------------------------------------------
        # Add Plafrom button.
        platform = tk.Button(buttonframe, image=platform_Img, command=say)
        platform.img = platform_Img
        platform.grid(row=0, column=0,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        platform_Lbl = ttk.Label(buttonframe, text="PLATFORM", font=('Arial', 32))
        platform_Lbl.grid(row=1, column=0)
        #----------------------------------------------------------------------------
        # Add System button.
        system = ttk.Button(buttonframe, image=system_Img, command=say)
        system.img = system_Img
        system.grid(row=0, column=1,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        system_Lbl = ttk.Label(buttonframe, text="SYSTEM", font=('Arial', 32))
        system_Lbl.grid(row=1, column=1)
        #----------------------------------------------------------------------------
        # Add game button.
        game = ttk.Button(buttonframe, image=game_Img, command=switch_to_game)
        game.img = game_Img
        game.grid(row=0, column=2, sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        game_Lbl = ttk.Label(buttonframe, text="GAME", font=('Arial', 32))
        game_Lbl.grid(row=1, column=2)

        buttonframe.pack(pady=40)
        #------------------------------------------------------------------------------------------
       

        ttk.Label(self, text="""For the Handheld-Database
Made by meeeaCH""", font=('Arial', 18), justify="center").pack()
        
        # Making the HELP button
        help = tk.Button(self, text="HELP", font=('Arial', 12), command=help_Btn_Func)
        help.pack(side="right", padx=20, pady=20)


        self.place(x=0, y=0)

class Game(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        title = ttk.Label(self, text="New Game", font=('Arial', 32))
        title.pack(pady=20)

        self.place(x=0, y=0)


    

# ------------------------  FUNCTIONS  --------------------------------
def say():
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

def switch_to_game():
    menu_switcher = 0
    print(menu_switcher)

# Defining the HELP button's function
def help_Btn_Func():
    main_menu = """In this section you can chose what you want to add to the database.
-Click the "PLATFORM" button to add a new platfrom. (For example: R36S, TSP)
-Click the "SYSTEM" button to add a new system to a platform. (For example: PSP, GBA)
-Click the "GAME" button to add a new game to a system.
    """
    messagebox.showinfo("showinfo", main_menu) 

# ------------------------- END OF FUNCTIONS ---------------------------

App('HANDHELD DATABASE', (1024,768), "./desktop_app/images/favicon.ico")