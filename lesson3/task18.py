"""Требуется найти в массиве A[1..N] самый близкий по величине элемент к
заданному числу X. Пользователь в первой строке вводит натуральное число
N – количество элементов в массиве. В последующих  строках записаны N целых
чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""
N = int(input('Введите количество элементов в массиве: '))
entered_list = input('Введите числа через пробел ').split()
ent_list = list(map(int, entered_list))
print(entered_list)
if len(ent_list) == N:
    X = int(input('Какое число необходимо сравнить? '))
    difference = abs(X - ent_list[0])
    index = 0
    for i in range(1, N):
        count = abs(X - ent_list[i])
        if count < difference:
            difference = count
            digit = ent_list[i]
    print(
        f'Число {digit} в списке наиболее близко по величине к числу {X}.')
else:
    print('Количество элементов не соответсвует N')