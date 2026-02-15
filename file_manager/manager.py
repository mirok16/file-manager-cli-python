import os
def list_files(path="."):
    return os.listdir(path)
def create_file(filename):
    with open(filename, "w") as f:
        f.write("")
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
if __name__ == "__main__":
    print("Files:", list_files())
# Lists files in directory
# Creates empty file
# Deletes file if exists
