
class IncorrectVinNumber(Exception) :
    def __init__(self, message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message
class Car():
    def __init__(self,model,vin,numbers):
        self.model = model
        self.__vin__ = self.__is_valid_vin__(vin)
        self.__numbers__ = self.__is_valid_numbers__(numbers)
    def __is_valid_vin__(self,vin_number):
        if isinstance(vin_number,int) and 1000000 <= vin_number <= 9999999:
            return True
        elif not isinstance(vin_number,int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number < 1000000 or  vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')


    def __is_valid_numbers__(self,numbers):
        if isinstance(numbers, str) and len(numbers) == 6:
            return True
        elif not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')


try:
    first = Car('Model1', "1000000", 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    first = Car('Model3', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model4', 3000000, 123456)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model5', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
