import os


SHAPE_FILES_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/shape_files/data"


def read_shape_file(file_name: str) -> str:
    file_path = os.path.join(SHAPE_FILES_DIR, f"{file_name}.ttl")
    with open(file_path, 'r', encoding="utf-8") as shape_file:
        return shape_file.read()
