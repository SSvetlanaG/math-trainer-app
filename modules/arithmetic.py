import random

def start_trainer():
    print("\n--- ТРЕНАЖЕР: АРИФМЕТИКА ---")
    print("Для выхода в меню введите число 0\n")
    
    score = 0  # Сюда складываем баллы
    
    while True:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
        
        # Считаем правильный ответ
        if operation == '+':
            correct_answer = a + b
        elif operation == '-':
            correct_answer = a - b
        else:  
            correct_answer = a * b
            
        try:
            # Запрашиваем ответ (сразу числом)
            user_answer = int(input(f"Сколько будет {a} {operation} {b}? "))
            
            # Если ввели 0 — выходим из цикла и возвращаем баллы
            if user_answer == 0:
                print(f"Выход. Всего набрано баллов: {score}")
                return score
                
            # Проверяем ответ
            if user_answer == correct_answer:
                print("✅ Правильно!")
                score += 1
            else:
                print(f"❌ Ошибка! Правильный ответ: {correct_answer}")
                
        except ValueError:
            print("❌ Нужно вводить только числа!")
