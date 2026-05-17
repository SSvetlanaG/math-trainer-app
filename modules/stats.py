def save_result(username, score):
    """Сохраняет имя пользователя и его баллы в файл."""
    with open("statistics.txt", "a", encoding="utf-8") as file:
        # Сохраняем только чистые данные через двоеточие
        file.write(f"{username}:{score}\n")
    print(f"Результат {username} ({score} б.) успешно сохранен!")

def show_stats():
    """Читает и красиво выводит всю статистику."""
    try:
        with open("statistics.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            
            print("\n   --- ТАБЛИЦА РЕКОРДОВ ---")
            print(f"{'Имя игрока':<20} | {'Баллы':<5}")
            print("-" * 32)
            
            for line in lines:
                if ":" in line:
                    # Разделяем имя и баллы, убирая символы переноса строки
                    name, score = line.strip().split(":", 1)
                    print(f"{name:<20} | {score:<5}")
    except FileNotFoundError:
        print("Статистика пока пуста.")
