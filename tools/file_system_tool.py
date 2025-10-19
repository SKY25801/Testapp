import os

def list_files(path="."):
    """Lists files in a directory, preventing directory traversal."""
    try:
        # Get the absolute path of the intended directory
        base_dir = os.path.abspath(os.getcwd())
        requested_path = os.path.abspath(os.path.join(base_dir, path))

        # Check if the requested path is within the base directory
        if not requested_path.startswith(base_dir):
            return ["Error: Directory traversal is not allowed."]

        return os.listdir(requested_path)
    except FileNotFoundError:
        return ["Error: Directory not found."]
    except Exception as e:
        return [f"An error occurred: {e}"]
