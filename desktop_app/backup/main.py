import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from desktop_app.funcs import main_manager


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
#---------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------
#--------------------------------- MAKING THE UI ---------------------------------------
#---------------------------------------------------------------------------------------

# SETTING UP THE MAIN MENU--------------------------------------------------
root = tk.Tk() # main menu root
# Setting the size of the launch window, this will be the minimum and maximum size too.
root.geometry("1024x768")
root.update_idletasks()

# Setting the minimum and maximum size of the window.
root.minsize(root.winfo_width(),root.winfo_height())
root.maxsize(root.winfo_width(),root.winfo_height())
# Setting the title of the app.
root.title("Handheld Database")
# Setting the icon of the app.
root.iconbitmap("./desktop_app/images/favicon.ico")

# Label tests
welcome = tk.Label(root, text="WELCOME!", font=('Arial', 32))
welcome.pack(pady=20)
lbl1 = tk.Label(root, text="""Attention, this app can only be used with scraping. 
Steamgrid APi key required.

Please select what you want to add to the database.""", font=('Arial', 32), anchor="center")
lbl1.pack(pady=10)

#------------------------------------------------------------------------------------------
# Importing images for the buttons
platform_Img = PhotoImage(file="./desktop_app/images/platform.png") # https://www.vecteezy.com/vector-art/3331132-hand-holding-portable-video-game-console-vector-icon
system_Img = PhotoImage(file="./desktop_app/images/system.png") # https://www.flaticon.com/free-icon/emulator_8560002
game_Img = PhotoImage(file="./desktop_app/images/game.png") # https://www.freepik.com/icon/game_12595961#fromView=keyword&page=1&position=3&uuid=b4f88723-ace5-456f-8a25-f54ac9151ca2

# Making a frame for the buttons.
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

# Add Plafrom button.
platform = tk.Button(buttonframe, image=platform_Img, command= lambda: main_manager.platform_Btn)
platform.grid(row=0, column=0,sticky=tk.W+tk.E, padx=20)
# Add Label under the button
platform_Lbl = tk.Label(buttonframe, text="PLATFORM", font=('Arial', 32))
platform_Lbl.grid(row=1, column=0)
# Add System button.
system = tk.Button(buttonframe, image=system_Img, command= main_manager.system_Btn)
system.grid(row=0, column=1,sticky=tk.W+tk.E, padx=20)
# Add Label under the button
system_Lbl = tk.Label(buttonframe, text="SYSTEM", font=('Arial', 32))
system_Lbl.grid(row=1, column=1)
# Add game button.
game = tk.Button(buttonframe, image=game_Img, command= main_manager.game_Btn)
game.grid(row=0, column=2, sticky=tk.W+tk.E, padx=20)
# Add Label under the button
game_Lbl = tk.Label(buttonframe, text="GAME", font=('Arial', 32))
game_Lbl.grid(row=1, column=2)
buttonframe.pack(pady=40)
#------------------------------------------------------------------------------------------



# Making the HELP button
help = tk.Button(root, text="HELP", font=('Arial', 12), command=help_Btn_Func)
help.place(x=960, y=720)

#---------------------- END OF MAIN MENU UI CODE -----------------------------------
#-----------------------------------------------------------------------------------
root.mainloop()