import json

INPUT_FILE = "input.csv"
NEW_LINE = "\n"
with open(INPUT_FILE) as file:
    lines_number = sum(1 for line in file) - 1


def csv_to_dicts(input_file, delimiter=",", new_line="\n") -> list[dict]:
    with open(input_file, "r") as in_f:
        headers = in_f.readline().replace(new_line, "").split(delimiter)
        for line in in_f:
            yield dict(zip(headers, line.replace(new_line, "").split(delimiter)))


indent = " "
line_count = 0
with open("output.json", 'w') as dst:
    dst.write("[" + NEW_LINE)  # first row in file
    for record in csv_to_dicts(INPUT_FILE):  # for each row in csv
        dst.write(indent + "{" + NEW_LINE)  # start json record
        for key, value in record.items():
            dst.write(f'{indent}{indent}"{key}": {value}')
            if key == list(record.keys())[-1]:
                dst.write(NEW_LINE)
            else:
                dst.write(',' + NEW_LINE)
        dst.write(indent + "}")  # end json record
        line_count += 1
        if line_count == lines_number:
            dst.write(NEW_LINE)
        else:
            dst.write(',' + NEW_LINE)
    dst.write("]")  # last row in file


# Но есть ощущение, что задание предполагает именно создание списка словарей,
# то есть следующий вариант
# list_dict = []
# for record in csv_to_list_dict(INPUT_FILE):
#     list_dict.append(record)
#
# print(json.dumps(list_dict, indent=4))

# Может я ещё какую-то хитрость упустил, чтобы обойти эту условность с созданием списка
# В любом случае, благодарю Вас за знакомство с концепцией генераторов, так как в курсе о них
# на данный момент ни слова, а дальнейшие темы как будто им уже посвящены не будут.
