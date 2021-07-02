__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import zipfile
# path = './files/cache'              # de current directory is files
# zip_list = './files/data.zip'
path = os.path.dirname(os.path.realpath(__file__))
zip_list = os.path.join(path, 'cache')


def clean_cache():
    if os.path.isdir(zip_list):
        shutil.rmtree(zip_list)  # delete folder/cache
        os.mkdir(zip_list)  # create folder/cache
    else:
        return os.mkdir(zip_list)


# clean_cache()


def cache_zip(file_path: str, cache_dir_path: str):
    with zipfile.ZipFile(file_path, 'r') as zipObj:
        zipObj.extractall(cache_dir_path)
# cache_zip(zip_l   ist, path)


def cached_files():
    file_list = []
    for root, dirs, files in os.walk(os.getcwd()+'\\cache'):
        for name in files:
            if root[-6:] == '\\cache':  # exclude files in subfolders
                file_list.append(os.path.join(root, name))
    return file_list
# print(cached_files())


def find_password(file_list):
    search_pw = "password:"
    for cached_file in file_list:
        with open(cached_file) as f:
            lines = f.readlines()
        for line in lines:
            if search_pw in line:
                return line.replace(search_pw, '').strip()
            else:
                continue
