import os
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

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


def create_directories_for_categories(categories: set, directory: str, verbose_mode: bool = False) -> None:
    if verbose_mode:
        logger.setLevel(logging.DEBUG)
    for category in categories:
        if os.path.exists(directory + "/" + category):
            logger.error(f"There exists a folder with the name {category} in directory. Terminating with no changes.")
            sys.exit()
    for category in categories:
        os.makedirs(directory + "/" + category)
        logger.debug("successfully created directory for category " + category)


def move_files_to_category_dir(files: list, directory: str, verbose_mode: bool = False) -> None:
    files_folder = Path(directory).parent
    if verbose_mode:
        logger.setLevel(logging.DEBUG)
    for file in files:
        os.rename(files_folder / file, directory + "/" + file)
        logger.debug(f"successfully moved file {file} to category {Path(file).suffix}")