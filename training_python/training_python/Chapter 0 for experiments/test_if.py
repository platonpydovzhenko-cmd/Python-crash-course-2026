age = 18.5

if age < 13:
    print("Ты еще ребенок.")
elif age < 18:
    print("Ты подросток.")
elif age == 18:
    print("Тебе только что исполнилось 18!")
else:
    print("Ты взрослый человек.")
print("--------------------------------------------------------")
is_macos = False
has_python = True

if is_macos or has_python:
    print("Система готова к разработке!")
print("--------------------------------------------------------")
brand = "Android"
model = "MacBook Air"
model = "phone"
if brand == "Apple":
    if model == "MacBook Air":
        print("Легкий и компактный ноутбук.")
    else:
        print("Другое устройство Apple.")
if brand == "Android":
    if model == "MacBook Air":
        print("Легкий и компактный телефон.")
    else:
        print("Другое устройство Android")
print("--------------------------------------------------------")
car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("--------------------------------------------------------")
laptop = 'macbook'
anime = 'Naruto'
language = 'Python'
age = 14

# Тест 1: Проверка равенства (True)
print("Is laptop == 'macbook'? I predict True.")
print(laptop == 'macbook')

# Тест 2: Проверка на неравенство (True)
print("\nIs laptop != 'windows'? I predict True.")
print(laptop != 'windows')

# Тест 3: Проверка с учетом регистра (False)
print("\nIs anime == 'naruto'? I predict False.")
print(anime == 'naruto') # Python чувствителен к регистру (N vs n)

# Тест 4: Сравнение чисел (True)
print("\nIs age == 14? I predict True.")
print(age == 14)

# Тест 5: Логическое сравнение (False)
print("\nIs language == 'Java'? I predict False.")
print(language == 'Java')

# Тест 6: Использование метода .lower() (True)
print("\nIs anime.lower() == 'naruto'? I predict True.")
print(anime.lower() == 'naruto')

# Тест 7: Математическое неравенство (False)
print("\nIs age > 20? I predict False.")
print(age > 20)

# Тест 8: Проверка вхождения (True)
print("\nIs 'Py' in language? I predict True.")
print('Py' in language)

# Тест 9: Проверка типа данных (False)
print("\nIs age == '14'? I predict False.")
print(age == '14') # Число 14 не равно строке '14'

# Тест 10: Сравнение строк (False)
print("\nIs laptop == 'air'? I predict False.")
print(laptop == 'air')
print("--------------------------------------------------------")
# Наши данные
names = ['titan', 'naruto']
items = ['titan', 'naruto', 80, 14]

# Наш "переключатель" (флаг)
has_numbers = False

print("--- Обработка списка ---")

for item in items:
    if item in names:
        # 1. Текстовое действие (глава 5, проверка вхождения в список)
        print(f"Это текст: {item.title()}")
    else:
        # 2. Если это не текст из списка names, значит это число
        print(f"Найдено число: {item}")
        has_numbers = True

# Финальное действие после цикла (проверка условия)
if has_numbers == True:
    print("\n--- Числа найдены! Выполняем математику ---")
    
    # Первое действие
    sum_result = 50 + 50
    print(f"Результат сложения: {sum_result}")
    
    # Второе действие (один раз в конце)
    power_result = 10 * 10
    print(f"Результат умножения: {power_result}")
print("--------------------------------------------------------")
names = [30, 53, 67, 944, 35, 564, 832]
for name in names:
    print(name == name)
    print(name <= name)
    print(name >= name)
    print(name != name)
