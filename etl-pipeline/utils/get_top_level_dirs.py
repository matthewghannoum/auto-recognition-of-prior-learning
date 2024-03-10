import os

def get_top_level_dirs(dirpath: str) -> list[str]:
    return [
        name
        for name in os.listdir(dirpath)
        if os.path.isdir(os.path.join(dirpath, name))
    ]