import json
import os

from helpers.os import scan_array_input, scan_input
from helpers.strings import normalize_string, normalize_string_lower

# Function to create a new platform
def create_platform(PATH, steamgrid_api_key, name, database_key, manufacturer, screen_size, resolution, battery_life, weight, system, cpu, gpu, ram, arch, storage, media, connectivity):
    """
    Creates a new platform by getting the data from Platfrom_Window.py.

    Parameters:
    platform_name_arg (str): The name of the platform to be created.
    steamgrid_api_key (str): The Steamgrid api key to get autorized.
    name (str): Full name of the device.
    database_key (str): Key value to refer to the device in the database.
    manufacturer (str)
    screen_size (str)
    resolution (str)
    battery_life (str)
    weight (str)
    system (str)
    cpu (str)
    gpu (str)
    ram (str)
    arch (str)
    storage (str)
    media (str)
    connectivity (str)
    """
    attributes = {}

    # Prompting user for platform attributes
    attributes["name"] = name
    attributes["database_key"] = normalize_string_lower(database_key)
    attributes["manufacturer"] = manufacturer
    attributes["screen_size"] = screen_size
    attributes["resolution"] = resolution
    attributes["battery_life"] = battery_life
    attributes["weight"] = weight
    attributes["system"] = system
    attributes["cpu"] = cpu
    attributes["gpu"] = gpu
    attributes["ram"] = ram
    attributes["arch"] = arch
    attributes["storage"] = storage
    attributes["media"] = media
    attributes["connectivity"] = connectivity
    attributes["systems"] = [{"name": "Name", "key": "key"}]

    # Normalize database_key to use as directory name
    platform_name = normalize_string(database_key)
    platform_dir = os.path.join(PATH[0],'commons','platforms', platform_name)
    os.makedirs(platform_dir, exist_ok=True)

    # Create index.json for the platform
    platform_index_path = os.path.join(platform_dir, 'index.json')
    if not os.path.exists(platform_index_path):
        with open(platform_index_path, 'w') as f:
            json.dump(attributes, f, indent=4)
    
    # Update the list of platforms in the main index.json
    update_platforms_list(attributes, platform_name)
# Function to update the list of platforms in the main index.json
def update_platforms_list(attributes, platform_name):
    """
    Updates the main index.json file to include the newly created platform.

    Parameters:
    attributes (dict): The attributes of the newly created platform.
    platform_name: normalized platform name, for setting the image path
    """
    platforms_list = []
    
    platforms_list_path = os.path.join('platforms', 'index.json')
    if os.path.exists(platforms_list_path):
        with open(platforms_list_path, 'r') as f:
            try:
                data = json.load(f)
                platforms_list = data.get('platforms', [])
            except json.JSONDecodeError:
                platforms_list = []
    
    # Extract relevant attributes for the platform entry
    platform_entry = {
        "name": attributes["name"],
        "database_key": attributes["database_key"],
        "image": ("platforms/"+ platform_name + ".webp"),
        "manufacturer": attributes.get("manufacturer", ""),
        "system": attributes.get("system", "")
    }

    platforms_list.append(platform_entry)

    # Write updated platform list back to index.json
    data = {"platforms": platforms_list}

    with open(platforms_list_path, 'w') as f:
        json.dump(data, f, indent=4)