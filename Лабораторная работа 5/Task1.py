# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
last_number = 15
list_of_dictionaries = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(last_number + 1)]
pprint(list_of_dictionaries)
