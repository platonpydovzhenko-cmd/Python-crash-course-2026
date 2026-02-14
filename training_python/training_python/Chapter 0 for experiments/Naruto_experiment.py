# --- ПРОГРАММА: СПИСОК ШИНОБИ (ГЛАВЫ 1-4) ---

shinobi_list = ['Naruto', 'Sasuke', 'Sakura']

shinobi_list.append('Kakashi')
shinobi_list.insert(0, 'Itachi')

print("1. Список в алфавитном порядке (временно):")
print(sorted(shinobi_list))

print("\n2. Список после постоянной сортировки (Z-A):")
shinobi_list.sort(reverse=True)
print(shinobi_list)

print("\n3. Рассылка заданий для каждого шиноби:")

for ninja in shinobi_list:
    # Начало цикла
    task = f"Шиноби {ninja}, вам назначена миссия ранга S!"
    print(task)
    
    status = f"Команда №7 ожидает прибытия {ninja} на тренировочную площадку."
    print(status)
    print("--- Задание передано ---")
    # Конец цикла

print("\n4. Итог подготовки:")
print(f"Всего в отряде: {len(shinobi_list)} сильнейших ниндзя.")
print("Деревня Скрытого Листа в безопасности.")
