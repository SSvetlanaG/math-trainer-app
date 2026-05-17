import random

def start_trainer():
    print("\n--- ТРЕНАЖЕР: АРИФМЕТИКА ---")
    print("Для выхода в меню ничего не вводите и просто нажмите Enter\n")
    
    score = 0
    
    while True:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
        
        if operation == '+':
            correct_answer = a + b
        elif operation == '-':
            correct_answer = a - b
        else:  
            correct_answer = a * b
            
        # Сначала принимаем ответ как обычную строку текста
        user_input = input(f"Сколько будет {a} {operation} {b}? ").strip()
        
        # Если игрок ничего не ввел и нажал Enter — выходим
        if user_input == "":
            print(f"Выход. Всего набрано баллов: {score}")
            return score
            
        try:
            # Превращаем в число только здесь
            user_answer = int(user_input)
            
            if user_answer == correct_answer:
                print("✅ Правильно!")
                score += 1
            else:
                print(f"❌ Ошибка! Правильный ответ: {correct_answer}")
                
        except ValueError:
            print("❌ Нужно вводить только числа или нажать Enter для выхода!")
