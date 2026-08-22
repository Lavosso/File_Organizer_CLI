import pytest
import src.files as files


def test_list_files_in_directory(tmpdir):
    directory_path = tmpdir
    tmpdir.mkdir("file1.txt")
    tmpdir.mkdir("file2.txt")
    tmpdir.mkdir("file3.mp3")
    correct_list = [
        "file1.txt",
        "file2.txt",
        "file3.mp3",
    ]
    assert set(correct_list) == set(
        files.list_files_in_directory(directory=directory_path)
    )


def test_list_files_in_directory_no_files(tmpdir):
    with pytest.raises(SystemExit):
        directory_path = tmpdir
        files.list_files_in_directory(directory=directory_path)


def test_list_files_in_directory_has_dirs(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("data")
    file2 = tmp_path / "file2.mp3"
    file2.write_text("data")
    sub_dir = tmp_path / "directory"
    sub_dir.mkdir()
    correct_list = ["file1.txt", "file2.mp3"]
    assert set(correct_list) == set(
        files.list_files_in_directory(directory=str(tmp_path))
    )
