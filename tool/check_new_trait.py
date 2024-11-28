import csv
import json

update_file = "data/fm engine change - fm24.csv"
released_file = "data/fm20 json/physical_constraints fm20 완전한자유-speed.json"

update = csv.reader(open(update_file, "r", encoding="utf-8"))
update = [row for row in update]
released = json.load(open(released_file, "r"))

fm24_keys = set()
pre_keys = set()
for i in range(len((released["version_array"])) - 1, -1, -1):
    data = released["version_array"][i]
    for pre_key in data.keys(): pre_keys.add(pre_key)

    for j, row in enumerate(update):
        key, before = row
        fm24_keys.add(key)
        if key in data:
            after = str(data[key])
            update[j][1] = after

print("disappeared")
print(pre_keys - fm24_keys, "\n")

print("new")
print(fm24_keys - pre_keys)

with open(released_file.replace(".json", ".csv"), "w") as wf:
    writer = csv.writer(wf)
    writer.writerows(update)
