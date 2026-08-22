from pathlib import Path
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def list_extensions(files: list) -> set:
    extensions_list = {Path(file).suffix for file in files}
    return extensions_list


def map_files_to_extensions(files: list, extensions: set, verbose_mode: bool = False) -> dict[str, list]:
    mapped_files: dict = {extension: [] for extension in extensions}
    if verbose_mode:
        logger.setLevel(logging.DEBUG)
    for file in files:
        mapped_files[Path(file).suffix].append(file)
        logger.debug(f"successfully mapped file {file} to category {Path(file).suffix}")
    return mapped_files
