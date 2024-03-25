import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import diamond
import Infomation
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath("assets/Main_menu")#Establishing the path to the images
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


        #The canvas that all of the images are built on
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
        info_window = Infomation.Info(extra_window)
        info_window.home_window = root
        #Sets the function "onclosing" to be called when the new window tries to be closed
        extra_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(extra_window))
        #hides the main menu
        root.withdraw()
    


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
