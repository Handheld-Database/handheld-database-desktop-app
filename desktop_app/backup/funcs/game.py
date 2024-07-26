import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import filedialog

selected_directory = "Directory Path."
    #---------------------------------------------------------------------------------------
    #--------------------------------- MAKING THE FUNCTIONS --------------------------------
    #---------------------------------------------------------------------------------------
    # Defining the HELP button's function
def help_Btn_Func():
    main_menu = """In this section you can chose what you want to add to the database.
    -Click the "PLATFORM" button to add a new platfrom. (For example: R36S, TSP)
    -Click the "SYSTEM" button to add a new system to a platform. (For example: PSP, GBA)
    -Click the "GAME" button to add a new game to a system.
        """
    messagebox.showinfo("showinfo", main_menu) 

    # Sets the folder to directory and dispalys it, and returns the current path to it.
def set_directory_path():
    selected_directory= filedialog.askdirectory()
    #text.config(text=selected_directory)

def update_directory():
    return selected_directory

    #---------------------------------------------------------------------------------------




    #---------------------------------------------------------------------------------------
    #--------------------------------- MAKING THE UI ---------------------------------------
    #---------------------------------------------------------------------------------------
def Game_Window():
    root_game = tk.Toplevel()
    root_game.geometry("1024x768")
    root_game.update_idletasks()

        # Setting the minimum and maximum size of the window.
    root_game.minsize(root_game.winfo_width(),root_game.winfo_height())
    root_game.maxsize(root_game.winfo_width(),root_game.winfo_height())
        # Setting the title of the app.
    root_game.title("Handheld Database")
        # Setting the icon of the app.
    root_game.iconbitmap("./desktop_app/images/favicon.ico")

        # Label tests
    platform_title = tk.Label(root_game, text="New Game", font=('Arial', 28))
    platform_title.pack(pady=10)


        # MAKE THE UI FOR THE NEW GAME,
    browse = tk.Button(root_game, text="BROWSE", font=('Arial', 12), command=set_directory_path)
    browse.place(x=10, y=720)

        # Label to display the path to the directory.
    text= tk.Label(root_game, text= update_directory, font=('Arial', 12),borderwidth=1, relief="solid")
    text.place(x=100, y=725)