import tkinter as tk
import tkinter.font as tkFont

class End_window:
    home_window = tk.Tk
    def __init__(self, root, win):
        #setting title
        if win == True:
            root.title("You win")
            Title_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=48),fg="#333333", justify="center", text= "YOU WIN")
            Title_lb.place(x=70,y=20,width=274,height=70) #creates the title label
        else:
            root.title("You lose")
            Title_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=48),fg="#333333", justify="center", text= "YOU LOSE")
            Title_lb.place(x=70,y=20,width=274,height=70) #creates the title label
        #setting window size
        width=439
        height=245
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Title_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=48),fg="#333333", justify="center", text= "YOU WIN")
        Title_lb.place(x=70,y=20,width=274,height=70) #creates the title label

        Correct_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=10),fg="#333333", justify="left", text= "Correct answers: ")
        Correct_lb.place(x=40,y=130,width=120,height=25) #creates the correct label

        Incorrect_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=10),fg="#333333", justify="left", text= "incorrect answers: ")
        Incorrect_lb.place(x=40,y=150,width=120,height=25) #creates the incorrect label

        Questions_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=10),fg="#333333", justify="left", text= "Questions answered: ")
        Questions_lb.place(x=40,y=170,width=130,height=25) #creates the questions label

        Quit_btn = tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Helvetica',size=10), fg="#000000", justify="center", text="Quit", command= self.Quit_btn)
        Quit_btn.place(x=240,y=170,width=173,height=41)

        Main_menu_btn = tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Helvetica',size=10), fg="#000000", justify="center", text="Main menu", command= lambda: self.Main_menu_btn(root))
        Main_menu_btn.place(x=240,y=110,width=173,height=41)
    
    def Quit_btn(self):
        self.home_window.destroy()
    
    def Main_menu_btn(self, window: tk.Tk):
        self.home_window.deiconify()
        window.destroy()


