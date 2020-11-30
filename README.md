# Problem2
## Web-service

<br>new_file_gen.py - генератор файлов
<br>app.py - соновной исполняемый файл
<br>Реализовано на фреймворке Flask

## Описание
<br>Генерируются несколько файлов большого размера (порядка 1гб.) содержащий целые числа разделенные запятыми (new_file_gen.py). 
<br>Далее запускается файл app.py:
 
<br>Запрос к серверу для поиска значения и записи результатов:
 * В поисковую строку браузера вводится `http://127.0.0.1:5000/`, где после `/` вводится значение для поиска
<br>В этот момент происходит поиск в папке фсех файлов с расширением `.txt`. Формируется список найденных имен файлов, открывается каждый из файлов, считается кол-во найденных совпадений в файле, записывается в словарь в поля `name` и `volumes`, имя файла и кол-во найденых вхождений соответственно.
<br> По окончанию поиска выведет список из пар `name, volume` для каждого файла.
