import os

def list_files(path="."):
    """Lists files in a directory."""
    return os.listdir(path)
