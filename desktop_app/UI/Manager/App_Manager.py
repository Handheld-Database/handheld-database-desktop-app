# This class will manage all interaction with the different scripts.

import os
import json
from tkinter import filedialog

try:
    from UI.Manager.funcs import platforms
except ImportError:
    print("App_Manager - Coudn't import platfroms.py")

try:
     from UI.Manager.funcs import systems
except ImportError:
    print("App_Manager - Coudn't import systems.py")


# mutable lists, only the value changes
database_root_path = [None]
scaned_platfroms = [None]
scanned_systems_in_choosen_platfrom = [None]

# Saves and returns the choosen directory.
def Set_Directory():
        database_root_path[0] = filedialog.askdirectory()
        return database_root_path[0]

# Scans the existing platfrom folder's content and removes non directories.
def List_Platforms():
        platfroms_path = os.path.join(database_root_path[0], 'platforms') # Gets all the entities in that folder
        list_of_things = os.listdir(platfroms_path)

        scaned_platfroms = [None]

        # Removes the index.json from the list
        for things in list_of_things:
            if(things != "index.json"):
                scaned_platfroms.append(things)
        scaned_platfroms.pop(0) # removes the first element
        #print(scaned_platfroms)
        return scaned_platfroms
                
# Scans the platfroms and lists the existing systems in a platfrom
def List_Systems_In_Platfroms(selected_platfrom):
        list_of_things = os.listdir(os.path.join(database_root_path[0], 'platforms', selected_platfrom, 'systems')) # Gets all the entities in that folder

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

# Create a new system
def New_System(steamgrid_api_key, platfrom_name, system_key, full_system_name):
    systems.create_system(database_root_path, steamgrid_api_key, platfrom_name, system_key, full_system_name)

# Reads the .json file in platfrom folders and gets the systems for every platfrom
def Read_Systems_In(platform_name):
    system_list_index_path = os.path.join(database_root_path[0],'platforms', platform_name, 'index.json')
    system_list_helper = {}
    system_list = []

    # Reading index.json and storing "systems" attribute.
    if os.path.exists(system_list_index_path):
        with open(system_list_index_path, 'r') as f:
            try:
                data = json.load(f)
                system_list_helper= data.get('systems', [])
                f.close()
            except json.JSONDecodeError:
                system_list_helper = []

    array_lenght = len(system_list_helper)
    for i in range(array_lenght):
        system_list.append(system_list_helper[i]["key"])

    return system_list_helper