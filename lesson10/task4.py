"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

list_words = ['разработка', 'администрирование', 'protocol', 'standard']
for line in list_words:
    word_bytes = line.encode('utf-8')
    print(f'В байтовом представлении: {word_bytes}')
    print(f'Тип: {type(word_bytes)}')
    word_str = bytes.decode(word_bytes, 'utf-8')
    print(f'В строковом представлении: {word_str} \n')