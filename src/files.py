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
