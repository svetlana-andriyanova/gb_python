"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv
import re


def write_to_csv(file, data):
    with open(file, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)


def get_data(list_files):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС',
                  'Код продукта', 'Тип системы']]
    for f in list_files:
        data_in_file = open(f, 'r')
        for row in data_in_file:
            if re.search(r'(Изготовитель системы).\s*(.*)', row):
                os_prod_list.append(
                    re.search(r'(Изготовитель системы).\s*(.*)', row).group(2))
            elif re.search(r'(Название ОС).\s*(.*)', row):
                os_name_list.append(
                    re.search(r'(Название ОС).\s*(.*)', row).group(2))
            elif re.search(r'(Код продукта).\s*(.*)', row):
                os_code_list.append(
                    re.search(r'(Код продукта).\s*(.*)', row).group(2))
            elif re.search(r'(Тип системы).\s*(.*)', row):
                os_type_list.append(
                    re.search(r'(Тип системы).\s*(.*)', row).group(2))
    for i in range(len(list_files)):
        main_data.append([os_prod_list[i], os_name_list[i],
                          os_code_list[i], os_type_list[i]])
    return main_data


write_to_csv('result.csv',
             get_data(['info_1.txt', 'info_2.txt', 'info_3.txt']))
with open('result.csv') as f_n:
    print(f_n.read())