"""
Задание 2.
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов не используя!!!
методы encode и decode) и определить тип, содержимое и длину соответствующих
переменных.
Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

list_byte = [b'class', b'function', b'method']

for line in list_byte:
    print(f'Содержание: {line}')
    print(f'Тип: {type(line)}')
    print(f'Длина: {len(line)}\n')