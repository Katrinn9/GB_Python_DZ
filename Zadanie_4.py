# Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stopping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Speed:', self.speed)

class TownCar(Car):
    def show_speed(self):
        print('Speed:', self.speed)
        if self.speed > 60:
            print('Внимание! Превышение скорости')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('Speed:', self.speed)
        if self.speed > 40:
            print('Внимание! Превышение скорости')


class PoliceCar(Car):
    pass

town_car = TownCar(59, 'Синяя', 'Городская машина', False)
sport_car = SportCar(210, 'Белая', 'Спортивная машина', False)
work_car = WorkCar(50, 'Серая', 'Рабочая машина', False)
police_car = PoliceCar(180, 'Черно-белая', 'Полицесйкая машина', True)

town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()