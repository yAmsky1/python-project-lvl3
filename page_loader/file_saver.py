def write_data_to_file(data, path):
    with open(path, 'wb') as file:
        file.write(data.content)
    return
