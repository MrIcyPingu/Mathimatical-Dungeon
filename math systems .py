import tkinter as tk
from tkinter import ttk
import random

class MathQuizApp:
    def __init__(self, root):
        root.title("Math Quiz")
        self.set_window_size(root, 600, 500)

        self.create_widgets(root)
        self.generate_question()

    def set_window_size(self, root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        align_str = f'{width}x{height}+{(screen_width - width) // 2}+{(screen_height - height) // 2}'
        root.geometry(align_str)
        root.resizable(width=False, height=False)

    def create_widgets(self, root):
        self.question_label = self.create_label(root, "", 100, 120, 370, 124)
        self.create_label(root, "math question:", 70, 70, 151, 30)

        self.answer_entry = self.create_entry(root, "", 100, 270, 177, 82)

        answer_button = self.create_button(root, "Answer Button", self.answer_button_command, 330, 290, 117, 45)
        self.result_label = self.create_label(root, "", 100, 350, 370, 30)

    def create_label(self, root, text, x, y, width, height):
        label = ttk.Label(root, text=text, font=('Times', 10), foreground='#333333', justify='center')
        label.place(x=x, y=y, width=width, height=height)
        return label

    def create_entry(self, root, default_text, x, y, width, height):
        entry = ttk.Entry(root, font=('Times', 10), justify='center')
        entry.place(x=x, y=y, width=width, height=height)
        return entry

    def create_button(self, root, text, command, x, y, width, height):
        button = ttk.Button(root, text=text, command=command)
        button.place(x=x, y=y, width=width, height=height)
        return button

    def answer_button_command(self):
        user_answer = self.answer_entry.get()
        correct_answer = str(eval(self.question_label["text"].replace("What is", "").replace("?", "")))

        if user_answer == correct_answer:
            self.result_label.config(text="Correct")
        else:
            self.result_label.config(text="Wrong")

        self.generate_question()

    def generate_question(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*', '/'])
        question_text = f"What is {num1} {operation} {num2}?"
        self.question_label.config(text=question_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
