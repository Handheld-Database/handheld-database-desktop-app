import tkinter as tk
import tkinter as ttk
from tkinter import PhotoImage
from tkinter import messagebox


class Platfrom_Window(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self,text="PALTFROM").pack(padx=10, pady=10)
        self.pack(padx=10, pady=10)

class System_Window(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self,text="SYSTEM").pack(padx=10, pady=10)
        self.pack(padx=10, pady=10)

class Game_Window(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self,text="GAME").pack(padx=10, pady=10)
        self.pack(padx=10, pady=10)


class Menu_Window(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        title = tk.Label(self, text="WELCOME!", font=('Arial', 32))
        title.pack(pady=20)

        lbl1 = tk.Label(self, text="""This application is for contributing to the Handheld Database.
Please select what you want to add to the database.""", font=('Arial', 28), anchor="center")
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
        platform = tk.Button(buttonframe, image=platform_Img)  # , command= lambda: main_manager.platform_Btn
        platform.img = platform_Img
        platform.grid(row=0, column=0,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        platform_Lbl = tk.Label(buttonframe, text="PLATFORM", font=('Arial', 32))
        platform_Lbl.grid(row=1, column=0)
        # Add System button.
        system = tk.Button(buttonframe, image=system_Img)  # , command= main_manager.system_Btn
        system.img = system_Img
        system.grid(row=0, column=1,sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        system_Lbl = tk.Label(buttonframe, text="SYSTEM", font=('Arial', 32))
        system_Lbl.grid(row=1, column=1)
        # Add game button.
        game = tk.Button(buttonframe, image=game_Img , command= main.open_Game_Window)  
        game.img = game_Img
        game.grid(row=0, column=2, sticky=tk.W+tk.E, padx=20)
        # Add Label under the button
        game_Lbl = tk.Label(buttonframe, text="GAME", font=('Arial', 32))
        game_Lbl.grid(row=1, column=2)
        buttonframe.pack(pady=40)
        #------------------------------------------------------------------------------------------

        ttk.Label(self, text="""For the Handheld-Database
Made by meeeaCH""", font=('Arial', 18), justify="center").pack()

        # Making the HELP button
        help = tk.Button(self, text="HELP", font=('Arial', 12), command=self.help_Btn_Func)
        help.pack(side="right", padx=20, pady=20)
        self.pack()


          # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """In this section you can chose what you want to add to the database.
-Click the "PLATFORM" button to add a new platfrom. (For example: R36S, TSP)
-Click the "SYSTEM" button to add a new system to a platform. (For example: PSP, GBA)
-Click the "GAME" button to add a new game to a system.
"""
        messagebox.showinfo("Main Menu Info", main_menu) 



class Main_Window(tk.Frame):
    def __init__(self, master):
        mainframe = tk.Frame(master)
        mainframe.pack()
    
        self.index = 0

        self.frameList = [Menu_Window(mainframe), Platfrom_Window(mainframe), System_Window(mainframe), Game_Window(mainframe)]
        self.frameList[1].forget()
        self.frameList[2].forget()
        self.frameList[3].forget()

       

    def open_Game_Window(self):
        self.frameList[0].forget()
        self.frameList[1].forget()
        self.frameList[2].tkraise()
        self.frameList[2].pack()

    def changeWindow(self):
        self.frameList[self.index].forget()
        self.index = (self.index + 1) % len(self.frameList)
        self.frameList[self.index].tkraise()
        self.frameList[self.index].pack(padx=10, pady=10)

  


# Setup the window's properties.
root = tk.Tk()
root.geometry("1024x768")
# Setting the minimum size of the window.
root.minsize(1024,768)
root.maxsize(1024,768)
# Setting the title of the app.
root.title("Handheld Database")
# Setting the icon of the app.
root.iconbitmap("./desktop_app/images/favicon.ico")


window = Main_Window(root)
root.mainloop()