from pathlib import Path

def map_files(files: list, file_types: list) -> dict[str, list]:
    mapped_files = {datatype:[] for datatype in file_types}
    for file in files:
        mapped_files[Path(file).suffix].append(file)
    return mapped_files

