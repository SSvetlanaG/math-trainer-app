import random

def start_trainer():
    print("\n--- ТРЕНАЖЕР: АРИФМЕТИКА ---")
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    
    try:
        user_answer = int(input(f"Сколько будет {a} + {b}? "))
        if user_answer == a + b:
            print("✅ Правильно!")
            return 1  # Возвращаем 1 балл
        else:
            print(f"❌ Ошибка! Правильный ответ: {a + b}")
            return 0
    except ValueError:
        print("Нужно вводить числа!")
        return 0