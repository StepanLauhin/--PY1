import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_file, delimiter=",", new_line="\n") -> list[dict]:
    with open(input_file, "r") as in_f:
        headers = in_f.readline().replace(new_line, "").split(delimiter)
        for line in in_f:
            yield dict(zip(headers, line.replace(new_line, "").split(delimiter)))


# Ваша версия, если я Вас правильно понял
# for record in csv_to_list_dict(INPUT_FILE):
#     print(json.dumps(record, indent=4))


# Но есть ощущение, что задание предполагает именно создание списка словарей,
# то есть следующий вариант
list_dict = []
for record in csv_to_list_dict(INPUT_FILE):
    list_dict.append(record)

print(json.dumps(list_dict, indent=4))

# Может я ещё какую-то хитрость упустил, чтобы обойти эту условность с созданием списка
# В любом случае, благодарю Вас за знакомство с концепцией генераторов, так как в курсе о них
# на данный момент ни слова, а дальнейшие темы как будто им уже посвящены не будут.
