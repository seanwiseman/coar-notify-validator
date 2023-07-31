import os


SHAPE_FILES_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/shape_files/data"


def read_shape_file(file_name: str) -> str:
    with open(os.path.join(SHAPE_FILES_DIR, f"{file_name}.ttl"), 'r') as f:
        return f.read()
