import json

from src import planner


def test_map_files_to_extensions():
    data_files = [
        "outro.mp3",
        "regulamin_sklepu.pdf",
        "deklaracja.pdf",
        "test_main.py",
        "harmonogram.txt",
        "pies.jpg",
        "scraper.py",
    ]
    correct_result = {
        ".txt": ["harmonogram.txt"],
        ".jpg": ["pies.jpg"],
        ".pdf": ["regulamin_sklepu.pdf", "deklaracja.pdf"],
        ".py": ["test_main.py", "scraper.py"],
        ".mp3": ["outro.mp3"],
    }
    assert correct_result == planner.map_files_to_extensions(data_files)


def test_map_files_to_extensions_no_name():
    data_files = [".mp3", ".txt", "abc.mp3"]
    correct_result = {
        ".mp3": [".mp3", "abc.mp3"],
        ".txt": [".txt"],
    }
    assert correct_result == planner.map_files_to_extensions(data_files)


def test_map_files_to_file_types():
    data_files = [
        "outro.mp3",
        "regulamin_sklepu.pdf",
        "deklaracja.pdf",
        "test_main.py",
        "harmonogram.txt",
        "pies.jpg",
        "scraper.py",
    ]
    with open("src/file_types.json", "r") as f:
        file_types = json.load(f)
    result = planner.map_files_to_file_types(data_files)
    for file in data_files:
        assert result[
            file_types[
                next(
                    key
                    for key, value in planner.map_files_to_extensions([file]).items()
                )
            ]
        ].__contains__(file)


def test_map_files_to_file_types_no_name():
    data_files = [".mp3", ".txt", "abc.mp3"]
    with open("src/file_types.json", "r") as f:
        file_types = json.load(f)
    result = planner.map_files_to_file_types(data_files)
    for file in data_files:
        assert result[
            file_types[
                next(
                    key
                    for key, value in planner.map_files_to_extensions([file]).items()
                )
            ]
        ].__contains__(file)


def test_list_extensions():
    data_files = [
        "outro.mp3",
        "regulamin_sklepu.pdf",
        "deklaracja.pdf",
        "test_main.py",
        "harmonogram.txt",
        "pies.jpg",
        "scraper.py",
    ]
    data_file_types = {".txt", ".jpg", ".pdf", ".py", ".mp3"}
    assert data_file_types == planner.list_extensions(data_files)


def test_list_extensions_no_name():
    data_files = [
        "outro.mp3",
        "regulamin_sklepu.pdf",
        "deklaracja.pdf",
        "test_main.py",
        "harmonogram.txt",
        "pies.jpg",
        "scraper.py",
        ".gat",
    ]
    data_file_types = {".txt", ".jpg", ".pdf", ".py", ".mp3", ".gat"}
    assert data_file_types == planner.list_extensions(data_files)
