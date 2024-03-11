import tkinter as tk
import tkinter.font as tkFont
###########################################
#Title: End_screen.py
#Created by: Ivin Chan
#Description: The end screen of the game.
###########################################

#End_window
#A class for the end screen window
#@param - boolean - win - if the user lost or won
#@param - diamond.Map - the instance of the current map class.
class End_window:
    home_window = tk.Tk
    def __init__(self, root, win, map_instance):
        #setting title
        if win == True:
            root.title("You win")
            Title_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=48),fg="#333333", justify="center", text= "YOU WIN")
            Title_lb.place(x=70,y=20,width=274,height=70) #creates the title label
        else:
            root.title("You lose")
            Title_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=48),fg="#333333", justify="center", text= "YOU LOSE")
            Title_lb.place(x=50,y=20,width=340,height=70) #creates the title label
        #setting window size
        width=439
        height=245
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Correct_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=10),fg="#333333", justify="left", text= "Correct answers: " + str(map_instance.correct))
        Correct_lb.place(x=40,y=130,width=120,height=25) #creates the correct label. Show how many correct answers they got.

        Incorrect_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=10),fg="#333333", justify="left", text= "incorrect answers: " + str(map_instance.incorrect))
        Incorrect_lb.place(x=40,y=150,width=120,height=25) #creates the incorrect label. Show how many incorrect answers they got.

        Questions_lb=tk.Label(root, font=tkFont.Font(family='Helvetica',size=10),fg="#333333", justify="left", text= "Questions answered: " + str(map_instance.correct + map_instance.incorrect))
        Questions_lb.place(x=40,y=170,width=130,height=25) #creates the questions label. Show how questions answered.

        Quit_btn = tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Helvetica',size=10), fg="#000000", justify="center", text="Quit", command= self.Quit_btn)
        Quit_btn.place(x=240,y=170,width=173,height=41) # creates a quit button

        Main_menu_btn = tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Helvetica',size=10), fg="#000000", justify="center", text="Main menu", command= lambda: self.Main_menu_btn(root))
        Main_menu_btn.place(x=240,y=110,width=173,height=41)# creates a main menu button
    

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


