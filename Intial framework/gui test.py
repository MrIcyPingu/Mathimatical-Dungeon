import tkinter as tk
import tkinter.font as tkFont

def card_focus(button: tk.Button):
        button.tkraise()
        button.place(y=330,width=162,height=172)

def card_unfocus(button: tk.Button):
        button.lower()
        button.place(y=430,width=81,height=86)

class App:
    def __init__(self, root):
        #setting title
        root.title("GUI test")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        New_window_Btn=tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center", text="Button")
        New_window_Btn.place(x=260,y=230,width=70,height=25)
        New_window_Btn["command"] = self.New_window_Btn

        New_card_Btn=tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center", text="Button")
        New_card_Btn.place(x=260,y=200,width=70,height=25)
        New_card_Btn["command"] = self.New_card_Btn

        hero_frame = tk.Frame(root, width=128,height=184, borderwidth=2, relief="groove")
        hero_frame.place(x=60,y=140)

        enemy_frame = tk.Frame(root, width=128,height=184, borderwidth=2, relief="groove")
        enemy_frame.place(x=420,y=140)

    def New_card_Btn(self):
        global card_counter
        card = tk.Button(root, name="card_" + str(card_counter), bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center", text="Card", command= lambda: print('hey'))
        cards.append(card)
        card.place(x=65 + card_counter*50 ,y=430,width=81,height=86)
        card.bind("<Enter>", lambda x: card_focus(card))
        card.bind("<Leave>", lambda x: card_unfocus(card))
        card_counter += 1    
             
    def New_window_Btn(self):
        extra_window = tk.Toplevel()
        extra_window.title("new window")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        extra_window.geometry(alignstr)

        New_window_Btn=tk.Button(extra_window, bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center", text="Button")
        New_window_Btn.place(x=260,y=230,width=70,height=25)
        New_window_Btn["command"] = self.New_window_Btn     

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    card_counter = 0
    cards = []
    root.mainloop()
