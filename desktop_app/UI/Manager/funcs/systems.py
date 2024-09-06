import json
import os
import re


# Function to create a new system under a specified platform
def create_system(PATH, steamgrid_api_key, platform_name, system_key, full_system_name):
    """
    Creates a new system under a specified platform by creating the necessary directory structure and an index.json file.

    Parameters:
    platform_name (str): The name of the platform under which the system will be created.
    system_name (str): The name of the system to be created.
    """
    
    # Define the directory path for the new system
    system_dir = os.path.join(PATH[0],'platforms', normalize_string_lower(platform_name), 'systems', normalize_string_lower(system_key))
    
    # Create the directory if it does not exist
    os.makedirs(system_dir, exist_ok=True)
    
    # Define the path for the system's index.json file
    system_index_path = os.path.join(system_dir, 'index.json')
    if not os.path.exists(system_index_path):
        # Create and write the initial JSON structure to index.json
        with open(system_index_path, 'w') as f:
            json.dump({"name": normalize_string_lower(system_key), "games": []}, f, indent=4)
    
    # Updating the list of systems in platforms/myplatform/index.js
    update_system_list(PATH, normalize_string_lower(platform_name), normalize_string_lower(system_key), normalize_string(full_system_name))

# Funtion to update the system list for the platform
def update_system_list(PATH, platform_name, system_name_as_key, full_system_name):
    """
    Updates the list of systems with the new added system name and key.

    Parameters:
    platform_name (str): normalized name of the platfrom.
    system_name_as_key (str): normalized name of the system.
    full_system_name (str): The systems full name
    """

    # Platform's index.js path that contains the list of systems. /platforms/myplatformname/index.js
    system_list_index_path = os.path.join(PATH[0],'platforms', platform_name, 'index.json')
    system_list = []
    exist = 0

    # Reading index.json and storing "systems" attribute.
    if os.path.exists(system_list_index_path):
        with open(system_list_index_path, 'r') as f:
            try:
                data = json.load(f)
                system_list= data.get('systems', [])
                f.close()
            except json.JSONDecodeError:
                system_list = []

    # Construct data which will be added to the list
    system_entry = {
        "name": full_system_name,
        "key": system_name_as_key
    }

    # Check if the to be added system already in the list.
    for item in system_list:
        if(item['key'] == system_entry['key']):
            exist = 1
            break

    # Add the new system to the file and write it, if it does not exists.
    match exist:
        case 1:
            print("---------------------------------")
            print("|  This system already exists in "+ system_name_as_key +"  |")
            print("---------------------------------")
        case _: # default case
            with open(system_list_index_path, 'w') as f:
                data["systems"].append(system_entry)   
                json.dump(data, f, indent = 4)  
                f.close()
                print()
                print("|-->  System added to " + platform_name + "  <--|")
                print()
           
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