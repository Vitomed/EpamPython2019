import os
import os.path

def list_of_dicts_json(dictionary: list) -> str:
    string_json = str(dictionary)
    replaces = (("[{'", '[{"', 1), ("'}]", '"}]', 1), ("': '", '": "'), ("', '", '", "'),
                ("'}, {'", '"}, {"'), ("': {'", '": {"'), ("}, '", '}, "'), ("'}", '"}'), ("\\'", "'"),
                ("': ", '": '), (", '", ', "'), ("'\"", '"'), ("\"'", "\""), ('""', '"'), ("\\\\", "\\"))
    for replace in replaces:
        string_json = string_json.replace(*replace)
    return string_json

def count_most(filtered_list: list, attr: str, sum_attr: str = None) -> tuple:
    sum_map, count_map = {}, {}
    if not sum_attr:
        for entry in filtered_list:
            try:
                if entry[attr] != 'null':
                    sum_map[entry[attr]] += 1
            except KeyError:
                sum_map[entry[attr]] = 1
    else:
        for entry in filtered_list:
            try:
                if entry[attr] != 'null' and entry[sum_attr] != 'null':
                    sum_map[entry[attr]] += int(entry[sum_attr].replace('"', ''))
                    count_map[entry[attr]] += 1
            except KeyError:
                count_map[entry[attr]], sum_map[entry[attr]] = 1, 1
        for key in count_map.keys():
            sum_map[key] = sum_map[key] / count_map[key]
    return max(sum_map, key=lambda k: sum_map[k]), min(sum_map, key=lambda k: sum_map[k])

def unique_dict(list_of_dicts: list) -> list:
    return [dict(s) for s in set(tuple(d.items()) for d in list_of_dicts)]


def get_data_from_file(name: str) -> str:
    with open(os.path.join(path, f"./files/{name}"), 'r') as file_r:
        return file_r.read()


def write_to_file(name: str, string: str):
    with open(os.path.join(path, f"./files/{name}"), 'w') as file_w:
        file_w.write(string)


