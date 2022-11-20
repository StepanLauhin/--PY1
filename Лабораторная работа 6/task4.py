import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_file, delimeter=",", new_line="\n") -> list[dict]:
    with open(input_file, "r") as in_f:
        headers = in_f.readline().rstrip().split(delimeter)
        file_data = []
        for line in in_f:
            file_data.append(line.rstrip().split(delimeter))
        list_dict = []
        for line in file_data:
            list_dict.append({headers[i]: data for i, data in enumerate(line)})
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
