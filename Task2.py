# TODO Найдите количество книг, которое можно разместить на дискете

information_volume = 1.44  # информационный объем дискеты, равный 1,44 Мб
pages_in_the_book = 100  # Количество страниц в книге
lines_per_page = 50  # Число строк на странице
characters_per_line = 25  # Количество символов в строке
symbol = 4  # Для хранения кода одного символа нужно 4 байта.

page_in_Mb = round((characters_per_line * lines_per_page * 4) / 1024 * 1024, 4)
# строки умножаем на кол-во символов и умножаем на размер 1 символа в байтах

book_in_Mb = page_in_Mb * pages_in_the_book
volume_book = information_volume / book_in_Mb
volume_book = int(volume_book)

print("Количество книг, помещающихся на дискету:", volume_book)
