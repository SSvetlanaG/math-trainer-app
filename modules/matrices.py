import random
def start_trainer():
    print("\n--- ТРЕНАЖЕР: МАТРИЦЫ (Сложение 2x2) ---")
    # Генерация простых матриц
    m1 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
    m2 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
    
    print(f"Матрица A: {m1[0]}\n           {m1[1]}")
    print(f"Матрица B: {m2[0]}\n           {m2[1]}")
    
    try:
        ans = int(input("Введите сумму верхнего левого угла (A[0][0] + B[0][0]): "))
        if ans == m1[0][0] + m2[0][0]:
            print("✅ Верно!")
            return 1
        else:
            print("❌ Ошибка!")
            return 0
    except ValueError:
        print("Нужно ввести число.")
        return 0