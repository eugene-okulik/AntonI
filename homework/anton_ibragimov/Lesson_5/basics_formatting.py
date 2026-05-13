# Задание 1: Распаковка
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(f"Name: {name}, Last Name: {last_name}, City: {city}, Phone: {phone}, Country: {country}")

print("-" * 30)

# Задание 2: Срезы и индексы
# Строка 1
line = "результат операции: 42"
index = line.index(':')
print(int(line[index + 2:]) + 10)

# Строка 2
line = "результат операции: 514"
index = line.index(':')
print(int(line[index + 2:]) + 10)

# Строка 3
line = "результат работы программы: 9"
index = line.index(':')
print(int(line[index + 2:]) + 10)

print("-" * 30)

# Задание 3: Форматирование списков
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_str = ", ".join(students)
subjects_str = ", ".join(subjects)

print(f"Students {students_str} study these subjects: {subjects_str}")
