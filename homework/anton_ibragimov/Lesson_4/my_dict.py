import pprint

from typing import Any, Dict

# 1. Создаем словарь my_dict
my_dict: Dict[str, Any] = {
    'tuple': (10, 20, 30, 40, 50, 60),
    'list': ['apple', 'banana', 'cherry', 'date', 'elderberry'],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5, 6, 7}
}

# 2. Действия с элементами

# Для 'tuple': выводим последний элемент
print("Последний элемент кортежа:", my_dict['tuple'][-1])

# Для 'list':
my_dict['list'].append('fig')  # Добавляем в конец
my_dict['list'].pop(1)  # Удаляем второй элемент ('banana')

# Для 'dict':
# Добавляем элемент с ключом-кортежем
my_dict['dict'][('i am a tuple',)] = 'New Value'

# Удаляем элемент по ключу 'а'
my_dict['dict'].pop('a')

# Для 'set':
my_dict['set'].add(100)  # Добавляем элемент
my_dict['set'].discard(1)  # Удаляем элемент 1

# 3. Вывод итогового словаря
print("\nИтоговый словарь:")
pprint.pprint(my_dict)
