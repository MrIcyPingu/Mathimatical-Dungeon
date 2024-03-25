import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
from pathlib import Path
###########################################
#Title: End_screen.py
#Created by: Ivin Chan
#Description: The end screen of the game.
###########################################
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath("assets/end")
#End_window
#A class for the end screen window
#@param - boolean - win - if the user lost or won
#@param - diamond.Map - the instance of the current map class.
class End_window:
    home_window = tk.Tk
    def __init__(self, root, win, map_instance):
        #setting window size
        width=439
        height=245
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.canvas = tk.Canvas(
            root,
            bg = "#FFFFFF",
            height = 245,
            width = 439,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.background_image = tk.PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        background = self.canvas.create_image(
            219.0,
            122.0,
            image=self.background_image
        )

        self.Main_menu_btn_image = tk.PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        Main_menu_btn = self.canvas.create_image(
            358.0,
            139.0,
            image=self.Main_menu_btn_image
        )
        self.canvas.tag_bind(Main_menu_btn, "<ButtonRelease-1>", lambda x : self.Main_menu_btn(root))

        self.Quit_btn_image = tk.PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        Quit_btn = self.canvas.create_image(
            351.52496337890625,
            182.79470825195312,
            image=self.Quit_btn_image
        )
        self.canvas.tag_bind(Quit_btn, "<ButtonRelease-1>", lambda x : self.Quit_btn())

        self.canvas.create_text(
            7.597900390625,
            126.79571533203125,
            anchor="nw",
            text="Correct Answers: " + str(map_instance.correct),
            fill="#1E1E1E",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            7.597900390625,
            152.79571533203125,
            anchor="nw",
            text="Incorrect Answers: " + str(map_instance.incorrect),
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            7.597900390625,
            175.79571533203125,
            anchor="nw",
            text="Questions Answered: " + str(map_instance.correct + map_instance.incorrect),
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        #setting title
        if win == True:
            root.title("You win")
            self.canvas.create_text(
                139.0,
                24.0,
                anchor="nw",
                text="YOU WIN",
                fill="#000000",
                font=("Inter", 32 * -1)
            )
        else:
            root.title("You lose")
            self.canvas.create_text(
                139.0,
                24.0,
                anchor="nw",
                text="YOU LOSE",
                fill="#000000",
                font=("Inter", 32 * -1)
            )
        root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root))
    

    #create_node()
    #A function to stop the game/applcation
    #@param - self - the current instance of the class.
    def Quit_btn(self):
        self.home_window.destroy() # destroys the menu menu which stops the game
    
    #Main_menu_btn()
    #A function to open the main menu
    #@param - self - the current instance of the class.
    #@param - tk.Tk - window - the end screen window
    def Main_menu_btn(self, window: tk.Tk):
        self.home_window.deiconify() # unhides the main menu
        window.destroy()# destroys the end screen window.

    #on_closing()
    #A function to be called on when the user manually closes the 
    #@param - self - the current instance of the class.
    #@param - tk.Tk - window - the end screen window
    #@return - the main menu window appears
    def on_closing(self, window:tk.Tk):
     if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.home_window.deiconify()
        window.destroy()

    #relative_to_assets()
    #Used to create a path to a an asset
    #@Param - self - the current instance of the class
    #@Param - path - the path/file to be being located
    #@Return - a path to the asset
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)


