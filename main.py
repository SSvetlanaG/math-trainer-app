import modules.arithmetic as arithmetic
import modules.matrices as matrices

def main():
    while True:
        print("\n=== МАТЕМАТИЧЕСКИЙ ТРЕНАЖЕР ===")
        print("1. Арифметика (числа)")
        print("2. Матрицы (сумма, умножение)")
        print("0. Выход")

        choice = input("\nВыберите раздел: ")

        if choice == "1":
            print("\nПереходим в модуль арифметики...")
            # Здесь позже вызовем функцию: arithmetic.start_trainer()
        elif choice == "2":
            print("\nПереходим в модуль матриц...")
            # Здесь позже вызовем функцию: matrices.start_trainer()
        elif choice == "0":
            print("Программа завершена. Удачи!")
            break
        else:
            print("Ошибка! Выберите пункт из списка.")

if __name__ == "__main__":
    main()
