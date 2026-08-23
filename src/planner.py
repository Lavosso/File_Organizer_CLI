import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def list_extensions(files: list) -> set:
    extensions_set = set()
    for file in files:
        if Path(file).suffix:
            extensions_set.add(Path(file).suffix)
        else:
            extensions_set.add(file)
    return extensions_set


def list_categories(plan: dict[str, list]) -> set:
    categories_set = {key for key in plan}
    return categories_set


def map_files_to_extensions(
    file_list: list, verbose_mode: bool = False
) -> dict[str, list]:
    extensions = list_extensions(file_list)
    mapped_files: dict = {extension: [] for extension in extensions}
    if verbose_mode:
        logger.setLevel(logging.DEBUG)
    for file in file_list:
        if Path(file).suffix:
            mapped_files[Path(file).suffix].append(file)
            logger.debug(
                f"successfully mapped file {file} to category {Path(file).suffix}"
            )
        else:
            mapped_files[file].append(file)
            logger.debug(f"successfully mapped file {file} to category {file}")
    logging.debug("files mapped to extensions successfully, sending back...")
    return mapped_files


def map_files_to_file_types(
    raw_file_list: list, verbose_mode: bool = False
) -> dict[str, list]:
    if verbose_mode:
        logger.setLevel(logging.DEBUG)
    logger.debug("raw file list mapped to extensions for easier further actions")
    files_mapped_to_extensions = map_files_to_extensions(raw_file_list)
    with open("src/file_types.json", "r") as file_types_json_data:
        file_types = json.load(file_types_json_data)
        logger.debug("loaded data from file_types.json")
    file_mapped_to_file_types: dict[str, list] = {}
    for extension, file_list in files_mapped_to_extensions.items():
        try:
            file_type = file_types[extension]
            logger.debug("file extension defined by file_types.json. Mapped to file type accordingly")
        except KeyError:
            file_type = "Other"
            logger.debug("file extension not defined by file_types.json. Mapped to 'Other'")
        try:
            for file in file_list:
                file_mapped_to_file_types[file_type].append(file)
                logger.debug(f"put file {file} into category {file_type}")
        except KeyError:
            file_mapped_to_file_types[file_type] = file_list
            logger.debug(f"created category {file_type} and put the first extension package in")
    logger.debug("files mapped to file types successfully, sending back...")
    return file_mapped_to_file_types
