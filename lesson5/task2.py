"""Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)"""


def count_ev_odd(n, c_event, c_odd):
    if n % 10 == 0:
        return print(f'Количество четных цифр - {c_event} '
                     f'\nКоличество нечетных цифр - {c_odd}')
    else:
        if n % 10 % 2 == 0:
            count_ev_odd(n // 10, c_event + 1, c_odd)
        else:
            count_ev_odd(n // 10, c_event, c_odd + 1)


digit = int(input('Введите натаральное число: '))
count_ev_odd(digit, 0, 0)