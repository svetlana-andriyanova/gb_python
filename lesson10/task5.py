"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def ping_web(sites):
    for site in sites:
        args = ['ping', site]
        proc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in proc_ping.stdout:
            enc_site = chardet.detect(line)
            print(line.decode(enc_site['encoding']))


ping_web(['yandex.ru', 'youtube.com'])