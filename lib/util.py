import json

def save(data_all, save_name):
    save_byte = bytearray()
    for data in data_all:
        save_byte += data

    assert len(data_all) == len(save_byte), "length has to be fixed"

    with open(save_name, mode="wb") as file:
        file.write(save_byte)


def load(file_name):
    with open(file_name, mode="rb") as file:
        file_content = file.read()

    data_all = []
    for i in range(len(file_content)):
        data = file_content[i : i + 1]
        data_all.append(data)

    return data_all


def load_json(filename):
    with open(filename, "r") as rf:
        keys = json.load(rf)
    return keys
