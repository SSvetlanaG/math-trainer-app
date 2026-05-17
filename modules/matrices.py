import random

def start_trainer():
    print("\n--- ТРЕНАЖЕР: МАТРИЦЫ ---")
    print("Для выхода в меню ничего не вводите и просто нажмите Enter\n")
    
    score = 0  # Счётчик правильных ответов
    
    while True:  # Бесконечный цикл — можно решать много примеров
        # Случайный выбор операции: 0 - сложение, 1 - вычитание, 2 - умножение на число
        operation = random.randint(0, 2)
        
        # Генерация первой матрицы 2x2
        m1 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
        
        # Вывод первой матрицы
        print(f"\nМатрица A:")
        print(f"{m1[0][0]} {m1[0][1]}")
        print(f"{m1[1][0]} {m1[1][1]}")
        
        if operation == 0:  # Сложение
            m2 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
            print(f"\nМатрица B:")
            print(f"{m2[0][0]} {m2[0][1]}")
            print(f"{m2[1][0]} {m2[1][1]}")
            print(f"\nВычислите: A + B")
            
            result = [
                [m1[0][0] + m2[0][0], m1[0][1] + m2[0][1]],
                [m1[1][0] + m2[1][0], m1[1][1] + m2[1][1]]
            ]
            
        elif operation == 1:  # Вычитание
            m2 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
            print(f"\nМатрица B:")
            print(f"{m2[0][0]} {m2[0][1]}")
            print(f"{m2[1][0]} {m2[1][1]}")
            print(f"\nВычислите: A - B")
            
            result = [
                [m1[0][0] - m2[0][0], m1[0][1] - m2[0][1]],
                [m1[1][0] - m2[1][0], m1[1][1] - m2[1][1]]
            ]
            
        else:  # Умножение на число
            scalar = random.randint(2, 5)
            print(f"\nУмножьте матрицу A на число {scalar}")
            
            result = [
                [m1[0][0] * scalar, m1[0][1] * scalar],
                [m1[1][0] * scalar, m1[1][1] * scalar]
            ]
        
        print("\nВведите 4 числа (результат) через пробел:")
        user_input = input("Ваш ответ: ").strip()
        
        # Выход, если пользователь ничего не ввёл
        if user_input == "":
            print(f"\nВыход из тренажёра. Всего набрано баллов: {score}")
            return score
        
        parts = user_input.split()
        
        # Проверка, что введено 4 числа
        if len(parts) != 4:
            print("❌ Ошибка! Нужно ввести ровно 4 числа через пробел.")
            continue
        
        try:
            user_numbers = [int(x) for x in parts]
            
            # Сравнение всех 4 чисел
            if (user_numbers[0] == result[0][0] and
                user_numbers[1] == result[0][1] and
                user_numbers[2] == result[1][0] and
                user_numbers[3] == result[1][1]):
                print("✅ Верно!")
                score += 1  # Увеличиваем счётчик
            else:
                print("❌ Ошибка!")
                print(f"Правильный ответ:")
                print(f"{result[0][0]} {result[0][1]}")
                print(f"{result[1][0]} {result[1][1]}")
        except ValueError:
            print("❌ Ошибка! Введите только числа, разделённые пробелами.")
            print("Пример: 4 7 5 5")