import os
from pathlib import Path


def list_files_in_directory(directory: str) -> list:
    dir_insides = os.listdir(path=directory)
    dir_files = [
        element
        for element in dir_insides
        if not Path(directory + "/" + element).is_dir()
    ]
    return dir_files


def list_directories_in_directory(directory: str) -> list:
    dir_insides = os.listdir(path=directory)
    dir_dirs = [
        element for element in dir_insides if Path(directory + "/" + element).is_dir()
    ]
    return dir_dirs


def create_directories_for_categories(categories: set, directory: str) -> None:
    for category in categories:
        if not os.path.exists(directory + "/" + category):
            os.makedirs(directory + "/" + category)


def move_files_to_category_dir(files: list, directory: str) -> None:
    files_folder = Path(directory).parent
    for file in files:
        os.rename(files_folder / file, directory + "/" + file)
