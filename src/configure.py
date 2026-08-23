import json
import sys


def edit_mapping(extension: str, file_type: str):
    with open("src/file_types.json", "r") as config_file:
        config = json.load(config_file)
    if extension not in config:
        raise KeyError(f"{extension} is not a valid file extension")
    config[extension] = file_type
    with open("src/file_types.json", "w") as config_file:
        json.dump(config, config_file, indent=4)


def add_mapping(extension: str, file_type: str):
    with open("src/file_types.json", "r") as config_file:
        config = json.load(config_file)
    if extension in config:
        raise KeyError(f"{extension} is already a mapped file extension")
    config[extension] = file_type
    with open("src/file_types.json", "w") as config_file:
        json.dump(config, config_file, indent=4)


def delete_mapping(extension_to_delete: str):
    with open("src/file_types.json", "r") as config_file:
        config = json.load(config_file)
    new_config = {
        extension: file_type
        for extension, file_type in config.items()
        if extension != extension_to_delete
    }
    with open("src/file_types.json", "w") as config_file:
        json.dump(new_config, config_file, indent=4)


def print_current_config():
    print("##### current config: #####")
    with open("src/file_types.json", "r") as config_file:
        config = json.load(config_file)
    for extension, file_type in config.items():
        print(f"{extension} -> {file_type}")


def configure_cli():
    print_current_config()
    while True:
        decision = input(
            "Would you like to: \n"
            "(e) edit a file extension to types mapping, \n"
            "(a) add a file extension to types mapping, \n"
            "(d) delete a file extension to types mapping, or \n"
            "(x) exit the program?\n"
        )
        if decision == "e":
            extension = input(
                "What file extension would you like to map differently?\n"
            )
            file_type = input(
                "What file type would you like the extension to be mapped to?\n"
            )
            edit_mapping(extension, file_type)
        elif decision == "a":
            extension = input("What file extension would you like to map?\n")
            file_type = input(
                "What file type would you like the extension to be mapped to?\n"
            )
            add_mapping(extension, file_type)
        elif decision == "d":
            extension = input("What file extension would you like to unmap?\n")
            delete_mapping(extension)
        elif decision == "x":
            sys.exit()
