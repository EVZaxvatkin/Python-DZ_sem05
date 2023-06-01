#1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def divine_path(full_path: str):
    def divine(abs_path: str, div: str) -> tuple:
        abs_path = abs_path.split(div)
        file_name, extension = abs_path[-1].split('.')
        path = div.join(abs_path[:-1])
        return path, file_name, extension

    return divine(full_path, '/') if '/' in full_path else divine(full_path, '\\')


print(divine_path())

#2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
#имена str, ставка int, премия str с указанием процентов вида “10.25%”.
#В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#Сумма рассчитывается как ставка умноженная на процент премии

def premium(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
    return {name: money / 100 * perc
            for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}


#3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonachi(limit: int):
    fibo = [0, 1]
    while limit > 0:
        yield fibo[-1]
        fibo.append(fibo[-1] + fibo[-2])
        limit -= 1


for number in fibonachi(10):
    print(number)