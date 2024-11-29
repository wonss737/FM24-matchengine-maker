import os
import logging

from main import load

def find_key(data_all):
    for i in range(len(data_all)):
        data = data_all[i]
        try:
            char = data.decode("utf-8")
            if char < "A" or char > "z":
                continue
            else:
                yield(char)
        except:
            continue


path = "db"
output_dir = "traits"

exclude = [
    "backup",
    "23_1_1_9",
    "23_7_0_5",
    "23_9_9_1",
]

for dir_name, dir_list, file_list in os.walk(path, followlinks=True):
    dont_care = False
    for exclude_dir in exclude:
        if exclude_dir in dir_name:
            dont_care = True
    if dont_care:
        continue

    for file_name in file_list:
        if not file_name.endswith(".jsb"):
            continue
        file_path = os.path.join(dir_name, file_name)
        data_all = load(file_path)

        output_txt = "".join(file_name.split(".")[:-1])
        output_txt = dir_name.replace("/", "_") + "_" + output_txt
        output_txt = os.path.join(output_dir, output_txt + ".txt")

        with open(output_txt, "w") as wf:
            count = 0
            keys = find_key(data_all)
            for key in keys:
                if count % 1000 == 0:
                    wf.write("\n")
                wf.write(key)
                count += 1
