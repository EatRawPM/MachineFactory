from os import walk
from os.path import join
from pygame.image import load

def imports_files(folder_path):
    images = []

    for path, folders, files in walk(folder_path):
        for file in files:
            images.append(load(join(path, file)))

    return images