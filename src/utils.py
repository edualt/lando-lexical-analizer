def load_content_from_file(path: str):
    with open(path, 'r') as f:
        return f.read()