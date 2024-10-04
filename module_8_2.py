

def personal_sum(numbers):

        result_ = 0
        incorrect_data = 0
        for i in numbers:
            try:
                result_ = result_ + i
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
        return (result_, incorrect_data)

def calculate_average(numbers):
    try:
        sum = personal_sum(numbers)
        sum_ = sum[0]
        div = 0
        for k in numbers:
            if type(k) is int or type(k) is float:
                div = div + 1
        media = sum_ / div
        return media
    except ZeroDivisionError:
        media = 0
        return media
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать






