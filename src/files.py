import logging
import os
import sys
import time
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def map_file_to_date(directory: str):
    creation_time = time.strftime(
        "%Y-%m-%d", time.localtime(os.path.getctime(directory))
    )
    return Path(directory).name, creation_time


def list_files_in_directory(directory: str) -> list:
    dir_insides = os.listdir(path=directory)
    dir_files = [
        element
        for element in dir_insides
        if not Path(directory + "/" + element).is_dir()
    ]
    if not dir_files:
        logger.warning("no user files found - no organizing can be done.")
        sys.exit(0)
    return dir_files


def list_directories_in_directory(directory: str) -> list:
    dir_insides = os.listdir(path=directory)
    dir_dirs = [
        element for element in dir_insides if Path(directory + "/" + element).is_dir()
    ]
    return dir_dirs


def create_directories_for_categories(
    categories: set,
    directory: str,
    verbose_mode: bool = False,
    dry_run: bool = False,
    showoff: bool = False,
) -> None:
    if verbose_mode or dry_run:
        logger.setLevel(logging.DEBUG)
    for category in categories:
        if os.path.exists(directory + "/" + category):
            logger.error(
                f"There exists a folder with the name {category} in directory. Terminating with no changes."
            )
            sys.exit()
    for category in categories:
        if showoff:
            time.sleep(1)
        if not dry_run:
            os.makedirs(directory + "/" + category)
        logger.debug("successfully created directory for category " + category)


def move_files_to_category_dir(
    file_list: list,
    category: str,
    directory: Path | str,
    verbose_mode: bool = False,
    dry_run: bool = False,
    showoff: bool = False,
) -> None:
    if verbose_mode or dry_run:
        logger.setLevel(logging.DEBUG)
    for file in file_list:
        if showoff:
            time.sleep(1)
        if not dry_run:
            os.rename(
                str(directory) + "/" + file,
                str(directory) + "/" + category + "/" + file,
            )
        logger.debug(f"successfully moved file {file} to directory {category}")
