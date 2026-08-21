from pathlib import Path

def list_extensions(files: list) -> set:
    extensions_list = {Path(file).suffix for file in files}
    return extensions_list

def map_files(files: list, file_types: set) -> dict[str, list]:
    mapped_files: dict = {datatype: [] for datatype in file_types}
    for file in files:
        mapped_files[Path(file).suffix].append(file)
    return mapped_files
