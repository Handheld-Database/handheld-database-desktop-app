import json
import os
import re

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
    attributes["name"] = str(name)
    attributes["database_key"] = normalize_string_lower(str(database_key))
    attributes["manufacturer"] = str(manufacturer)
    attributes["screen_size"] = str(screen_size)
    attributes["resolution"] = str(resolution)
    attributes["battery_life"] = str(battery_life)
    attributes["weight"] = str(weight)
    attributes["system"] = str(system)
    attributes["cpu"] = str(cpu)
    attributes["gpu"] = str(gpu)
    attributes["ram"] = str(ram)
    attributes["arch"] = str(arch)
    attributes["storage"] = str(storage)
    attributes["media"] = str(media)
    attributes["connectivity"] = str(connectivity)
    attributes["systems"] = [{"name": "Name", "key": "key"}]

    # Normalize database_key to use as directory name
    platform_name = normalize_string_lower(str(database_key))
    platform_dir = os.path.join(PATH[0],'commons','platforms', platform_name)
    os.makedirs(platform_dir, exist_ok=True)

    # Create index.json for the platform
    platform_index_path = os.path.join(platform_dir, 'index.json')
    if not os.path.exists(platform_index_path):
        with open(platform_index_path, 'w') as f:
            json.dump(attributes, f, indent=4)
    
    # Update the list of platforms in the main index.json
    update_platforms_list(attributes, platform_name, PATH)
# Function to update the list of platforms in the main index.json
def update_platforms_list(attributes, platform_name, PATH):
    """
    Updates the main index.json file to include the newly created platform.

    Parameters:
    attributes (dict): The attributes of the newly created platform.
    platform_name: normalized platform name, for setting the image path
    """
    platforms_list = []
    
    platforms_list_path = os.path.join(PATH[0],'commons','platforms', 'index.json')
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

# Function to normalize input string by removing extra spaces and non-word characters
def normalize_string(input_string):
    """
    Normalizes an input string by removing extra spaces and non-word characters.

    Parameters:
    input_string (str): The string to be normalized.

    Returns:
    str: The normalized string.
    """
    # Collapse multiple spaces into one
    normalized_string = re.sub(r'\s+', ' ', input_string)
    # Remove non-word characters
    normalized_string = re.sub(r'[^\w\s]', '', normalized_string)
    # Remove leading/trailing spaces
    normalized_string = normalized_string.strip()
    return normalized_string

# Function to normalize input string by removing all spaces, non-word characters and converting to lower case
def normalize_string_lower(input_string):
    """
    Normalizes an input string by removing all spaces, non-word characters, 
    and converting the string to lower case.

    Parameters:
    input_string (str): The string to be normalized.

    Returns:
    str: The normalized string.
    """
    # Use the normalize_string function to remove extra spaces and non-word characters
    normalized_string = normalize_string(input_string)
    # Convert the string to lower case
    normalized_string = normalized_string.lower()
    # Remove all spaces
    normalized_string = re.sub(r'\s+', '', normalized_string)
    return normalized_string