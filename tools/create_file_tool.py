import os

def create_file(filename, content):
    """Creates a new file with the given content."""
    try:
        # Prevent directory traversal
        base_dir = os.path.abspath(os.getcwd())
        file_path = os.path.abspath(os.path.join(base_dir, filename))
        if not file_path.startswith(base_dir):
            return "Error: Directory traversal is not allowed."

        if os.path.exists(file_path):
            return f"Error: File '{filename}' already exists."

        with open(file_path, 'w') as f:
            f.write(content)
        return f"File '{filename}' created successfully."
    except Exception as e:
        return f"An error occurred: {e}"
