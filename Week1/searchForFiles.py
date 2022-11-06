from pathlib import Path
import os


def searchForFiles(path):
    path = Path(path)
    for file in path.glob("*.*"):
        print(file)

    # files = list(path.glob('**/*.' + extension))
    # return files
searchForFiles("/Users/user/")

