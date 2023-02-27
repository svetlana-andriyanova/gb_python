"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
"""

N = int(input('Введите количество монет '))
eagle = 0
tails = 0
for i in range(N):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        eagle += 1
    else:
        tails += 1
if eagle < tails:
    print(f'Переверните {eagle} монет с орла на решку, их меньше всего')
elif eagle == tails:
    print(f'Количество орлов и решек одинаково, по {eagle} штук')
else:
    print((f'Переверните {tails} монет с решки на орла, их меньше всего'))
