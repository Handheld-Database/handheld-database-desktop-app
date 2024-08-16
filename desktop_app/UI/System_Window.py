import tkinter as tk                
from tkinter import messagebox
from tkinter import scrolledtext 

try:
        from UI.Manager import App_Manager
except ImportError:
        print(" System_Window.py - Coudn't import App_Manager!")

class System_Window(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="""Add a new System to an existing Platfrom.""",font=('Arial', 18)) # , font=styles.title_Font
            label.pack(side="top", fill="x", pady=30)
            button = tk.Button(self, text="Go Back",
                            command=lambda: controller.show_frame("Menu_Window"))
            button.pack(anchor = "s", side="left", padx=20, pady=12)

            # Making the HELP button
            help = tk.Button(self, text="Help", font=('Arial', 10), command=self.help_Btn_Func) 
            help.pack(anchor = "s", side="right", padx=10, pady=12)

            # Frame for containing entries and labels for new system
            button_frame = tk.Frame(self)
            button_frame.columnconfigure(0, weight=1)
            button_frame.columnconfigure(1, weight=1)

            steamgrid_api_entry_lbl = tk.Label(button_frame, text = "STEAMGRID API KEY: ", font=('Arial', 14)).grid(row=0, column=0, sticky='e')
            steamgrid_api_entry = tk.Entry(button_frame, width=40,font=('Arial', 11), justify="center")
            self.default_text = tk.StringVar()
            self.default_text.set("PASTE YOUR STEAMGRID API KEY HERE")
            steamgrid_api_entry.config(textvariable = self.default_text, width=40)
            steamgrid_api_entry.grid(row=0, column=1)

            platfrom_name_lbl = tk.Label(button_frame, text = "Platfrom name: ", font=('Arial', 14)).grid(row=1, column=0, sticky='e')
            self.paltfrom_name_text = tk.StringVar()
            platfrom_name_entry = tk.Entry(button_frame, textvariable=self.paltfrom_name_text, width=40,font=('Arial', 11)).grid(row=1, column=1)

            system_name_lbl = tk.Label(button_frame, text = "System name: ", font=('Arial', 14)).grid(row=2, column=0, sticky='e')
            self.system_name_text = tk.StringVar()
            system_name_entry = tk.Entry(button_frame, textvariable=self.system_name_text, width=40,font=('Arial', 11)).grid(row=2, column=1)

            placeholder = tk.Label(button_frame).grid(row=3, column=0)

            add_button = tk.Button(button_frame, text="ADD", font=('Arial', 14), command=lambda: [App_Manager.New_Platfrom(), self.new_system_added_notification(), self.clear_input_fields()]).grid(row=4, column=1)
            clear_button = tk.Button(button_frame, text = "CLEAR", font=('Arial', 14), 
            command=self.clear_input_fields).grid(row=4, column=0, sticky='e')

            button_frame.pack(side="left" ,padx=10)
            # -----------------------------------------------------------------------------------


            # Displays the existing platfroms and systems
            platfromAndSystems_Label = tk.Label(self, text="Systems List: ", font=('Arial', 18)).pack()  
            self.display_info_text = tk.StringVar()

            #display_info = tk.Text(self, text=self.display_info_text, state='disabled', font=('Arial', 12)).pack()

            #display_info = scrolledtext.ScrolledText(self, state ='disabled',wrap = tk.WORD,  width = 40,   height = 30,  font = ('Arial', 12)) 
            #display_info.insert(tk.INSERT, self.display_info_text)
            #display_info.pack()

            get_info = tk.Button(self, text = "GET", font=('Arial', 14), command=lambda: self.get_systems()).pack()
             # -----------------------------------------------------------------------------------


            
            
        # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """HERE GOES THE HELP FOR THIS SECTION.
"""
        messagebox.showinfo("System Info", main_menu) 


    def clear_input_fields(self):
        self.paltfrom_name_text.set("")
        self.system_name_text.set("")
       

    def new_system_added_notification(self):
        add_message = """New system was added.
"""
        messagebox.showinfo("System Message", add_message) 


    def get_systems(self):
        platfroms = [None]
        systems = [None]
        platfroms = App_Manager.list_platforms()

        
        text_to_display="""test:
gharegr
erger
ergerg
ergerg
ergerge
gergeg
"""
        self.display_info_text.set(text_to_display)
        print("rReeeee")
      
