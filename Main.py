import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import diamond
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath("assets/Main_menu")
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


        canvas = tk.Canvas(
            root,
            bg = "#6CBBDA",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        #background image
        canvas.place(x = 0, y = 0)
        self.background_image = tk.PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        background = canvas.create_image(
            291.0,
            169.0,
            image=self.background_image
        )
        
        self.Title_lb_image = tk.PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        
        #Creates the title
        Title_lb = canvas.create_image(
            285.0,
            104.0,
            image=self.Title_lb_image
        )

        #Creates the infomation button
        self.Info_Btn_image = tk.PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        
        Info_Btn = canvas.create_image(
            369.0,
            247.0,
            image=self.Info_Btn_image
        )
        canvas.tag_bind(Info_Btn, "<Button-1>", lambda x :self.Info_Btn())

        #Creates the start game button
        self.Start_game_Btn_image = tk.PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        
        Start_game_Btn = canvas.create_image(
            206.0,
            202.0,
            image=self.Start_game_Btn_image
        )
        canvas.tag_bind(Start_game_Btn, "<ButtonRelease-1>", lambda x : self.Start_game_Btn())



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

    #relative_to_assets()
    #Used to create a path to a an asset
    #@Param - self - the current instance of the class
    #@Param - path - the path/file to be being located
    #@Return - a path to the asset
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop() # keeps the program running as long as the main menu is alive.
