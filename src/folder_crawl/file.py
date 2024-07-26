import os
import pathlib


# Read Config file
class Config:
    def __init__(self, file_path):
        self.file_path = pathlib.Path(os.path.join(file_path, "README", ".conf"))

    def exists(self):
        return self.file_path.is_file()
