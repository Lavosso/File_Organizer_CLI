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
    data_file_extensions = {".txt", ".jpg", ".pdf", ".py", ".mp3"}
    correct_result = {
        ".txt": ["harmonogram.txt"],
        ".jpg": ["pies.jpg"],
        ".pdf": ["regulamin_sklepu.pdf", "deklaracja.pdf"],
        ".py": ["test_main.py", "scraper.py"],
        ".mp3": ["outro.mp3"],
    }
    assert correct_result == planner.map_files_to_extensions(
        data_files, data_file_extensions
    )


def test_map_files_to_extensions_no_name():
    data_files = [".mp3", ".txt", "abc.mp3"]
    data_file_extensions = {".txt", ".mp3"}
    correct_result = {
        ".mp3": [".mp3", "abc.mp3"],
        ".txt": [".txt"],
    }
    assert correct_result == planner.map_files_to_extensions(
        data_files, data_file_extensions
    )


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
