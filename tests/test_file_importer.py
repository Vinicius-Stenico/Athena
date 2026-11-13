from pathlib import Path

import pytest

from athena.file_importer import filter_files, get_supported_files, list_files


def test_filter_files():
	files = [
        Path("python.pdf"), 
        Path("image.png"), 
        Path("notes.txt")
    ]
	
	result = filter_files(files)
	
	assert result == [
        Path("python.pdf"), Path("notes.txt")
    ]

def test_filter_files_empty():
    files = []

    result = filter_files(files)

    assert result == []

def test_filter_files_uppercase():
    files = [
        Path("Python.PDF"),
        Path("Database.DOCX"),
        Path("image.PNG")  
    ]

    result = filter_files(files)

    assert result == [
        Path("Python.PDF"),
        Path("Database.DOCX")
    ]

def test_list_files(tmp_path):
    files = ["notes.txt", "python.pdf"]
    folders = ["images"]

    for filename in files:
         file_path = tmp_path / filename
         file_path.touch()

    for foldername in folders:
         folder_path = tmp_path / foldername
         folder_path.mkdir()

    result = list_files(tmp_path)
    
    assert set(result) == {
         tmp_path / "notes.txt",
         tmp_path / "python.pdf"
    }

def test_list_files_nonexistent_directory(tmp_path):
     folder_path = tmp_path / "missing"

     with pytest.raises(FileNotFoundError):

        list_files(folder_path)

def test_get_supported_files(tmp_path):
    files = ["python.pdf", "notes.txt", "image.png"]
    folders = ["images"]

    for filename in files:
         file_path = tmp_path / filename
         file_path.touch()

    for foldername in folders:
         folder_path = tmp_path / foldername
         folder_path.mkdir()

    result = get_supported_files(tmp_path)

    assert set(result) == {
         tmp_path / "notes.txt",
         tmp_path / "python.pdf"
    }