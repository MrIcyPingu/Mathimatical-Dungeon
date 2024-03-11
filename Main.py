import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import diamond
###########################################
#Title: Main.py
#Created by: Ivin Chan
#Description: This is the python code that
#be used to open up the application. When
#this is ran the main menu of the game
#open.
###########################################

#Main
#A class for the main menu window
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

        #Creates the title text
        Title_lb = tk.Label(root, font=tkFont.Font(family='Helvetica',size=40), fg="#333333", justify="center", text="Mathematical Dungeon" )
        Title_lb.place(x=10,y=20,width=563,height=104)

        #Creates the start game button
        Start_game_Btn=tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Helvetica',size=10), fg="#000000", justify="center", text="Start Game")
        Start_game_Btn.place(x=160,y=140,width=258,height=64)
        Start_game_Btn["command"] = self.Start_game_Btn

        #Creates the infomation button
        Info_Btn=tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Helvetica',size=10), fg="#000000", justify="center", text="Infomation")
        Info_Btn.place(x=160,y=220,width=258,height=64)
        Info_Btn["command"] = self.Info_Btn

    #Info_Btn()
    #Creates a new window with the nessary infomation on how to play the game
    #@Param - self - the current instance of the class
    #@Return - tk.Toplevel - extra_window - the infomation window
    def Info_Btn(self):
        extra_window = tk.Toplevel()
        #window title
        extra_window.title("Infomation")
        #window size
        width=602
        height=344
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        extra_window.geometry(alignstr)
        #Sets the function "onclosing" to be called when the new window tries to be closed
        extra_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(extra_window))
        #hides the main menu
        root.withdraw()

        #Creates the Title text
        Title_lb=tk.Label(extra_window, font=tkFont.Font(family='Helvetica',size=48), fg="#333333", justify="center", text="Infomation" )
        Title_lb.place(x=140,y=10,width=293,height=52)

        #Creates the game objective title
        Game_objective_lb=tk.Label(extra_window, font=tkFont.Font(family='Helvetica',size=18), fg="#333333", justify="left", text="Game objective" )
        Game_objective_lb.place(x=10,y=70,width=175,height=37)
        #Creates the game objective body of text
        Game_objective_body_lb=tk.Label(extra_window, font=tkFont.Font(family='Helvetica',size=10), fg="#333333", justify="left", text="The aim of this game is to travel \nthrough the map, from the left \nto the right. For each node you \ntravel to, you will be met with a \nbattle to face where you will \nhave to fight an enemy, making \nyour way to the end." )
        Game_objective_body_lb.place(x=10,y=100,width=200,height=118)
        #Creates the battle title
        Battle_lb=tk.Label(extra_window, font=tkFont.Font(family='Helvetica',size=18), fg="#333333", justify="left", text="Battle" )
        Battle_lb.place(x=240,y=70,width=60,height=37)
        #Creates the battle body of text
        Battle_body_lb=tk.Label(extra_window, font=tkFont.Font(family='Helvetica',size=10), fg="#333333", justify="left", text="When you fight the enemies, you will be given 5 cards to \nuses. To either attack, defence or heal with your aim to get \nthe enemy's to 0, while keep you health above 0. Each card \ntake a certain amount of energy, with you having 4 energy \neach turn. If you have no energy, end your turn and the \nenemy's turn will  start where they will attack and/or \ndefend, and it will be your turn again" )
        Battle_body_lb.place(x=240,y=100,width=350,height=118)
        #Creates the questions title
        Questions_lb=tk.Label(extra_window, font=tkFont.Font(family='Helvetica',size=18), fg="#333333", justify="left", text="Questions" )
        Questions_lb.place(x=10,y=225,width=120,height=37)
        #Creates the questions body of text
        Questions_body_lb=tk.Label(extra_window, font=tkFont.Font(family='Helvetica',size=10), fg="#333333", justify="left", text="To get the energy for you battles, each turn you will be asked a list of questions. The amount of \nquestion you are ask will be the same to the amount of energy you have, so if you answer 4 \nquestions correctly you will be given 4 energy. All question are Maths questions, that will help you \ntrain you maths skills while you raid our dungeon." )
        Questions_body_lb.place(x=10,y=255,width=580,height=75)


    #Start_game_Btn()
    #Creates a new window with the map
    #@Param - self - the current instance of the class
    #@Return - tk.Toplevel - extra_window - the map window
    def Start_game_Btn(self):
        extra_window = tk.Toplevel()
        #Create a new instance of the map class with a new window
        map = diamond.Map(extra_window)
        #Creating a reference to the main menu, in the map class
        map.home_window = root
        #Sets the function "onclosing" to be called when the new window tries to be closed
        extra_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(extra_window))
        #hiding the main menu
        root.withdraw()

    #on_closing()
    #Creates a dialog box to make sure that they want to close the window and reopen the main menu if yes. 
    #@Param - self - the current instance of the class
    #@Param - tk.Tk - window - the window that is being closed
    #@Return - main menu reappears and window closes, if dialog box passes
    def on_closing(self, window:tk.Tk):
     if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.deiconify()
        window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop() # keeps the program running as long as the main menu is alive.
