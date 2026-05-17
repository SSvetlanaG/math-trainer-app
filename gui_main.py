import tkinter as tk
from tkinter import messagebox
import random
import math
from modules import stats

class MathTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Математический тренажер")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        self.username = None
        self.current_mode = None
        
        # Переменные для тренажёров
        self.current_problem = None
        self.current_answer = None
        self.current_score = 0
        
        # Для арифметики — сохраняем числа
        self.current_a = None
        self.current_b = None
        
        self.show_welcome()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # ==================== ЭКРАН ПРИВЕТСТВИЯ ====================
    def show_welcome(self):
        self.clear_window()
        
        label = tk.Label(self.root, text="Добро пожаловать!", 
                         font=("Arial", 24, "bold"), bg="#f0f0f0")
        label.pack(pady=50)
        
        label2 = tk.Label(self.root, text="Введите ваше имя:", 
                          font=("Arial", 14), bg="#f0f0f0")
        label2.pack(pady=10)
        
        self.name_entry = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.name_entry.pack(pady=10)
        self.name_entry.bind("<Return>", lambda e: self.save_name())
        
        btn_start = tk.Button(self.root, text="Начать", font=("Arial", 14),
                              bg="#4CAF50", fg="white", command=self.save_name)
        btn_start.pack(pady=20)
    
    def save_name(self):
        name = self.name_entry.get().strip()
        if name:
            self.username = name.capitalize()
        else:
            self.username = "Игрок"
        self.show_main_menu()
    
    # ==================== ГЛАВНОЕ МЕНЮ ====================
    def show_main_menu(self):
        self.clear_window()
        
        label = tk.Label(self.root, text=f"Математический тренажер\nПользователь: {self.username}",
                         font=("Arial", 18, "bold"), bg="#f0f0f0")
        label.pack(pady=30)
        
        buttons = [
            ("1. Арифметика", lambda: self.start_arithmetic()),
            ("2. Матрицы", lambda: self.start_matrices()),
            ("3. Квадратные уравнения", lambda: self.start_quadratic()),
            ("4. Статистика", self.show_stats),
            ("5. Выход", self.exit_app)
        ]
        
        for text, command in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 12),
                            bg="#2196F3", fg="white", width=30,
                            command=command)
            btn.pack(pady=8)
    
    # ==================== ЗАПУСК ТРЕНАЖЁРОВ ====================
    def start_arithmetic(self):
        self.current_mode = "arithmetic"
        self.current_score = 0
        self.next_arithmetic_problem()
    
    def start_matrices(self):
        self.current_mode = "matrices"
        self.current_score = 0
        self.next_matrices_problem()
    
    def start_quadratic(self):
        self.current_mode = "quadratic"
        self.current_score = 0
        self.next_quadratic_problem()
    
    # ---------- Арифметика (ИСПРАВЛЕНА) ----------
    def next_arithmetic_problem(self):
        self.current_a = random.randint(1, 10)
        self.current_b = random.randint(1, 10)
        self.current_answer = self.current_a + self.current_b
        self.show_problem_window(f"Сколько будет?\n\n{self.current_a} + {self.current_b} = ?")
    
    # ---------- Матрицы ----------
    def next_matrices_problem(self):
        operation = random.randint(0, 2)
        m1 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
        
        if operation == 0:
            m2 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
            self.current_answer = [
                m1[0][0] + m2[0][0], m1[0][1] + m2[0][1],
                m1[1][0] + m2[1][0], m1[1][1] + m2[1][1]
            ]
            problem_text = f"Матрица A:\n{m1[0][0]} {m1[0][1]}\n{m1[1][0]} {m1[1][1]}\n\n"
            problem_text += f"Матрица B:\n{m2[0][0]} {m2[0][1]}\n{m2[1][0]} {m2[1][1]}\n\n"
            problem_text += "A + B = ? (введите 4 числа через пробел)"
        
        elif operation == 1:
            m2 = [[random.randint(1, 5) for _ in range(2)] for _ in range(2)]
            self.current_answer = [
                m1[0][0] - m2[0][0], m1[0][1] - m2[0][1],
                m1[1][0] - m2[1][0], m1[1][1] - m2[1][1]
            ]
            problem_text = f"Матрица A:\n{m1[0][0]} {m1[0][1]}\n{m1[1][0]} {m1[1][1]}\n\n"
            problem_text += f"Матрица B:\n{m2[0][0]} {m2[0][1]}\n{m2[1][0]} {m2[1][1]}\n\n"
            problem_text += "A - B = ? (введите 4 числа через пробел)"
        
        else:
            scalar = random.randint(2, 5)
            self.current_answer = [
                m1[0][0] * scalar, m1[0][1] * scalar,
                m1[1][0] * scalar, m1[1][1] * scalar
            ]
            problem_text = f"Матрица A:\n{m1[0][0]} {m1[0][1]}\n{m1[1][0]} {m1[1][1]}\n\n"
            problem_text += f"Умножьте матрицу A на число {scalar}\n\n"
            problem_text += "Результат? (введите 4 числа через пробел)"
        
        self.show_problem_window(problem_text, is_matrix=True)
    
    # ---------- Квадратные уравнения ----------
    def next_quadratic_problem(self):
        x1 = random.randint(-8, 8)
        x2 = random.randint(-8, 8)
        
        b = -(x1 + x2)
        c = x1 * x2
        
        self.current_answer = [x1, x2]
        
        equation = "x²"
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
        
        problem_text = f"Решите уравнение:\n\n{equation}\n\nВведите корни x₁ и x₂ через пробел"
        self.show_problem_window(problem_text, is_quadratic=True)
    
    # ---------- Общее окно для всех тренажёров ----------
    def show_problem_window(self, problem_text, is_matrix=False, is_quadratic=False):
        self.clear_window()
        
        label = tk.Label(self.root, text=problem_text,
                         font=("Courier", 11), bg="#f0f0f0", justify="left")
        label.pack(pady=20)
        
        entry_label = tk.Label(self.root, text="Ваш ответ:", font=("Arial", 12), bg="#f0f0f0")
        entry_label.pack()
        
        self.answer_entry = tk.Entry(self.root, font=("Arial", 14), width=30)
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", lambda e: self.check_answer(is_matrix, is_quadratic))
        
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=20)
        
        check_btn = tk.Button(btn_frame, text="Проверить", font=("Arial", 12),
                              bg="#4CAF50", fg="white",
                              command=lambda: self.check_answer(is_matrix, is_quadratic))
        check_btn.pack(side="left", padx=10)
        
        back_btn = tk.Button(btn_frame, text="Выйти в меню", font=("Arial", 12),
                             bg="#FF9800", fg="white", 
                             command=lambda: self.exit_trainer(is_matrix, is_quadratic))
        back_btn.pack(side="left", padx=10)
        
        self.score_label = tk.Label(self.root, text=f"Баллов за сессию: {self.current_score}",
                                    font=("Arial", 12), bg="#f0f0f0", fg="blue")
        self.score_label.pack(pady=10)
    
    def check_answer(self, is_matrix=False, is_quadratic=False):
        user_input = self.answer_entry.get().strip()
        
        if not user_input:
            messagebox.showinfo("Выход", f"Тренажёр завершён. Набрано баллов: {self.current_score}")
            stats.save_result(self.username, self.current_score)
            self.show_main_menu()
            return
        
        try:
            if is_matrix:
                parts = user_input.split()
                if len(parts) != 4:
                    messagebox.showerror("Ошибка", "Введите 4 числа через пробел!")
                    return
                user_answer = [int(x) for x in parts]
                if user_answer == self.current_answer:
                    self.current_score += 1
                    messagebox.showinfo("Результат", "✅ Верно! +1 балл")
                else:
                    messagebox.showinfo("Результат", f"❌ Ошибка!\nПравильный ответ: {self.current_answer}")
            
            elif is_quadratic:
                parts = user_input.split()
                if len(parts) != 2:
                    messagebox.showerror("Ошибка", "Введите 2 числа через пробел!")
                    return
                user_answer = [int(float(x)) for x in parts]
                correct = self.current_answer
                if (user_answer[0] == correct[0] and user_answer[1] == correct[1]) or \
                   (user_answer[0] == correct[1] and user_answer[1] == correct[0]):
                    self.current_score += 1
                    messagebox.showinfo("Результат", "✅ Верно! +1 балл")
                else:
                    messagebox.showinfo("Результат", f"❌ Ошибка!\nПравильные корни: {correct[0]} и {correct[1]}")
            
            else:  # Арифметика (ИСПРАВЛЕНА)
                user_answer = int(user_input)
                if user_answer == self.current_answer:
                    self.current_score += 1
                    messagebox.showinfo("Результат", "✅ Верно! +1 балл")
                else:
                    messagebox.showinfo("Результат", f"❌ Ошибка!\nПравильный ответ: {self.current_answer}")
            
            self.answer_entry.delete(0, tk.END)
            self.score_label.config(text=f"Баллов за сессию: {self.current_score}")
            
            # Следующая задача
            if self.current_mode == "arithmetic":
                self.next_arithmetic_problem()
            elif self.current_mode == "matrices":
                self.next_matrices_problem()
            elif self.current_mode == "quadratic":
                self.next_quadratic_problem()
            
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числа!")
    
    def exit_trainer(self, is_matrix=False, is_quadratic=False):
        if self.current_score > 0 or messagebox.askyesno("Выход", "Вы точно хотите выйти? Баллы не сохранятся!"):
            stats.save_result(self.username, self.current_score)
            self.show_main_menu()
    
    # ==================== СТАТИСТИКА ====================
    def show_stats(self):
        self.clear_window()
        
        label = tk.Label(self.root, text="Таблица рекордов",
                         font=("Arial", 18, "bold"), bg="#f0f0f0")
        label.pack(pady=20)
        
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(pady=10)
        
        tk.Label(frame, text="Имя игрока", font=("Arial", 12, "bold"),
                 width=20, anchor="w", bg="#f0f0f0").grid(row=0, column=0, padx=5)
        tk.Label(frame, text="Баллы", font=("Arial", 12, "bold"),
                 width=10, anchor="w", bg="#f0f0f0").grid(row=0, column=1, padx=5)
        
        tk.Label(frame, text="-" * 35, bg="#f0f0f0").grid(row=1, column=0, columnspan=2, pady=5)
        
        try:
            with open("statistics.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            
            row = 2
            for line in lines:
                if ": " in line:
                    name, score = line.strip().split(": ", 1)
                    tk.Label(frame, text=name, font=("Courier", 11),
                             width=20, anchor="w", bg="#f0f0f0").grid(row=row, column=0, padx=5)
                    tk.Label(frame, text=score, font=("Courier", 11),
                             width=10, anchor="w", bg="#f0f0f0").grid(row=row, column=1, padx=5)
                    row += 1
            
            if row == 2:
                tk.Label(frame, text="Статистика пока пуста", font=("Arial", 12),
                         fg="red", bg="#f0f0f0").grid(row=row, column=0, columnspan=2)
        
        except FileNotFoundError:
            tk.Label(frame, text="Статистика пока пуста", font=("Arial", 12),
                     fg="red", bg="#f0f0f0").grid(row=2, column=0, columnspan=2)
        
        back_btn = tk.Button(self.root, text="Назад", font=("Arial", 12),
                             bg="#FF9800", fg="white", command=self.show_main_menu)
        back_btn.pack(pady=20)
    
    def exit_app(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathTrainerApp(root)
    root.mainloop()