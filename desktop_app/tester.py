import tkinter as tk

# This is just for testing things.


# dynamic dropdown menu test
def on_option_select():
    selected = selected_option.get()
    result_label.config(text=f"Selected Option: {selected}")
    
root = tk.Tk()
root.title("Dropdown Menu Example")
root.geometry("400x300")

# Create a StringVar to hold the selected option
selected_option = tk.StringVar()

# Create the dropdown menu
dropdown = tk.OptionMenu(root, selected_option, "Select an option")
dropdown.pack(pady=10)

# A list of options to populate the dropdown
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Populate the dropdown menu with the list of options
for option in options:
    dropdown["menu"].add_command(label=option, command=lambda opt=option: selected_option.set(opt))

# Add a button to display the selected option
show_button = tk.Button(root, text="Show Selection", command=on_option_select)
show_button.pack()

# Label to display the selected option
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()