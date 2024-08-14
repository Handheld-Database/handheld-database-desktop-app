import os
import tkinter as tk
from tkinter import filedialog



root=tk.Tk()    

ent1=tk.Entry(root,font=40)
ent1.grid(row=2,column=2)

# Scans the existing platfroms and removes non directories.
def list_platforms():
    list_of_things = os.listdir(filedialog.askdirectory())
    platfroms = []

    for things in list_of_things:
        if(things != "index.json"):
            platfroms.append(things)

   #print("Platfroms:  " + str(platfroms))
    return platfroms



b1=tk.Button(root,text="DEM",font=40,command=list_platforms)
b1.grid(row=2,column=4)

root.mainloop()



