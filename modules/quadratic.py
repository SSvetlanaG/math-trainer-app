import random

def start_trainer():
    print("\n--- ТРЕНАЖЕР: КВАДРАТНЫЕ УРАВНЕНИЯ ---")
    print("Формат: x² + bx + c = 0")
    print("Для выхода в меню ничего не вводите и просто нажмите Enter\n")
    
    score = 0
    
    while True:
        # Генерируем два случайных целых корня (от -8 до 8, не включая 0)
        x1 = random.randint(-8, 8)
        x2 = random.randint(-8, 8)
        
        # По корням вычисляем коэффициенты
        # Уравнение: x² - (x1 + x2)x + (x1 * x2) = 0
        b = -(x1 + x2)
        c = x1 * x2
        
        # Красивый вывод уравнения
        equation = f"x²"
        if b != 0:
            if b > 0:
                equation += f" + {b}x"
            else:
                equation += f" - {abs(b)}x"
        if c != 0:
            if c > 0:
                equation += f" + {c}"
            else:
                equation += f" - {abs(c)}"
        equation += " = 0"
        
        print(f"\n{equation}")
        
        # Ввод первого корня (выход по Enter)
        user_input1 = input("Введите x₁ (или Enter для выхода): ").strip()
        
        if user_input1 == "":
            print(f"\nВыход. Всего набрано баллов: {score}")
            return score
        
        user_input2 = input("Введите x₂: ").strip()
        
        # Проверка на пустой ввод x₂ (тоже выход)
        if user_input2 == "":
            print(f"\nВыход. Всего набрано баллов: {score}")
            return score
        
        # Проверка ответа
        try:
            ans1 = int(float(user_input1))  # Преобразуем в целое
            ans2 = int(float(user_input2))
            
            # Проверяем (порядок корней может быть любым)
            if (ans1 == x1 and ans2 == x2) or (ans1 == x2 and ans2 == x1):
                print("✅ Верно!")
                score += 1
            else:
                print(f"❌ Ошибка! Правильные корни: {x1} и {x2}")
        except ValueError:
            print("❌ Ошибка! Введите целые числа.")