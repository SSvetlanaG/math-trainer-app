def save_result(username, score):
    """Сохраняет имя пользователя и его баллы в файл."""
    with open("statistics.txt", "a", encoding="utf-8") as file:
        file.write(f"Игрок: {username} | Баллы: {score}\n")
    print(f"Результат {username} сохранен!")

def show_stats():
    """Читает и выводит всю статистику."""
    try:
        with open("statistics.txt", "r", encoding="utf-8") as file:
            print("\n--- ТАБЛИЦА РЕКОРДОВ ---")
            print(file.read())
    except FileNotFoundError:
        print("Статистика пока пуста.")
