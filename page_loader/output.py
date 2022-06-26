import os


def save_as_file(data, path):
    if isinstance(data, str):
        with open(path, 'w') as file:
            file.write(data)
    else:
        with open(path, 'wb') as file:
            file.write(data)
    return


def create_directory(path):
    name, ext = os.path.splitext(path)
    file_dir_path = name + '_files'
    if not os.path.exists(file_dir_path):
        os.mkdir(file_dir_path)
    return file_dir_path
