'''Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать публичные методы получения полного имени
сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position
передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __str__(self):
        return f'Полное имя: {self.surname} {self.name}'

    def total_income(self):
        return self._income.get('wage') + self._income.get('wage') * \
            (self._income.get('bonus') / 100)


worker_1 = Position('Иван', 'Иванов', 'Менеджер', 30000, 25)
print('Имя:', worker_1.name)
print('Фамилия:', worker_1.surname)
print('Должность:', worker_1.position)
print(worker_1)
print('Размер дохода:', worker_1.total_income())