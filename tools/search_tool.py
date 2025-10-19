import os

def search(query):
    """Searches for files in the current directory that contain the query."""
    results = []
    for filename in os.listdir("."):
        if query in filename:
            results.append(filename)
    return results if results else "No matching files found."
