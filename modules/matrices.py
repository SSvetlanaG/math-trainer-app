import random

def start_trainer():
    # Случайно выбираем операцию: 0 - сложение, 1 - вычитание, 2 - умножение на число
    operation = random.randint(0, 2)
    
    # Генерация двух случайных матриц 2x2 (для умножения на число вторая не понадобится)
    m1 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
    m2 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
    
    # Для умножения на число генерируем случайное число от 2 до 5
    scalar = random.randint(2, 5)
    
    # Показываем условие в зависимости от операции
    print("\n--- ТРЕНАЖЕР: МАТРИЦЫ ---")
    print("Матрица A:")
    print(f"{m1[0][0]} {m1[0][1]}")
    print(f"{m1[1][0]} {m1[1][1]}")
    
    if operation == 0:  # Сложение
        print("\nМатрица B:")
        print(f"{m2[0][0]} {m2[0][1]}")
        print(f"{m2[1][0]} {m2[1][1]}")
        print(f"\nВычислите: A + B")
        
        # Правильный ответ
        result = [
            [m1[0][0] + m2[0][0], m1[0][1] + m2[0][1]],
            [m1[1][0] + m2[1][0], m1[1][1] + m2[1][1]]
        ]
        
    elif operation == 1:  # Вычитание
        print("\nМатрица B:")
        print(f"{m2[0][0]} {m2[0][1]}")
        print(f"{m2[1][0]} {m2[1][1]}")
        print(f"\nВычислите: A - B")
        
        # Правильный ответ
        result = [
            [m1[0][0] - m2[0][0], m1[0][1] - m2[0][1]],
            [m1[1][0] - m2[1][0], m1[1][1] - m2[1][1]]
        ]
        
    else:  # Умножение на число (operation == 2)
        print(f"\nУмножьте матрицу A на число {scalar}")
        
        # Правильный ответ
        result = [
            [m1[0][0] * scalar, m1[0][1] * scalar],
            [m1[1][0] * scalar, m1[1][1] * scalar]
        ]
    
    # Просим ввести ответ
    print("\nВведите 4 числа (результат) через пробел:")
    print("(Первая строка: два числа, пробел, вторая строка: два числа)")
    
    user_input = input("Ваш ответ: ")
    parts = user_input.split()
    
    # Проверяем, что введено ровно 4 числа
    if len(parts) != 4:
        print("❌ Ошибка! Нужно ввести ровно 4 числа через пробел.")
        return 0
    
    try:
        user_numbers = [int(x) for x in parts]
        
        # Сравниваем все 4 числа
        if (user_numbers[0] == result[0][0] and
            user_numbers[1] == result[0][1] and
            user_numbers[2] == result[1][0] and
            user_numbers[3] == result[1][1]):
            print("✅ Отлично! Верно!")
            return 1
        else:
            print("❌ Ошибка! Правильный ответ:")
            print(f"{result[0][0]} {result[0][1]}")
            print(f"{result[1][0]} {result[1][1]}")
            return 0
            
    except ValueError:
        print("❌ Ошибка! Введите только числа, разделённые пробелами.")
        return 0