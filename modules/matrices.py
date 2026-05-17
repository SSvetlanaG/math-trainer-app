import random

def start_trainer():
    print("\n--- ТРЕНАЖЕР: МАТРИЦЫ (Сложение 2x2) ---")
    print("Для выхода в меню ничего не вводите и просто нажмите Enter\n")
    
    score = 0
    
    while True:
        m1 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
        m2 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
        
        print(f"\nМатрица A: {m1[0]}\n           {m1[1]}")
        print(f"Матрица B: {m2[0]}\n           {m2[1]}")
        
        correct_answer = m1[0][0] + m2[0][0]
        
        user_input = input("Введите сумму верхнего левого угла (A[0][0] + B[0][0]): ").strip()
        
        if user_input == "":
            print(f"Выход. Всего набрано баллов: {score}")
            return score
            
        try:
            ans = int(user_input)
            
            if ans == correct_answer:
                print("✅ Верно!")
                score += 1
            else:
                print(f"❌ Ошибка! Правильный ответ: {correct_answer}")
                
        except ValueError:
            print("❌ Нужно ввести число или нажать Enter для выхода.")
