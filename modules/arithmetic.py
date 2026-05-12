import random

def start_trainer():
    print("\n--- ТРЕНАЖЕР: АРИФМЕТИКА ---")
    
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    
    if random.choice([True, False]):
        
        correct_answer = a + b
        question = f"Сколько будет {a} + {b}? "
    else:
        
        correct_answer = a * b
        question = f"Сколько будет {a} * {b}? "
    
    try:
        user_answer = int(input(question))
        if user_answer == correct_answer:
            print("✅ Правильно!")
            return 1
        else:
            print(f"❌ Ошибка! Правильный ответ: {correct_answer}")
            return 0
    except ValueError:
        print("❌ Нужно вводить числа!")
        return 0