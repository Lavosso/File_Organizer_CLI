from pathlib import Path


def list_extensions(files: list) -> set:
    extensions_list: set = {Path(file).suffix for file in files}
    return extensions_list


def map_files_to_categories(files: list, categories: set) -> dict[str, list]:
    mapped_files: dict = {category: [] for category in categories}
    for file in files:
        mapped_files[Path(file).suffix].append(file)
    return mapped_files
