from file_manager.manager import list_files

def test_list_files():
    files = list_files()
    assert isinstance(files, list)
