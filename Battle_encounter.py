import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import tkinter.ttk
import random
import End_screen
import math_questions_systems
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath("assets/Battle_encounter")
###########################################
#Title: Battle_encounter.py
#Created by: Ivin Chan
#Description: The code for when the user
#enters a battle.
###########################################

#Entity
#A class for the creation of entities that will be used the battle encounter
#@param - health - int - the life points of the entity to see if is dead
#@param - defence - int - how much defence does the entity have
#@param - energy_limit - int - the maximum amount of energy the entity can have
#@param - energy - int - the current amount of energy the entity has.
class Entity:
     health = 10
     defence = 0
     energy = 4
     energy_limit = 4

#Battle_Encounter
#A class for the battle encounter window
#@param - button_pressed - int - the button pressed on the map to make the battle encounter
#@param - map_instance - diamond.map - a reference to the currently running class of the map.
class Battle_Encounter():
    player = Entity() #creates the player and enemy
    enemy = Entity()
    card_counter = 0
    cards = []
    Map_window = tk.Tk
    Main_window = tk.Tk

    #card_focus()
    #this function is used to enlarge a card to make it stand out in the hand
    #@param - self - the current instance of the class.
    #@param - button - tk.button - the card to be focused on
    def card_focus(self, button: tk.Button):
            button.tkraise()
            if button.cget("image") == self.attack_picture_small.name:
                button["image"] = self.attack_picture
            elif button.cget("image") == self.defence_picture_small.name:
                button["image"] = self.defence_picture
            elif button.cget("image") == self.heal_picture_small.name:
                button["image"] = self.heal_picture
            button.place(y=330,width=162,height=172)

    #card_unfocus()
    #this function is used to return a card to its orignal size in the correct postion on the deck
    #@param - self - the current instance of the class.
    #@param - button - tk.button - the card to be unfocused
    def card_unfocus(self, button: tk.Button):
            card_num=int(str(button.winfo_name).split(".")[-1][-3]) #used to determine which layer the card should go on 
            if self.card_counter > 0 and card_num < self.card_counter - 1:
                card_below = self.cards[card_num + 1]
                button.lower(card_below)
            button.place(y=430,width=81,height=86)
            if button.cget("image") == self.attack_picture.name:
                button["image"] = self.attack_picture_small
            elif button.cget("image") == self.defence_picture.name:
                button["image"] = self.defence_picture_small
            elif button.cget("image") == self.heal_picture.name:
                button["image"] = self.heal_picture_small

    def __init__(self, root, button_pressed, map_instance):
        #setting title
        root.title("Battle")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.attack_picture = tkinter.PhotoImage(file = self.relative_to_assets("Attack.png"))
        self.attack_picture_small = tkinter.PhotoImage(file = self.relative_to_assets("Attack_small.png"))
        self.defence_picture = tkinter.PhotoImage(file = self.relative_to_assets("Defend.png"))
        self.defence_picture_small = tkinter.PhotoImage(file = self.relative_to_assets("Defend_small.png"))
        self.heal_picture = tkinter.PhotoImage(file = self.relative_to_assets("Heal.png"))
        self.heal_picture_small = tkinter.PhotoImage(file = self.relative_to_assets("Heal_small.png"))
        
        self.canvas = tk.Canvas(
            root,
            bg = "#FFFFFF",
            height = 500,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.background_image = tk.PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        background = self.canvas.create_image(
            300.0,
            250.0,
            image=self.background_image
        )

        self.Energy_lb_image = tk.PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        Energy_lb = self.canvas.create_image(
            496.0,
            38.0,
            image=self.Energy_lb_image
        )

        self.Enemy_health_lb_image = tk.PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        Enemy_health_lb = self.canvas.create_image(
            434.0,
            133.0,
            image=self.Enemy_health_lb_image
        )

        self.Hero_health_lb_image = tk.PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        Hero_health_lb = self.canvas.create_image(
            155.0,
            38.0,
            image=self.Hero_health_lb_image
        )

        self.Hero_image = tk.PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        Hero = self.canvas.create_image(
            130.0,
            255.0,
            image=self.Hero_image
        )
        if button_pressed == 9:
            self.Enemy_image = tk.PhotoImage(
                file=self.relative_to_assets("image_10.png"))
            Enemy = self.canvas.create_image(
                432.0,
                250.0,
                image=self.Enemy_image
            )
            self.enemy.energy = 5
            self.enemy.health = 15
        else:
            match random.randint(0, 3): #determines the type of card
                    case 0:
                        self.Enemy_image = tk.PhotoImage(
                            file=self.relative_to_assets("image_6.png"))
                        Enemy = self.canvas.create_image(
                            432.0,
                            250.0,
                            image=self.Enemy_image
                        )
                        self.enemy.energy = 4
                        self.enemy.energy_limit = 4
                        self.enemy.health = 10
                    case 1:
                        self.Enemy_image = tk.PhotoImage(
                            file=self.relative_to_assets("image_8.png"))
                        Enemy = self.canvas.create_image(
                            432.0,
                            250.0,
                            image=self.Enemy_image
                        )
                        self.enemy.energy = 5
                        self.enemy.energy_limit = 5
                        self.enemy.health = 6
                    case 2:
                        self.Enemy_image = tk.PhotoImage(
                            file=self.relative_to_assets("image_9.png"))
                        Enemy = self.canvas.create_image(
                            432.0,
                            250.0,
                            image=self.Enemy_image
                        )
                        self.enemy.energy = 3
                        self.enemy.energy_limit = 3
                        self.enemy.health = 12
                    case _:
                        self.Enemy_image = tk.PhotoImage(
                            file=self.relative_to_assets("image_6.png"))
                        Enemy = self.canvas.create_image(
                            432.0,
                            250.0,
                            image=self.Enemy_image
                        )
                        self.enemy.energy = 4
                        self.enemy.energy_limit = 4
                        self.enemy.health = 10


        self.End_turn_btn_image = tk.PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        End_turn_btn = self.canvas.create_image(
            69.0,
            132.0,
            image=self.End_turn_btn_image
        )

        self.canvas.tag_bind(End_turn_btn, "<ButtonRelease-1>", lambda x : self.End_turn_btn(End_turn_btn, root, button_pressed))

        self.map_instance = map_instance

        #Restarts the health of entities
        self.player.health = 10
        self.player.energy = 0


        self.Energy_lb = self.canvas.create_text(
            432.0,
            26.0,
            anchor="nw",
            text="Energy: " + str(self.player.energy),
            fill="#000000",
            font=("Inter ExtraBold", 20 * -1)
        )

        self.Health_lb = self.canvas.create_text(
            14.0,
            26.0,
            anchor="nw",
            text="Health: " + str(self.player.health) + "           Defence: " + str(self.player.defence),
            fill="#000000",
            font=("Inter ExtraBold", 20 * -1)
        )

        self.Health_Enemy_lb = self.canvas.create_text(
            293.0,
            121.0,
            anchor="nw",
            text="Health: " + str(self.enemy.health) + "           Defence: " + str(self.enemy.defence),
            fill="#000000",
            font=("Inter ExtraBold", 20 * -1)
        )

        #Give the first hand of cards
        self.card_counter = 0
        self.cards.clear()
        while self.card_counter <= 5:
            self.New_card(root, button_pressed)

        self.Open_question_window(root)

    #Open_question_window()
    #Open a question window
    #@param - self - the current instance of the class.
    #@param - tk.Tk - window - the battle window
    #@return - a question window
    def Open_question_window(self, window:tk.Tk):
        window.withdraw() #hides the battle window
        extra_window = tk.Toplevel()
        questions = math_questions_systems.MathQuizApp(extra_window) # creates a new question window
        questions.Battle_window = window # creates a reference to the battle window in the new window
        questions.Battle_instance = self # creates a reference to the main menu window in the new window
        questions.Map_instance = self.map_instance # creates a reference to the map class in the new window
        extra_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(extra_window, questions.Battle_window, self.Map_window))

    
    #on_closing()
    #A function to be called on when the user manually closes the 
    #@param - self - the current instance of the class.
    #@param - tk.Tk - map_window - the map window
    #@param - tk.Tk - battle_window - the battle window
    #@return - the main menu window appears
    def on_closing(self, question_window:tk.Tk, battle_window:tk.Tk, map_window:tk.Tk):
     if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.Main_window.deiconify()
        map_window.destroy()
        battle_window.destroy()
        question_window.destroy()
  
        

        
    #End_turn_btn()
    #Ends the turn of the user and performs the enemy's turn
    #@param - self - the current instance of the class.
    #@param - tk.button - button - the button pressed
    #@param - tk.Tk - window - the battle window
    #@param - int - button_pressed - the node pressed on the map window  
    def End_turn_btn(self, button: tk.Button, window:tk.Tk, button_pressed):
         self.enemy.defence = 0
         defended = 0
         attacked = 0
         while self.enemy.energy >= 1:
              match random.randint(0, 3): #randomly gets the enemy to attack or defend until their energy runs out
                 case 1:
                    self.attack(self.enemy, self.player)
                    attacked += 1
                 case 2:
                    self.defend(self.enemy)
                    defended += 1
                 case _:
                    self.attack(self.enemy, self.player)
                    attacked += 1
         self.enemy.energy = self.enemy.energy_limit #reseting the enemies energy and player's defence
         self.player.defence = 0
         self.canvas.itemconfig(self.Health_lb, text="Health: " + str(self.player.health) + "           Defence: " + str(self.player.defence))
         tkinter.messagebox.showinfo("Enemy's turn", "The enemy defended: " + str(defended) + "\nThe enemy attacked: " + str(attacked))
         for card in self.cards:
             card.destroy() #give the user a new hand of cards
         self.card_counter = 0
         self.cards.clear()
         while self.card_counter <= 5:
            self.New_card(window, button_pressed)
         if self.player.health > 0: #check if the player's health is 0
            self.Open_question_window(window) # opens a question window
         else:     
            button["state"] = "disabled" # disables the end_turn button
            tkinter.messagebox.showinfo("You lose", "your health has reached 0. GAME OVER")#if the users health reach 0
            extra_window = tk.Toplevel() 
            end = End_screen.End_window(extra_window, False, self.map_instance) # creates a end screen window
            end.home_window = self.Main_window # create a main menu reference in the new window
            self.Map_window.destroy()
            window.destroy()

        

    #attack()
    #Used to attack an entity
    #@param - self - the current instance of the class
    #@param - attacker - Entity - the attacking entity
    #@param - defender - Entity - the defending entity
    #@param - card - tk.Button - the card being used
    #@param - tk.Tk - window - the battle window
    #@param - int - button_pressed - the button pressed on the map window
    def attack(self, attacker: Entity, defender: Entity, card: tk.Button=None, window:tk.Tk=None, button_pressed: int=None):
         if attacker.energy > 0:
            if defender.defence > 0:
                defender.defence -= 1 # if the defender has a defence value
            else:
               defender.health -= 1 #if the defender has no defence value
            attacker.energy -= 1 #takes 1 away from the attacker energy
            if card != None: #sets the labels to the new values
                self.canvas.itemconfig(self.Health_Enemy_lb,text= "Health: " + str(defender.health) + "           Defence: " + str(defender.defence))
                self.canvas.itemconfig(self.Energy_lb, text="Energy: " + str(attacker.energy))
                card["state"] = "disabled"
            else:
                try:
                    self.canvas.itemconfig(self.Health_lb, text="Health: " + str(defender.health) + "           Defence: " + str(defender.defence))
                finally:
                    return
         if defender.health <= 0 and defender == self.enemy:
            tkinter.messagebox.showinfo("You win",  "the enemy's health has reached 0. You win") #if the enemies health reach 0
            if button_pressed == 9: #if the map button pressed was 9 (last button), open the you win window
                extra_window = tk.Toplevel()
                end = End_screen.End_window(extra_window, True, self.map_instance)
                end.home_window = self.Main_window
                end.Map_instance = self.map_instance
                self.Map_window.destroy()
                window.destroy()
            else:
                self.Map_window.deiconify() #reopens the map window
                window.destroy()
                
    #defend()
    #Used to defend an entity
    #@param - self - the current instance of the class
    #@param - defender - Entity - the defending entity
    #@param - card - tk.Button - the card being used
    def defend(self, defender: Entity, card: tk.Button=None):
         if defender.energy > 0:
            defender.defence += 1 # adds 1 to the defenders defence
            defender.energy -= 1
            if card != None: #sets the labels to the new values
                self.canvas.itemconfig(self.Health_lb, text="Health: " + str(defender.health) + "           Defence: " + str(defender.defence))
                self.canvas.itemconfig(self.Energy_lb, text="Energy: " + str(defender.energy))
                card["state"] = "disabled"
            else:
                try:
                    self.canvas.itemconfig(self.Health_Enemy_lb,text="Health: " + str(defender.health) + "           Defence: " + str(defender.defence))
                finally:
                    return             

    #heal()
    #Used to heal an entity
    #@param - self - the current instance of the class
    #@param - defender - Entity - the healing entity
    #@param - card - tk.Button - the card being used           
    def heal(self, defender: Entity, card: tk.Button=None):
         if defender.energy > 0:
            defender.health += 1 #adds 1 to the defenders health
            defender.energy -= 1
            self.canvas.itemconfig(self.Health_lb, text="Health: " + str(defender.health) + "           Defence: " + str(defender.defence))#sets the labels to the new values
            self.canvas.itemconfig(self.Energy_lb, text="Energy: " + str(defender.energy))
            card["state"] = "disabled"

    #New_card()
    #Used to create a random typed card
    #@param - self - the current instance of the class
    #@param - tk.Tk - window - the battle window
    #@param - int - button_pressed - the button pressed on the map window
    def New_card(self, window: tk.Tk, button_pressed):
        card = tk.Button(window, name="card_" + str(self.card_counter), bg="#f0f0f0", borderwidth=0, font=tkFont.Font(family='Helvetica',size=10), fg="#000000", justify="center")
        match random.randint(0, 3): #determines the type of card
                 case 0:
                    card["command"] = lambda: self.attack(self.player, self.enemy, card, window, button_pressed)
                    card["image"] = self.attack_picture_small
                 case 1:
                    card["command"] = lambda: self.defend(self.player, card)
                    card["image"] = self.defence_picture_small
                 case 2:
                    card["command"] = lambda: self.heal(self.player, card)
                    card["image"] = self.heal_picture_small
                 case _:
                    card["image"] = self.attack_picture_small
                    card["command"] = lambda: self.attack(self.player, self.enemy, card, window, button_pressed)

        self.cards.append(card)
        card.place(x=140 + self.card_counter*50 ,y=430,width=81,height=86)
        card.bind("<Enter>", lambda x: self.card_focus(card)) #attaches the focus and unfocus to the card on hover
        card.bind("<Leave>", lambda x: self.card_unfocus(card))
        self.card_counter += 1

    #relative_to_assets()
    #Used to create a path to a an asset
    #@Param - self - the current instance of the class
    #@Param - path - the path/file to be being located
    #@Return - a path to the asset
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)


