from modules import arithmetic
from modules import matrices
from modules import stats

def main():
    while True:
        print("\n=== МАТЕМАТИЧЕСКИЙ ТРЕНАЖЕР ===")
        print("1. Арифметика (числа)")
        print("2. Матрицы (сумма, умножение)")
        print("3. Посмотреть статистику") # Новый пункт
        print("0. Выход")
        
        choice = input("\nВыберите раздел: ")
        
        if choice == "1":
            print("\n[В разработке: Модуль Нины]")
        elif choice == "2":
            print("\n[В разработке: Модуль Даниила]")
        elif choice == "3":
            stats.show_stats() # Вызов функции из модуля stats.py
        elif choice == "0":
            print("Программа завершена. Удачи!")
            break
        else:
            print("Ошибка! Выберите пункт из списка.")

if __name__ == "__main__":
    main()
