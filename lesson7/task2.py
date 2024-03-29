"""
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    _mass = 25
    _depth = 0.05

    def __init__(self, length_road, width_road):
        self._length_road = length_road
        self._width_road = width_road

    def mass_calc(self):
        asph_mass = self._length_road * self._width_road * \
                    self._mass * self._depth
        return asph_mass


res = Road(5000, 20)
print(f'Масса асфальта,необходимого для покрытия всего дорожного полотна равна'
      f' {res.mass_calc()/1000} т.')