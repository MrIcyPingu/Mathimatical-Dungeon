import tkinter as tk
import Battle_encounter
import tkinter.messagebox
###########################################
#Title: Diamond.py
#Created by: Ivin Chan
#Description: Placeholder code for the map
#while Saffa makes her own.
###########################################

#Map()
#A class for the map window
class Map:
    home_window = tk.Tk # The main menu reference
    def __init__(self, root):
     self.buttons = {} # Stores the buttons
     self.node_counter = 0 # Uses to set the button names
     self.connected_nodes = {} # Stores what buttons are connected
     self.correct = 0 # Uses to see how many correct answers 
     self.incorrect = 0# Uses to see how many incorrect answers 
     #Sets the title 
     root.title("Map")
     #Setting the window size
     width=630
     height=460
     screenwidth = root.winfo_screenwidth()
     screenheight = root.winfo_screenheight()
     alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
     root.geometry(alignstr)

    # Create buttons in a diamond grid
     for i in range(7):#for each row
         for j in range(7):#for each column
             if i + j >= 3 and j - i <= 3 and i - j <= 3 and i + j <= 9:
                 if (i, j) not in [(1, 3), (2, 2), (2, 4), (3, 1), (3, 3), (3, 5), (4, 2), (4, 4), (5, 3)]:
                    button = self.create_node(root) #creates a button
                    self.buttons.update({(i,j): button})
                    button.grid(row=i, column=j, padx=5, pady=5) #places the button in the grid
                    self.connected_nodes.update({(i, j): ((i-1, j+1),(i+1, j+1))}) #links connected buttons on the map
                    button["text"] = str(i) + ", " + str(j)
                 else:
                    tk.Label(root, text="").grid(row=i, column=j, padx=10, pady=10)
             else:
                # Create a blank label as placeholder for empty space
                tk.Label(root, text="").grid(row=i, column=j, padx=5, pady=5)
    #sets the starting node to enabled
     self.buttons[(3,0)]["state"] = "normal"
    
    #create_node()
    #A function to create the buttons that will be the nodes of the map.
    #@param - self - the current instance of the class.
    #@param - tk.Tk - window - the window the nodes are going to made on.
    #@return - tk.button - button - the button that will acts as the node on the map.
    def create_node(self, window: tk.Tk):
      #Creating the button
      button = tk.Button(window, name="node_" + str(self.node_counter), bg="#f0f0f0", width=10, height=3, fg="#000000", justify="center")
      button["command"] = lambda: self.start_encounter(button, window)
      button["state"] = "disabled" #Making the button unclickable for the time being.
      self.node_counter += 1
      return button

    #start_encounter()
    #A function to create the battle encounter window
    #@param - self - the current instance of the class.
    #@param - tk.Tk - window - the map window
    #@param - tk.button - node - the button that has been pressed
    #@return - a battle encounter window
    def start_encounter(self, node: tk.Button, window:tk.Tk):
        extra_window = tk.Toplevel()
        button_pressed = int(str(node.winfo_name).split(".")[-1][-3]) #get the button number
        #creates a battle encounter window
        battle = Battle_encounter.Battle_Encounter(extra_window, button_pressed, self)
        battle.Map_window = window #adds a reference to the map window to the new window
        battle.Main_window = self.home_window # adds a reference to the main menu window to the new window
        extra_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(window, extra_window))
        nodes = self.connected_nodes[tuple(map(int, node.cget('text').split(', ')))] #gets the grid references of connect nodes
        for map_node in self.buttons.values(): #disables all nodes on the map
           map_node["state"] = "disabled" 

        for button in nodes:
           if button in self.buttons:
              self.buttons[button]["state"] = "normal" # Enables all nodes that are connected, if the node exists.
        node["text"] = "X"
        window.withdraw() # hides the map window

    #on_closing()
    #A function to be called on when the user manually closes the 
    #@param - self - the current instance of the class.
    #@param - tk.Tk - window_main - the map window
    #@param - tk.Tk - window_battle - the battle window
    #@return - the main menu window appears
    def on_closing(self, window_main:tk.Tk, window_battle:tk.Tk):
     if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.home_window.deiconify() #unhides main menu
        window_battle.destroy() #closes battle window
        window_main.destroy() #closes map window






