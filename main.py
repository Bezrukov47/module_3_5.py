# Распаковка позиционных параметров
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции
print_params()  # Вывод: 1 строка True
print_params(10)  # Вывод: 10 строка True
print_params(b=25)  # Вывод: 1 25 True
print_params(c=[1, 2, 3])  # Вывод: 1 строка [1, 2, 3]

# Распаковка параметров
values_list = [3.14, 'текст', False]
values_dict = {'a': 42, 'b': 'слово', 'c': None}

print_params(*values_list)  # Вывод: 3.14 текст False
print_params(**values_dict)  # Вывод: 42 слово None

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Вывод: 54.32 Строка 42