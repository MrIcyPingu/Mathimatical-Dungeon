import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import random


#Entity
#A class for the creation of entities that will be used the battle encounter
#@param - health - int - the life points of the entity to see if is dead
#@param - defence - int - how much defence does the entity have
#@param - energy_limit - int - the maximum amount of energy the entity can have
#@param - energy - int - the current amount of energy the entity has.
class Entity:
     health = 10
     defence = 0
     energy_limit = 4
     energy = 4

#Battle_Encounter
#A class for the battle encounter window
class Battle_Encounter():
    player = Entity() #creates the player and enemy
    enemy = Entity()
    card_counter = 0
    cards = []

    #card_focus()
    #this function is used to enlarge a card to make it stand out in the hand
    #@param - button - tk.button - the card to be focused on
    def card_focus(self, button: tk.Button):
            button.tkraise()
            button.place(y=330,width=162,height=172)

    #card_unfocus()
    #this function is used to return a card to its orignal size in the correct postion on the deck
    #@param - button - tk.button - the card to be unfocused
    def card_unfocus(self, button: tk.Button):
            card_num=int(str(button.winfo_name).split(".")[-1][-3]) #used to determine which layer the card should go on 
            if self.card_counter > 0 and card_num < self.card_counter - 1:
                card_below = self.cards[card_num + 1]
                button.lower(card_below)
            button.place(y=430,width=81,height=86)

    def __init__(self, root):
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

        #Hero picture
        hero_frame = tk.Frame(root, width=128,height=184, borderwidth=2, relief="groove")
        hero_frame.place(x=60,y=140)

        #Enemy picture
        enemy_frame = tk.Frame(root, width=128,height=184, borderwidth=2, relief="groove")
        enemy_frame.place(x=420,y=140)

        #Restarts the health of entities
        self.enemy.health = 10
        self.player.health = 10

        self.Health_lb=tk.Label(root, font=tkFont.Font(family='Times',size=10),fg="#333333", justify="left", text= "Health: " + str(self.player.health) + " defence: " + str(self.player.defence))
        self.Health_lb.place(x=10,y=20,width=170,height=25) #creates the player health label

        self.Health_Enemy_lb=tk.Label(root, font=tkFont.Font(family='Times',size=10),fg="#333333", justify="left", text= "Health: " + str(self.enemy.health) + " defence: " + str(self.enemy.defence))
        self.Health_Enemy_lb.place(x=380,y=160,width=170,height=25) #creates the eneny health label

        self.Energy_lb=tk.Label(root, font=tkFont.Font(family='Times',size=10),fg="#333333", justify="right", text="Energy: " + str(self.player.energy))
        self.Energy_lb.place(x=500,y=20,width=70,height=25) #creates the player energy label

        #Give the first hand of cards
        self.card_counter = 0
        self.cards.clear()
        while self.card_counter <= 5:
            self.New_card(root)

        #End turn button
        End_turn_btn = tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center", text="End turn", command= lambda: self.End_turn_btn(root))
        End_turn_btn.place(x=250,y=20,width=70,height=25)

        
    #End_turn_btn()
    #Ends the turn of the user and performs the enemy's turn
    def End_turn_btn(self, window:tk.Tk):
         self.enemy.defence = 0
         while self.enemy.energy >= 1:
              match random.randint(0, 3): #randomly gets the enemy to attack or defend until their energy runs out
                 case 1:
                    self.attack(self.enemy, self.player)
                 case 2:
                    self.defend(self.enemy)
                 case _:
                    self.attack(self.enemy, self.player)
         self.enemy.energy = 4
         self.player.energy = 4 #resets both of entities energy
         self.Energy_lb["text"] = "Energy: " + str(self.player.energy)
         self.player.defence = 0
         self.Health_lb["text"] = "Health: " + str(self.player.health) + " defence: " + str(self.player.defence)
         for card in self.cards:
             card.destroy() #give the user a new hand of cards
         self.card_counter = 0
         self.cards.clear()
         while self.card_counter <= 5:
            self.New_card(window)
         if self.player.health <= 0:
                tkinter.messagebox.showinfo("You lose", "your health has reached 0. GAME OVER")#if the users health reach 0
                window.destroy()
        

    #attack()
    #Used to attack an entity
    #@param - attacker - Entity - the attacking entity
    #@param - defender - Entity - the defending entity
    #@param - card - tk.Button - the card being used
    def attack(self, attacker: Entity, defender: Entity, card: tk.Button=None, window:tk.Tk=None):
         if attacker.energy > 0:
            if defender.defence > 0:
                defender.defence -= 1 # if the defender has a defence value
            else:
               defender.health -= 1 #if the defender has no defence value
            attacker.energy -= 1 #takes 1 away from the attacker energy
            if card != None: #sets the labels to the new values
                self.Health_Enemy_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                self.Energy_lb["text"] = "Energy: " + str(attacker.energy)
                card["state"] = "disabled"
            else:
                try:
                    self.Health_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                finally:
                    return
         if defender.health <= 0 and defender == self.enemy:
            tkinter.messagebox.showinfo("You win",  "the enemy's health has reached 0. You win") #if the enemies health reach 0  
            window.destroy()
                
    #defend()
    #Used to defend an entity
    #@param - defender - Entity - the defending entity
    #@param - card - tk.Button - the card being used
    def defend(self, defender: Entity, card: tk.Button=None):
         if defender.energy > 0:
            defender.defence += 1 # adds 1 to the defenders defence
            defender.energy -= 1
            if card != None: #sets the labels to the new values
                self.Health_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                self.Energy_lb["text"] = "Energy: " + str(defender.energy)
                card["state"] = "disabled"
            else:
                try:
                    self.Health_Enemy_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                finally:
                    return             

    #heal()
    #Used to heal an entity
    #@param - defender - Entity - the healing entity
    #@param - card - tk.Button - the card being used           
    def heal(self, defender: Entity, card: tk.Button=None):
         if defender.energy > 0:
            defender.health += 1 #adds 1 to the defenders health
            defender.energy -= 1
            self.Health_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence) #sets the labels to the new values
            self.Energy_lb["text"] = "Energy: " + str(defender.energy)
            card["state"] = "disabled"

    #New_card()
    #Used to create a random typed card
    def New_card(self, window: tk.Tk):
        card = tk.Button(window, name="card_" + str(self.card_counter), bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center")
        match random.randint(0, 3): #determines the type of card
                 case 0:
                    card["text"] = "Attack"
                    card["command"] = lambda: self.attack(self.player, self.enemy, card, window)
                 case 1:
                    card["text"] = "Defend"
                    card["command"] = lambda: self.defend(self.player, card)
                 case 2:
                    card["text"] = "Heal"
                    card["command"] = lambda: self.heal(self.player, card)
                 case _:
                    card["text"] = "Attack"
                    card["command"] = lambda: self.attack(self.player, self.enemy, card)

        self.cards.append(card)
        card.place(x=140 + self.card_counter*50 ,y=430,width=81,height=86)
        card.bind("<Enter>", lambda x: self.card_focus(card)) #attaches the focus and unfocus to the card on hover
        card.bind("<Leave>", lambda x: self.card_unfocus(card))
        self.card_counter += 1


