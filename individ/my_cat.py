  Индивидуальные задания
  Задание 2 Вариант 3

Продолжаем тему операционных систем на базе Unix, в которых обычно также есть утилита
с названием cat, что является сокращением от concatenate (сцепить). Эта утилита выводит
на экран объединенное содержимое нескольких файлов, имена которых передаются ей в
качестве аргументов командной строки. При этом файлы сцепляются в том порядке, в
котором указаны в аргументах. Напишите программу на Python, имитирующую работу этой
утилиты. В процессе работы программа должна выдавать сообщения о том, какие файлы
открыть не удается, и переходить к следующим файлам. Если программа была запущена
без аргументов командной строки, на экран должно быть выведено соответствующее
сообщение об ошибке.

#!/usr/bin/env python 3
# –*– coding: utf–8 –*–

import sys

def cat_files(file_names):
    for file_name in file_names:
        try:
            with open(file_name, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Skipping...")
        except Exception as e:
            print(f"An error occurred while reading '{file_name}': {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py file1 file2 ...")
    else:
        file_names = sys.argv[1:]
        cat_files(file_names)
