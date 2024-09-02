import tkinter as tk       
from tkinter import ttk         
from tkinter import messagebox

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
        help = tk.Button(self, text="Help", font=('Arial', 10), command=self.Help_Btn_Func) 
        help.pack(anchor = "s", side="right", padx=10, pady=12)

        # Frame for containing entries and labels for new system
        button_frame = tk.Frame(self)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        steamgrid_api_entry_lbl = tk.Label(button_frame, text = "STEAMGRID API KEY: ", font=('Arial', 14)).grid(row=0, column=0, sticky='e')
        steamgrid_api_entry = tk.Entry(button_frame, width=40,font=('Arial', 11), justify="center")
        self.steamgrid_api_entry_text = tk.StringVar()
        self.steamgrid_api_entry_text.set("PASTE YOUR STEAMGRID API KEY HERE")
        steamgrid_api_entry.config(textvariable = self.steamgrid_api_entry_text, width=40)
        steamgrid_api_entry.grid(row=0, column=1)

        platfrom_name_lbl = tk.Label(button_frame, text = "Platfrom Key: ", font=('Arial', 14)).grid(row=1, column=0, sticky='e')
        self.paltfrom_name_text = tk.StringVar()
        platfrom_name_entry = tk.Entry(button_frame, textvariable=self.paltfrom_name_text, width=40,font=('Arial', 11)).grid(row=1, column=1)

        full_system_name_lbl = tk.Label(button_frame, text = "Full System Name: ", font=('Arial', 14)).grid(row=2, column=0, sticky='e')
        self.full_system_name_text = tk.StringVar()
        full_system_name_entry = tk.Entry(button_frame, textvariable=self.full_system_name_text, width=40,font=('Arial', 11)).grid(row=2, column=1)

        system_name_lbl = tk.Label(button_frame, text = "System Key: ", font=('Arial', 14)).grid(row=3, column=0, sticky='e')
        self.system_key_text = tk.StringVar()
        system_name_entry = tk.Entry(button_frame, textvariable=self.system_key_text, width=40,font=('Arial', 11)).grid(row=3, column=1)

        placeholder = tk.Label(button_frame).grid(row=4, column=0)

        add_button = tk.Button(button_frame, text="ADD", font=('Arial', 14), command=lambda: self.Check_Inputs()
                ).grid(row=5, column=1)
        
        clear_button = tk.Button(button_frame, text = "CLEAR", font=('Arial', 14), 
        command=self.Clear_Input_Fields).grid(row=5, column=0, sticky='e')

        button_frame.pack(side="bottom", pady=40)
         # -----------------------------------------------------------------------------------


        # Displays the existing platfroms and systems
        display_frame = tk.Frame(self)
        display_frame.columnconfigure(0, weight=700)
       
        platfromAndSystems_Label = tk.Label(display_frame, text="Systems List:", font=('Arial', 18)).grid(row=0, column=0)
        self.treev = ttk.Treeview(display_frame, selectmode = "none")
        self.treev.grid(row=1, column=0)

        # Scrollbar 
        horscrlbar = ttk.Scrollbar(display_frame,  
                        orient ="horizontal",  
                        command = self.treev.xview) 
        horscrlbar.grid(row=2, column=0, sticky="nsew")
        verscrlbar = ttk.Scrollbar(display_frame,  
                        orient ="vertical",  
                        command = self.treev.yview) 
        verscrlbar.grid(row=1, column=1, sticky="nsew")

        
        # Configuring treeview 
        self.treev.configure(xscrollcommand = horscrlbar.set, yscrollcommand=verscrlbar.set) 
        
        # Table heading style
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#3b65b9", foreground="white")
        
        tk.Label(display_frame).grid(row=3, column=0)
        get_info = tk.Button(display_frame, text = "GET", font=('Arial', 14), command=lambda: self.Get_Systems()).grid(row=4, column=0)

        display_frame.pack(side="top")
        # -----------------------------------------------------------------------------------


# Fill the table with the existing systems in each platfroms
    def Get_Systems(self):
        number_of_columns = []
        data = []
        systems_lenght = 0
        headings = App_Manager.List_Platforms()  # The Name of the platforms
        number_of_platfroms = len(headings)  # number of columns based on the number of platfroms
        number_of_systems = 0 # number of systems based on the systems in each platform

        # Deletes every row in the table
        for row in self.treev.get_children():
                self.treev.delete(row)

        # Gets the maximum number of systems
        for i in range(number_of_platfroms):
             system_helper = len(App_Manager.Read_Systems_In(headings[i]))
             if system_helper > number_of_systems:
                  number_of_systems = system_helper
        

        # Counts the number of columns, (1, 2, 3, 4, 5)
        for i in range(number_of_systems):
             number_of_columns.append(i+1)

        # Defining number of columns, (1, 2, 3, 4, 5)
        self.treev["columns"] = (number_of_columns) 
        # Defining heading 
        self.treev['show'] = 'headings'
                
        # Make the table headings with tha biggest number of systems
        for i in range(number_of_systems):
             if i==0:
                self.treev.column(1, width = 100, stretch=False) 
                self.treev.heading(1, text = "Platfrom Key")
             else:
                self.treev.column(i+1, width = 70, stretch=False) 
                self.treev.heading(i+1, text = "System")

        # Fill the table with data
        for i in range(number_of_platfroms):
             systems = App_Manager.Read_Systems_In(headings[i])
             systems_lenght = len(systems)
        
             data.append(headings[i])
             for j in range(systems_lenght):
                data.append(systems[j]['key'])
        
             self.treev.insert("","end", values=data)
             data=[]

# Defining the HELP button's function
    def Help_Btn_Func(self):
        main_menu = """
- "GET" button lists the existing systems in each platfrom.
- "ADD" button adds a new system to the database.
- "CLEAR" button clears the input fields.

Fill out the input fields and press "ADD".
"""
        messagebox.showinfo("System Info", main_menu) 

# Clears the input fields
    def Clear_Input_Fields(self):
        self.paltfrom_name_text.set("")
        self.system_key_text.set("")
        self.full_system_name_text.set("")
       
# Pop up windowd
    def New_System_Added_Notification(self):
        add_message = """New system was added.
"""
        messagebox.showinfo("System Message", add_message) 

# Checks if the input fields are empty or not
    def Check_Inputs(self):
        error_message = """Fill out all the fields!
"""
        if self.paltfrom_name_text.get() == "" or self.paltfrom_name_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.system_key_text.get() == "" or self.system_key_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        elif self.full_system_name_text.get() == "" or self.full_system_name_text.get() == None:
                messagebox.showinfo("System Message", error_message) 
        else:
                App_Manager.New_System(self.steamgrid_api_entry_text.get(), self.paltfrom_name_text.get(), self.system_key_text.get(), self.full_system_name_text.get())
                self.New_System_Added_Notification()
                self.Clear_Input_Fields()