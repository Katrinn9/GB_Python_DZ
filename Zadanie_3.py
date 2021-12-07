# Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname =surname
        self.position = position
        self._income_salary = income['salary']
        self._income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'
    def get_full_income(self):
        return self._income_salary + self._income_bonus

position = Position('Ekaterina', 'Kozlyakova', 'junior', {"salary": 50000, "bonus": 90000})
print(position.get_full_name())
print(position.get_full_income())