import tkinter as tk
from pathlib import Path
import tkinter.messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath("assets/Info")

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
        self.image_image_1 = tk.PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            301.0,
            172.0,
            image=self.image_image_1
        )

        self.image_image_2 = tk.PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            301.0,
            44.0,
            image=self.image_image_2
        )

        self.image_image_3 = tk.PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            98.0,
            160.0,
            image=self.image_image_3
        )

        self.image_image_4 = tk.PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            394.0,
            160.0,
            image=self.image_image_4
        )

        self.image_image_5 = tk.PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            301.0,
            292.0,
            image=self.image_image_5
        )

        self.image_image_6 = tk.PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            48.0,
            57.0,
            image=self.image_image_6
        )

        self.canvas.tag_bind(image_6, "<ButtonRelease-1>", lambda x: self.on_closing(root))

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