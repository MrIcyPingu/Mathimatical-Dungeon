import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import diamond
import End_screen

class Main():
    def __init__(self, root):
        #setting title
        root.title("Main menu")
        #setting window size
        width=582
        height=336
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        Title_lb = tk.Label(root, font=tkFont.Font(family='Helvetica',size=40), fg="#333333", justify="center", text="Mathematical Dungeon" )
        Title_lb.place(x=10,y=20,width=563,height=104)

        Start_game_Btn=tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Helvetica',size=10), fg="#000000", justify="center", text="Start Game")
        Start_game_Btn.place(x=160,y=140,width=258,height=64)
        Start_game_Btn["command"] = self.Start_game_Btn

        Info_Btn=tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Helvetica',size=10), fg="#000000", justify="center", text="Infomation")
        Info_Btn.place(x=160,y=220,width=258,height=64)
        Info_Btn["command"] = self.Info_Btn

    def Info_Btn(self):
        extra_window = tk.Toplevel()
        extra_window.title("new window")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        extra_window.geometry(alignstr)
        extra_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(extra_window))
        root.withdraw()

    def Start_game_Btn(self):
        extra_window = tk.Toplevel()
        map = diamond.map(extra_window)
        map.home_window = root
        extra_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(extra_window))
        root.withdraw()

    
    def on_closing(self, window:tk.Tk):
     if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.deiconify()
        window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
