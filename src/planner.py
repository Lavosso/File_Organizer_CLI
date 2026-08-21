from pathlib import Path


def read_category(files: list, category: str = "extension") -> set:
    category_list = set()
    file_category = ""
    for file in files:
        if category == "extension":
            file_category = Path(file).suffix
        category_list.add(file_category)
    return category_list


def map_files(files: list, file_types: set) -> dict[str, list]:
    mapped_files: dict = {datatype: [] for datatype in file_types}
    for file in files:
        mapped_files[Path(file).suffix].append(file)
    return mapped_files
