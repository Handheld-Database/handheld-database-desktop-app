import tkinter as tk                
from tkinter import messagebox
try:
        from UI.Manager import App_Manager
except ImportError:
        print(" Platfrom_Window.py - Coudn't import App_Manager!")

class Platfrom_Window(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="""Add a non existent platfrom to the database.
""",font=('Arial', 22)) # , font=styles.title_Font
            label.pack(side="top",padx=5, fill="x")
            button = tk.Button(self, text="Go Back",
                            command=lambda: controller.show_frame("Menu_Window"))
            button.pack(anchor = "s", side="left", padx=20, pady=12)

            # --------------------------------------------------------------------------------------
            # Container for the inputs which are necessary to add a new platform to the database.
            # --------------------------------------------------------------------------------------
            button_frame = tk.Frame(self)
            button_frame.columnconfigure(0, weight=1)
            button_frame.columnconfigure(1, weight=1)

            #steamgrid_api_entry_lbl = tk.Label(button_frame, text = "STEAMGRID API KEY: ", font=('Arial', 18)).grid(row=0, column=0, sticky='e')
            steamgrid_api_entry = tk.Entry(button_frame, width=60,font=('Arial', 11), justify="center")
            self.steamgrid_api_text = tk.StringVar()
            self.steamgrid_api_text.set("PASTE YOUR STEAMGRID API KEY HERE")
            steamgrid_api_entry.config(textvariable = self.steamgrid_api_text, width=60)
            #steamgrid_api_entry.grid(row=0, column=1)  This isn't shown because the script doesn't scrape picture for the devices yet.

            name_lbl = tk.Label(button_frame, text = "Device's name: ", font=('Arial', 20)).grid(row=1, column=0, sticky='e')
            self.name_text = tk.StringVar()
            name_entry = tk.Entry(button_frame, textvariable=self.name_text, width=60,font=('Arial', 11)).grid(row=1, column=1)
            
            database_key_entry_lbl = tk.Label(button_frame, text = "Database Key: ", font=('Arial', 18)).grid(row=2, column=0, sticky='e')
            self.database_key_text = tk.StringVar()
            database_key_entry = tk.Entry(button_frame, textvariable=self.database_key_text, width=60,font=('Arial', 11)).grid(row=2, column=1)

            manufacturer_entry_lbl = tk.Label(button_frame, text = "Manufacturer: ", font=('Arial', 18)).grid(row=3, column=0,sticky='e')
            self.manufacturer_entry_text = tk.StringVar()
            manufacturer_entry = tk.Entry(button_frame, textvariable=self.manufacturer_entry_text, width=60,font=('Arial', 11)).grid(row=3, column=1)

            screen_size_entry_lbl = tk.Label(button_frame, text = "Screen Size: ", font=('Arial', 18)).grid(row=4, column=0, sticky='e')
            self.screen_size_text = tk.StringVar()
            screen_size_entry = tk.Entry(button_frame, textvariable=self.screen_size_text, width=60,font=('Arial', 11)).grid(row=4, column=1)

            resolution_entry_lbl = tk.Label(button_frame, text = "Resolution: ", font=('Arial', 18)).grid(row=5, column=0, sticky='e')
            self.resolution_text = tk.StringVar()
            resolution_entry = tk.Entry(button_frame, textvariable=self.resolution_text, width=60,font=('Arial', 11)).grid(row=5, column=1)

            battery_life_entry_lbl = tk.Label(button_frame, text = "Battery Life: ", font=('Arial', 18)).grid(row=6, column=0, sticky='e')
            self.battery_life_text = tk.StringVar()
            battery_life_entry = tk.Entry(button_frame, textvariable=self.battery_life_text, width=60,font=('Arial', 11)).grid(row=6, column=1)

            weight_entry_lbl = tk.Label(button_frame, text = "Weight: ", font=('Arial', 18)).grid(row=7, column=0, sticky='e')
            self.weight_text =tk.StringVar()
            weight_entry = tk.Entry(button_frame, textvariable=self.weight_text, width=60,font=('Arial', 11)).grid(row=7, column=1)

            system_entry_lbl = tk.Label(button_frame, text = "System:", font=('Arial', 18)).grid(row=8, column=0, sticky='e')
            self.system_text = tk.StringVar()
            system_entry = tk.Entry(button_frame, textvariable=self.system_text, width=60,font=('Arial', 11)).grid(row=8, column=1)
            
            cpu_entry_lbl = tk.Label(button_frame, text = "CPU: ", font=('Arial', 18)).grid(row=9, column=0, sticky='e')
            self.cpu_text = tk.StringVar()
            cpu_entry = tk.Entry(button_frame, textvariable=self.cpu_text, width=60,font=('Arial', 11)).grid(row=9, column=1)

            gpu_entry_lbl = tk.Label(button_frame, text = "GPU: ", font=('Arial', 18)).grid(row=10, column=0, sticky='e')
            self.gpu_text = tk.StringVar()
            gpu_entry= tk.Entry(button_frame, textvariable=self.gpu_text, width=60,font=('Arial', 11)).grid(row=10, column=1)

            ram_entry_lbl = tk.Label(button_frame, text = "RAM: ", font=('Arial', 18)).grid(row=11, column=0, sticky='e')
            self.ram_text = tk.StringVar()
            ram_entry = tk.Entry(button_frame, textvariable=self.ram_text, width=60,font=('Arial', 11)).grid(row=11, column=1)

            arch_entry_lbl = tk.Label(button_frame, text = "Arch: ", font=('Arial', 18)).grid(row=12, column=0, sticky='e')
            self.arch_text = tk.StringVar()
            arch_entry = tk.Entry(button_frame, textvariable=self.arch_text, width=60,font=('Arial', 11)).grid(row=12, column=1)

            storage_entry_lbl = tk.Label(button_frame, text = "Storage: ", font=('Arial', 18)).grid(row=13, column=0, sticky='e')
            self.storage_text = tk.StringVar()
            storage_entry = tk.Entry(button_frame, textvariable=self.storage_text, width=60,font=('Arial', 11)).grid(row=13, column=1)

            media_entry_lbl = tk.Label(button_frame, text = "Media: ", font=('Arial', 18)).grid(row=14, column=0, sticky='e')
            self.media_text = tk.StringVar()
            media_entry = tk.Entry(button_frame, textvariable=self.media_text, width=60,font=('Arial', 11)).grid(row=14, column=1)

            connectivity_entry_lbl = tk.Label(button_frame, text = "Connectivity (separate with ';'): ", font=('Arial', 18) ).grid(row=15, column=0, sticky='e')
            self.connectivity_text = tk.StringVar()
            connectivity_entry = tk.Entry(button_frame, textvariable=self.connectivity_text, width=60,font=('Arial', 11)).grid(row=15, column=1)

            add_button = tk.Button(button_frame, text="ADD", font=('Arial', 16), command=lambda: self.Check_Inputs()).grid(row=16, column=1)
            clear_button = tk.Button(button_frame, text = "CLEAR", font=('Arial', 16), 
            command=self.Clear_Input_Fields).grid(row=16, column=0, sticky='e')

            button_frame.pack(side="left")
             # --------------------------------------------------------------------------------------
            
            # Making the HELP button
            help = tk.Button(self, text="Help", font=('Arial', 10), command=self.Help_Btn_Func) 
            help.pack(anchor = "s", side="right", padx=10, pady=12)

            
        # Defining the HELP button's function
    def Help_Btn_Func(self):
        main_menu = """
Adding Proccess:
1. - Fill out the entries for the device you want to add to the database.
2. - Press the ADD button, which will add the device to the database based on the provided data.

Clear button: clears out the all the data entries, except the API key.
"""
        messagebox.showinfo("Platfrom Info", main_menu) 

    def Clear_Input_Fields(self):
          self.name_text.set("")
          self.database_key_text.set("")
          self.manufacturer_entry_text.set("")
          self.screen_size_text.set("")
          self.resolution_text.set("")
          self.battery_life_text.set("")
          self.weight_text.set("")
          self.system_text.set("")
          self.cpu_text.set("")
          self.gpu_text.set("")
          self.ram_text.set("")
          self.arch_text.set("")
          self.storage_text.set("")
          self.media_text.set("")
          self.connectivity_text.set("")

    def New_Platfrom_Added_Notification(self):
        add_message = """New platfrom was added.
"""
        messagebox.showinfo("Platfrom Message", add_message) 

    def Check_Inputs(self):
        error_message = """Fill out all the fields!
"""

        if self.steamgrid_api_text.get() == "" or self.steamgrid_api_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.name_text.get() == "" or self.name_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.database_key_text.get() == "" or self.database_key_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.manufacturer_entry_text.get() == "" or self.manufacturer_entry_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.screen_size_text.get() == "" or self.screen_size_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.resolution_text.get() == "" or self.resolution_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.battery_life_text.get() == "" or self.battery_life_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.weight_text.get() == "" or self.weight_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.system_text.get() == "" or self.system_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.cpu_text.get() == "" or self.cpu_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.gpu_text.get() == "" or self.gpu_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.ram_text.get() == "" or self.ram_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.arch_text.get() == "" or self.arch_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.storage_text.get() == "" or self.storage_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.media_text.get() == "" or self.media_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.connectivity_text.get() == "" or self.connectivity_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        else:
               App_Manager.New_Platfrom(
                  self.steamgrid_api_text.get(),
                  self.name_text.get(),
                  self.database_key_text.get(),
                  self.manufacturer_entry_text.get(),
                  self.screen_size_text.get(),
                  self.resolution_text.get(),
                  self.battery_life_text.get(),
                  self.weight_text.get(),
                  self.system_text.get(),
                  self.cpu_text.get(),
                  self.gpu_text.get(),
                  self.ram_text.get(),
                  self.arch_text.get(),
                  self.storage_text.get(),
                  self.media_text.get(),
                  self.connectivity_text.get())
               self.New_Platfrom_Added_Notification()
               self.Clear_Input_Fields()