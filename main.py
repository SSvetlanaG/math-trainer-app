from modules import arithmetic
from modules import matrices
from modules import stats

def main():
    print("=== ДОБРО ПОЖАЛОВАТЬ В МАТЕМАТИЧЕСКИЙ ТРЕНАЖЕР ===")
    # Запрашиваем имя один раз при старте программы
    username = input("Введите ваше имя: ").strip()
    
    # Если пользователь ничего не ввел, даем имя по умолчанию
    if not username:
        username = "Игрок"

    while True:
        print(f"\n=== МАТЕМАТИЧЕСКИЙ ТРЕНАЖЕР (Пользователь: {username}) ===")
        print("1. Арифметика (числа)")
        print("2. Матрицы (сумма, умножение)")
        print("3. Посмотреть статистику")
        print("0. Выход")
        
        choice = input("\nВыберите раздел: ")
        
        if choice == "1":
            score = arithmetic.start_trainer()
            # Передаем реальное имя вместо строки "Игрок"
            stats.save_result(username, score) 
            
        elif choice == "2":
            score = matrices.start_trainer()
            # Передаем реальное имя вместо строки "Игрок"
            stats.save_result(username, score)

        elif choice == "3":
            stats.show_stats()
            
        elif choice == "0":
            print("Программа завершена. Удачи!")
            break
            
        else:
            print("Ошибка! Выберите пункт из списка.")

if __name__ == "__main__":
    main()
