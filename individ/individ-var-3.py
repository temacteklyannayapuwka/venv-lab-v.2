#!/usr/bin/env python 3
# –*– coding: utf–8 –*–

# Открываем файл для чтения
with open("file-var-3.txt", "r", encoding="utf-8") as fileptr:
    # Читаем файл построчно
    for line in fileptr:
        # Используем регулярное выражение для поиска двузначных чисел
        import re

        numbers = re.findall(r'\b\d{2}\b', line)

        # Если найдены двузначные числа в строке, выводим строку
        if numbers:
            print(line.strip())  # Убираем лишние пробелы и символы перевода строки
