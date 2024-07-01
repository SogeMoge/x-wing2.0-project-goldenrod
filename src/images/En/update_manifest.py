import os
import json


def list_png_files(directory, base_dir):
    files_dict = {}
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            key = os.path.splitext(filename)[0]
            files_dict[key] = f"{base_dir}/{filename}"
    return files_dict


# Directories containing the .png files
pilot_directory = "pilots"
upgrade_directory = "upgrades"
remotes_directory = "remotes"
condition_directory = "Condition"

# Base directory names
base_pilot = "pilots"
base_upgrade = "upgrades"
base_remotes = "remotes"
base_condition = "Condition"

# Create the final data structure
data = {
    "pilots": list_png_files(pilot_directory, base_pilot),
    "upgrades": list_png_files(upgrade_directory, base_upgrade),
    "remotes": list_png_files(remotes_directory, base_remotes),
    "conditions": list_png_files(condition_directory, base_condition),
}

# Create a JSON file and write the dictionary to it
with open("manifest.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

print("JSON file created successfully.")
