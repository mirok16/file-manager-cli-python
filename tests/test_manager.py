from file_manager.manager import list_files

def test_list_files():
    files = list_files()
    assert isinstance(files, list)
from file_manager.manager import create_file
import os

def test_create_file():
    create_file("test.txt")
    assert os.path.exists("test.txt")
    os.remove("test.txt")
from file_manager.manager import delete_file

def test_delete_file():
    create_file("delete_me.txt")
    delete_file("delete_me.txt")
