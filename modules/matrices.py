import random

def start_trainer():
    print("\n--- ТРЕНАЖЕР: МАТРИЦЫ (Сложение 2x2) ---")
    print("Для выхода в меню введите число 0\n")
    
    score = 0  # Сюда складываем баллы
    
    while True:
        # Генерация простых матриц
        m1 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
        m2 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
        
        print(f"\nМатрица A: {m1[0]}\n           {m1[1]}")
        print(f"Матрица B: {m2[0]}\n           {m2[1]}")
        
        try:
            ans = int(input("Введите сумму верхнего левого угла (A[0][0] + B[0][0]): "))
            
            # Если ввели 0 — выходим из цикла и возвращаем баллы в меню
            if ans == 0:
                print(f"Выход. Всего набрано баллов: {score}")
                return score
                
            # Проверяем ответ
            if ans == m1[0][0] + m2[0][0]:
                print("✅ Верно!")
                score += 1
            else:
                print(f"❌ Ошибка! Правильный ответ: {m1[0][0] + m2[0][0]}")
                
        except ValueError:
            print("❌ Нужно ввести число.")
