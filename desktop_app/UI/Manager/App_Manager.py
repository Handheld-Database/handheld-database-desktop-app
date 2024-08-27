# This class will manage all interaction with the different scripts.

import os
from tkinter import filedialog

try:
        from funcs import platforms
except ImportError:
        print(" App_Manager - Coudn't import platfroms.py")

# mutable lists, only the value changes
database_root_path = [None]
scaned_platfroms = [None]
scanned_systems_in_choosen_platfrom = [None]

def print_out_things(thing):
    print(thing)

# Saves and returns the choosen directory.
def set_directory():
    database_root_path[0] = filedialog.askdirectory()
    return database_root_path[0]

# Scans the existing platfrom folder's content and removes non directories.
def list_platforms():
    platfroms_path = os.path.join(database_root_path[0], 'commons', 'platforms') # Gets all the entities in that folder
    list_of_things = os.listdir(platfroms_path)

    scaned_platfroms = [None]

    # Removes the index.json from the list
    for things in list_of_things:
        if(things != "index.json"):
            scaned_platfroms.append(things)
    scaned_platfroms.pop(0) # removes the first element
    #print(scaned_platfroms)
    return scaned_platfroms
            
# Scans the platfroms and lists the existing systems in them.
def list_systems_in_platfroms(selected_platfrom):
    list_of_things = os.listdir(os.path.join(database_root_path[0],'commons', 'platforms', selected_platfrom, 'systems')) # Gets all the entities in that folder

    #scanned_systems_in_choosen_platfrom = [None]

    # Removes the index.json from the list
    for things in list_of_things:
        if(things != "index.json"):
            scanned_systems_in_choosen_platfrom.append(things)
    scanned_systems_in_choosen_platfrom.pop(0)  # removes the first element
    print(scanned_systems_in_choosen_platfrom) 
    return scanned_systems_in_choosen_platfrom

# Creates the new platfrom with data from the UI elements.
def New_Platfrom(steamgrid_api_key, name, database_key, manufacturer, screen_size, resolution, battery_life, weight, system, cpu, gpu, ram, arch, storage, media, connectivity):
    platforms.create_platform(database_root_path, steamgrid_api_key, name, database_key, manufacturer, screen_size, resolution, battery_life, weight, system, cpu, gpu, ram, arch, storage, media, connectivity)
    #test.print_out_things("REeeeeeee")
    print("Add a new platfrom")
