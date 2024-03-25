import tkinter as tk
from tkinter import ttk
import random
from pathlib import Path
###########################################
#Title: math_questions_systems.py
#Created by: Sadeq Osmani
#Description: This is the python code that
#be used to open up the application. When
#this is ran the main menu of the game
#open.
###########################################
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath("assets/questions")

class MathQuizApp:
    Battle_window = tk.Tk
    Battle_instance = None
    Map_instance = None
    def __init__(self, root):
        root.title("Math Quiz")
        self.set_window_size(root, 600, 426)
        self.canvas = tk.Canvas(
            root,
            bg = "#FFFFFF",
            height = 426,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.background_image = tk.PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.background = self.canvas.create_image(
            300.0,
            213.0,
            image=self.background_image
        )

        self.question_label = self.canvas.create_text(
            220.0,
            170.0,
            anchor="nw",
            text="What Is 11*12?",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.correct_count_label = self.canvas.create_text(
            425.0,
            43.0,
            anchor="nw",
            text="Correct: 0",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.incorrect_count_label = self.canvas.create_text(
            425.0,
            89.0,
            anchor="nw",
            text="Incorrect: 0",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.answer_button_image = tk.PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        answer_button = self.canvas.create_image(
            440.0833435058594,
            285.6666259765625,
            image=self.answer_button_image
        )
        self.canvas.tag_bind(answer_button, "<ButtonRelease-1>", lambda x : self.answer_button_command(root))

        self.answer_entry = tk.Entry(root, bd=0, bg="#35CE0F", fg="#000716", highlightthickness=0)

        self.answer_entry.place(
            x=99.0,
            y=252.0,
            width=169.0,
            height=66.0
        )
        self.result_label = tk.Label(root, text="", font=('Times', 10), bg="#35CE0F", foreground="#000716", justify='center')
        self.result_label.place(
            x=100, 
            y=350, 
            width=100, 
            height=40
        )
        # Initialize counters
        self.correct_count = 0
        self.incorrect_count = 0
        self.generate_question()

    def set_window_size(self, root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        align_str = f'{width}x{height}+{(screen_width - width) // 2}+{(screen_height - height) // 2}'
        root.geometry(align_str)
        root.resizable(width=False, height=False)
    
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)


    def answer_button_command(self, window:tk.Tk):
        user_answer = self.answer_entry.get()
        correct_answer = str(eval(self.canvas.itemcget(self.question_label, "text").replace("What is", "").replace("?", "")))

        if user_answer == correct_answer:
            self.result_label.config(text="Correct")
            self.correct_count += 1
        else:
            self.result_label.config(text="Wrong")
            self.incorrect_count += 1

        # Update counters
        self.canvas.itemconfig(self.correct_count_label, text=f"Correct: {self.correct_count}")
        self.canvas.itemconfig(self.incorrect_count_label,text=f"Incorrect: {self.incorrect_count}")

        if self.correct_count + self.incorrect_count != 4:
            self.generate_question()
        else:
            self.Battle_window.deiconify()
            self.Battle_instance.player.energy = self.correct_count
            self.Battle_instance.canvas.itemconfig(self.Battle_instance.Energy_lb, text="Energy: " + str(self.correct_count))
            self.Map_instance.correct += self.correct_count
            self.Map_instance.incorrect += self.incorrect_count
            window.destroy()

    def generate_question(self):
        # Clear the result label
        self.result_label.config(text="")
        # Clear the answer entry
        self.answer_entry.delete(0, tk.END)
        
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*', '/'])
        question_text = f"What is {num1} {operation} {num2}?"
        self.canvas.itemconfig(self.question_label, text=question_text)
