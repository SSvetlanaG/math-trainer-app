from modules import arithmetic
from modules import matrices
from modules import stats
from modules import quadratic  # ДОБАВЛЕНО: импорт нового модуля

def main():
    print("=== ДОБРО ПОЖАЛОВАТЬ В МАТЕМАТИЧЕСКИЙ ТРЕНАЖЕР ===")
    username = input("Введите ваше имя: ").strip()

    if not username:
        username = "Игрок"

    while True:
        print(f"\n=== МАТЕМАТИЧЕСКИЙ ТРЕНАЖЕР (Пользователь: {username}) ===")
        print("1. Арифметика (числа)")
        print("2. Матрицы (сложение, вычитание, умножение на число)")
        print("3. Посмотреть статистику")
        print("4. Квадратные уравнения")  # ДОБАВЛЕНО: новый пункт меню
        print("0. Выход")

        choice = input("\nВыберите раздел: ")

        if choice == "1":
            score = arithmetic.start_trainer()
            stats.save_result(username, score)

        elif choice == "2":
            score = matrices.start_trainer()
            stats.save_result(username, score)

        elif choice == "3":
            stats.show_stats()

        elif choice == "4":  # ДОБАВЛЕНО: обработка нового пункта
            score = quadratic.start_trainer()
            stats.save_result(username, score)

        elif choice == "0":
            print("Программа завершена. Удачи!")
            break

        else:
            print("Ошибка! Выберите пункт из списка.")

if __name__ == "__main__":
    main()
