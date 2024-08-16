import tkinter as tk                 
from tkinter import messagebox
try:
        from UI.Manager import App_Manager
except ImportError:
        print(" Game_W_Manual.py - Coudn't import App_Manager!")

platfroms = [None]
systems = [None]

class Game_W_Manual(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                self.controller = controller
                label = tk.Label(self, text="""Manual Game Window Temp
You will be able to add games to the database manually.""",font=('Arial', 18)) # , font=styles.title_Font
                label.pack(side="top", fill="x", pady=10)
        #-------------------------------------------------------------------------------------  Adding a game procces: tsp nds "Dragon Ball Kai Ultimate Butouden" --tester meeeaCH --steamgrid-key yourID
                # Test ------------
                selected_platform = tk.StringVar()
                if (selected_platform == None):
                        selected_platform = "Select an option"

                platfrom_dropdown = tk.OptionMenu(self, selected_platform, "Select an option")
                platfrom_dropdown.pack(pady=10)

                # Populate the dropdown menu with the list of platfroms
                for option in App_Manager.scaned_platfroms:
                        platfrom_dropdown["menu"].add_command(label=option, command=lambda opt=option: selected_platform.set(opt))
                
                # Add a button to print the selected option for testing
                button = tk.Button(self, text="Show Selection", command=lambda : App_Manager.print_out_things(selected_platform.get()))
                button.pack()

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

        def update_dropdown(self):
                self.platfrom_dropdown.configure(self, *App_Manager.list_platforms())