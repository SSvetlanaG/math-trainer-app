def save_result(username, score):
    """Сохраняет имя пользователя и его баллы в файл (суммирует баллы для одного имени)."""
    records = {}
    
    # Сначала читаем все существующие записи
    try:
        with open("statistics.txt", "r", encoding="utf-8") as file:
            for line in file:
                if ": " in line:
                    name, points = line.strip().split(": ", 1)
                    records[name] = records.get(name, 0) + int(points)
    except FileNotFoundError:
        pass  # Файла пока нет, создадим новый
    
    # Добавляем новый результат к существующему
    records[username] = records.get(username, 0) + score
    
    # Перезаписываем файл с обновлёнными данными
    with open("statistics.txt", "w", encoding="utf-8") as file:
        for name, points in records.items():
            file.write(f"{name}: {points}\n")
    
    print(f"Результат {username} ({score} б.) успешно сохранен!")

def show_stats():
    """Читает и красиво выводит всю статистику."""
    try:
        with open("statistics.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        print("\n--- ТАБЛИЦА РЕКОРДОВ ---")
        print(f"{'Имя игрока':<20} | {'Баллы':<5}")
        print("-" * 32)
        
        for line in lines:
            if ": " in line:
                name, score = line.strip().split(": ", 1)
                print(f"{name:<20} | {score:<5}")
    
    except FileNotFoundError:
        print("Статистика пока пуста.")
