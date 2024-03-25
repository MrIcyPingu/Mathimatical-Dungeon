import tkinter as tk
from pathlib import Path
import tkinter.messagebox

###########################################
#Title: Infomation.py
#Created by: Ivin Chan
#Description: A window to explain how to
#play the game
###########################################

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath("assets/Info") #Establishing the path to the images

class Info:
    home_window = tk.Tk
    def __init__(self, root):
        #setting title
        root.title("Infomation")
        #window size
        width=602
        height=344
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        #The canvas that all the images are placed on
        self.canvas = tk.Canvas(
            root,
            bg = "#FFFFFF",
            height = 344,
            width = 602,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        #Sets up the background
        self.background_image = tk.PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        background = self.canvas.create_image(
            301.0,
            172.0,
            image=self.background_image
        )
        #Creates the title
        self.title_image = tk.PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        title = self.canvas.create_image(
            301.0,
            44.0,
            image=self.title_image
        )
        #Creates the game objective text
        self.Game_objective_image = tk.PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        Game_objective = self.canvas.create_image(
            98.0,
            160.0,
            image=self.Game_objective_image
        )
        #Create the questions text
        self.Questions_image = tk.PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        Questions = self.canvas.create_image(
            394.0,
            160.0,
            image=self.Questions_image
        )
        #Create the battle text
        self.Battle_image = tk.PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        Battle = self.canvas.create_image(
            301.0,
            292.0,
            image=self.Battle_image
        )
        ##Create an exit button
        self.Exit_image = tk.PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        Exit = self.canvas.create_image(
            48.0,
            57.0,
            image=self.Exit_image
        )

        self.canvas.tag_bind(Exit, "<ButtonRelease-1>", lambda x: self.on_closing(root))

    #relative_to_assets()
    #Used to create a path to a an asset
    #@Param - self - the current instance of the class
    #@Param - path - the path/file to be being located
    #@Return - a path to the asset
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #on_closing()
    #A function to be called on when the user manually closes the 
    #@param - self - the current instance of the class.
    #@param - tk.Tk - window - the end screen window
    #@return - the main menu window appears
    def on_closing(self, window:tk.Tk):
     if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.home_window.deiconify()
        window.destroy()