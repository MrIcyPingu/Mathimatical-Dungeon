import tkinter as tk
import Battle_encounter
import tkinter.messagebox


class map:
    buttons = []
    node_counter = 0
    connected_nodes = []
    home_window = tk.Tk
    def __init__(self, root):
     self.buttons.clear()
     self.node_counter = 0
     self.connected_nodes.clear()
     root.title("Map")
     width=630
     height=460
     screenwidth = root.winfo_screenwidth()
     screenheight = root.winfo_screenheight()
     alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
     root.geometry(alignstr)

    # Create buttons in a diamond grid
     for i in range(7):
         counter = 0
         for j in range(7):
             if i + j >= 3 and j - i <= 3 and i - j <= 3 and i + j <= 9:
                 if (i, j) not in [(1, 3), (2, 2), (2, 4), (3, 1), (3, 3), (3, 5), (4, 2), (4, 4), (5, 3)]:
                    button = self.create_node(root)
                    button.grid(row=i, column=j, padx=5, pady=5)
                    self.connected_nodes.append(((i, j),(i+1, j-1),(i+1, j+1)))
                    button["text"] = str(i) + ", " + str(j)
                 else:
                    tk.Label(root, text="").grid(row=i, column=j, padx=10, pady=10)
             else:
                # Create a blank label as placeholder for empty space
                tk.Label(root, text="").grid(row=i, column=j, padx=5, pady=5)
    
    def create_node(self, window: tk.Tk):
      button = tk.Button(window, name="node_" + str(self.node_counter), bg="#f0f0f0", width=10, height=3, fg="#000000", justify="center")
      button["command"] = lambda: self.start_encounter(button, window)
      self.node_counter += 1
      self.buttons.append(button)
      return button

    def start_encounter(self, node: tk.Button, window:tk.Tk):
        extra_window = tk.Toplevel()
        button_pressed = int(str(node.winfo_name).split(".")[-1][-3])
        battle = Battle_encounter.Battle_Encounter(extra_window, button_pressed)
        battle.home_window = window
        battle.Main_window = self.home_window
        extra_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(window, extra_window))
        node["state"] = "disabled"
        node["text"] = "X"
        window.withdraw()

    def on_closing(self, window_main:tk.Tk, window_battle:tk.Tk):
     if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.home_window.deiconify()
        window_battle.destroy()
        window_main.destroy()






