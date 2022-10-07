BYTES_ONE_CHAR = 1  # размер одного символа в байтах
# никаких магических чисел
pages = 100
lines = 50  # TODO ввести количество строк
chars = 25  # TODO ввести количество символов в строке

total_chars = pages * lines * chars  # TODO общее количество символов в книге
total_bytes = BYTES_ONE_CHAR * total_chars  # TODO размер одной книги в байтах

disk_size = 1.44 * 1024 ** 2
books = disk_size // total_bytes
print(books)  # TODO найти количество книг, которое поместится на дискете
