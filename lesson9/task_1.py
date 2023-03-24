"""
Реализовать дескрипторы
"""


class NonString:

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError("Имя/фамилия/должность должны быть строкой.")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = NonString()
    surname = NonString()
    position = NonString()
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


worker_1 = Position('Иван', 'Иванов', 789, 30000, 25)
print('Имя:', worker_1.name)
print('Фамилия:', worker_1.surname)
print('Должность:', worker_1.position)
print(worker_1)
print('Размер дохода:', worker_1.total_income())