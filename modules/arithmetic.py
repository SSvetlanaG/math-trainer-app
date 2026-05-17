<<<<<<< HEAD
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
=======
import random

def start_trainer():
    print("\n--- ТРЕНАЖЕР: АРИФМЕТИКА ---")
    
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    
    
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        correct_answer = a + b
        question = f"Сколько будет {a} + {b}? "
    elif operation == '-':
        correct_answer = a - b
        question = f"Сколько будет {a} - {b}? "
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
