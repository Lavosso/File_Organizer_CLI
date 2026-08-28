
from src import files


def test_list_files_in_directory(tmpdir):
    directory_path = tmpdir
    file1 = tmpdir / "file1.txt"
    file1.write_text("data", encoding="utf-8")
    file2 = tmpdir / "file2.txt"
    file2.write_text("data", encoding="utf-8")
    file3 = tmpdir / "file3.mp3"
    file3.write_text("data", encoding="utf-8")
    correct_list = [
        "file1.txt",
        "file2.txt",
        "file3.mp3",
    ]
    assert set(correct_list) == set(
        files.list_files_in_directory(directory=directory_path)
    )


def test_list_files_in_directory_no_files(tmpdir):
    directory_path = tmpdir
    assert not files.list_files_in_directory(directory=directory_path)


def test_list_files_in_directory_has_dirs(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("data")
    file2 = tmp_path / "file2.mp3"
    file2.write_text("data")
    sub_dir = tmp_path / "directory"
    sub_dir.mkdir()
    correct_list = ["file1.txt", "file2.mp3"]
    assert set(correct_list) == set(files.list_files_in_directory(directory=tmp_path))


def test_list_directories_in_directory(tmp_path):
    sub_dir = tmp_path / "directory"
    sub_dir.mkdir()
    sub_dir2 = tmp_path / "directory2"
    sub_dir2.mkdir()
    file1 = tmp_path / "file1.txt"
    file1.write_text("data")
    correct_list = ["directory", "directory2"]
    assert set(correct_list) == set(
        files.list_directories_in_directory(directory=tmp_path)
    )


def test_list_directories_in_directory_no_dirs(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("data")
    assert set() == set(files.list_directories_in_directory(directory=tmp_path))


def test_create_directories_for_categories(tmp_path):
    categories = {"cat1", "cat2"}
    files.create_directories_for_categories(categories=categories, directory=tmp_path)
    assert tmp_path.joinpath("cat1").exists() and tmp_path.joinpath("cat2").exists()


def test_move_files_to_category(tmp_path):
    category = ".cat1"
    (tmp_path / category).mkdir()
    file1 = tmp_path / "file1.cat1"
    file2 = tmp_path / "file2.cat1"
    file2.write_text("data")
    file1.write_text("data")
    file_list = ["file1.cat1", "file2.cat1"]
    files.move_files_to_category_dir(file_list, category=category, directory=tmp_path)
    assert (
        tmp_path.joinpath(".cat1").joinpath("file1.cat1").exists()
        and tmp_path.joinpath(".cat1").joinpath("file2.cat1").exists()
    )
