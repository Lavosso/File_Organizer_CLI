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


def map_files_to_extensions(
    files: list, extensions: set, verbose_mode: bool = False
) -> dict[str, list]:
    mapped_files: dict = {extension: [] for extension in extensions}
    if verbose_mode:
        logger.setLevel(logging.DEBUG)
    for file in files:
        if Path(file).suffix:
            mapped_files[Path(file).suffix].append(file)
            logger.debug(
                f"successfully mapped file {file} to category {Path(file).suffix}"
            )
        else:
            mapped_files[file].append(file)
            logger.debug(f"successfully mapped file {file} to category {file}")

    return mapped_files
