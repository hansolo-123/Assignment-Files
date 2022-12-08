__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile


# 1
def clean_cache():
    directory = "cache"
    parent_dir = os.path.normpath("C:/Users/mordr/Winc Academy/Back_end_dev/files/")
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
        print("Directory '% s' created" % directory)
    except OSError:
        child_dir = "C:/Users/mordr/Winc Academy/Back_end_dev/files/cache"
        for f in os.listdir(child_dir):
            os.remove(os.path.join(child_dir, f))
        print("Directory '% s' already exists cache folder emptied" % directory)


# 2
def cache_zip(zip_folder, destination):
    with zipfile.ZipFile(zip_folder) as zf:
        zf.extractall(destination)


# 3
def cached_files():
    folder = os.path.normpath("C:/Users/mordr/Winc Academy/Back_end_dev/files/cache")
    absolute_path = [os.path.join(folder, f) for f in os.listdir(folder)]
    return absolute_path


# 4
def find_password(files):
    keywords = ['password', 'username', 'user', 'x', 'login']

    for root, _, files in os.walk('C:/Users/mordr/Winc Academy/Back_end_dev/files/cache'):
        for path in filter(lambda p: p.endswith('.txt'), files):
            with open(os.path.join(root, path)) as f:
                for i, line in enumerate(f.readlines()):
                    for word in filter(lambda w: w in line, keywords):
                        print(f'{path}, {i+1}, {word}, {line.strip()}')
                        password_fase_1 = line.strip()
                        password_fase_2 = password_fase_1[password_fase_1.find(' '):]
                        password = password_fase_2.lstrip()
                        print(password)
                        return password


# 1
clean_cache()
# 2
zip_folder = "c:/Users/mordr/Winc Academy/Back_end_dev/files/data.zip"
destination = "c:/Users/mordr/Winc Academy/Back_end_dev/files/cache"
cache_zip(zip_folder, destination)
# 3
cached_files()
# 4
find_password(files=cached_files)
