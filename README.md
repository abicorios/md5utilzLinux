# md5utilzLinux
Утилиты для обмена информацией о дереве каталогов. Запись информации о дереве каталогов в csv-файл, и упорядочивание каталогов в соответствии с информацией из csv-файла. Порт утилит https://github.com/abicorios/md5utilz с Windows на Linux.
# Зависимости
Утилиты зависят от порта архиватора 7zip на Linux [p7zip](http://p7zip.sourceforge.net/) и библиотеки обработки данных [pandas](https://pandas.pydata.org/). В системах произошедших от Linux Debian можно использовать команду
```
sudo apt install p7zip-full p7zip-rar python3-pandas
```
В других системах вместо apt может быть другой менеджер пакетов, имена пакетов могут несколько отличаться. Используйте поиск пакетов в соотвествии с вашей системой.
# Разработка
Использовался язык [Python (v3.6)](https://www.python.org/), дистрибутив библиотек [Miniconda3](https://conda.io/miniconda.html), текстовый редактор [Vim](https://www.vim.org/), система контролся версий [Git](https://git-scm.com/).
