import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import random

#card_focus()
#this function is used to enlarge a card to make it stand out in the hand
#@param - button - tk.button - the card to be focused on
def card_focus(button: tk.Button):
        button.tkraise()
        button.place(y=330,width=162,height=172)

#card_unfocus()
#this function is used to return a card to its orignal size in the correct postion on the deck
#@param - button - tk.button - the card to be unfocused
def card_unfocus(button: tk.Button):
        card_num=int(str(button.winfo_name).split(".")[-1][-3]) #used to determine which layer the card should go on 
        if card_counter > 0 and card_num < card_counter - 1:
             card_below = cards[card_num + 1]
             button.lower(card_below)
        button.place(y=430,width=81,height=86)

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

#Entity
#A class for the battle encounter window
class Battle_Encounter:
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

        #Give the first hand of cards
        while card_counter <= 5:
            self.New_card()

        #End turn button
        End_turn_btn = tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center", text="End turn", command= lambda: self.End_turn_btn())
        End_turn_btn.place(x=250,y=20,width=70,height=25)

        #Restarts the health of entities
        enemy.health = 10
        player.health = 10
        
    #End_turn_btn()
    #Ends the turn of the user and performs the enemy's turn
    def End_turn_btn(self):
         enemy.defence = 0
         while enemy.energy >= 1:
              match random.randint(0, 3): #randomly gets the enemy to attack or defend until their energy runs out
                 case 1:
                    self.attack(enemy, player)
                 case 2:
                    self.defend(enemy)
                 case _:
                    self.attack(enemy, player)
         enemy.energy = 4
         player.energy = 4 #resets both of entities energy
         player.defence = 0
         global cards
         for card in cards:
             card.destroy() #give the user a new hand of cards
         global card_counter 
         card_counter = 0
         while card_counter <= 5:
            self.New_card()

    #attack()
    #Used to attack an entity
    #@param - attacker - Entity - the attacking entity
    #@param - defender - Entity - the defending entity
    #@param - card - tk.Button - the card being used
    def attack(self, attacker: Entity, defender: Entity, card: tk.Button=None):
         if attacker.energy > 0:
            if defender.defence > 0:
                defender.defence -= 1 # if the defender has a defence value
            else:
               defender.health -= 1 #if the defender has no defence value
            attacker.energy -= 1 #takes 1 away from the attacker energy
            if defender.health == 0 and defender == enemy:
                tkinter.messagebox.showinfo("You win",  "the enemy's health has reached 0. You win") #if the enemies health reach 0
                root.destroy()
            elif defender.health == 0:
                tkinter.messagebox.showinfo("You lose", "your health has reached 0. GAME OVER")#if the users health reach 0
                root.destroy()
            if card != None: #sets the labels to the new values
                Health_Enemy_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                Energy_lb["text"] = "Energy: " + str(attacker.energy)
                card["state"] = "disabled"
            else:
                try:
                    Health_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                finally:
                    return
                
    #defend()
    #Used to defend an entity
    #@param - defender - Entity - the defending entity
    #@param - card - tk.Button - the card being used
    def defend(self, defender: Entity, card: tk.Button=None):
         if defender.energy > 0:
            defender.defence += 1 # adds 1 to the defenders defence
            defender.energy -= 1
            if card != None: #sets the labels to the new values
                Health_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                Energy_lb["text"] = "Energy: " + str(defender.energy)
                card["state"] = "disabled"
            else:
                try:
                    Health_Enemy_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
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
            Health_lb["text"] = "Health: " + str(defender.health) + "defence: " + str(defender.defence) #sets the labels to the new values
            Energy_lb["text"] = "Energy: " + str(defender.energy)
            card["state"] = "disabled"

    #New_card()
    #Used to create a random typed card
    def New_card(self):
        global card_counter
        card_type = 0
        card = tk.Button(root, name="card_" + str(card_counter), bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center")
        match random.randint(0, 3): #determines the type of card
                 case 0:
                    card["text"] = "Attack"
                    card["command"] = lambda: self.attack(player, enemy, card)
                 case 1:
                    card["text"] = "Defend"
                    card["command"] = lambda: self.defend(player, card)
                 case 2:
                    card["text"] = "Heal"
                    card["command"] = lambda: self.heal(player, card)
                 case _:
                    card["text"] = "Attack"
                    card["command"] = lambda: self.attack(player, enemy, card)

        cards.append(card)
        card.place(x=140 + card_counter*50 ,y=430,width=81,height=86)
        card.bind("<Enter>", lambda x: card_focus(card)) #attaches the focus and unfocus to the card on hover
        card.bind("<Leave>", lambda x: card_unfocus(card))
        card_counter += 1
            

if __name__ == "__main__":
    player = Entity() #creates the player and enemy
    enemy = Entity()
    card_counter = 0
    cards = []
    root = tk.Tk()
    app = Battle_Encounter(root)

    Health_lb=tk.Label(root, font=tkFont.Font(family='Times',size=10),fg="#333333", justify="left", text= "Health: " + str(player.health) + " defence: " + str(player.defence))
    Health_lb.place(x=10,y=20,width=170,height=25) #creates the player health label

    Health_Enemy_lb=tk.Label(root, font=tkFont.Font(family='Times',size=10),fg="#333333", justify="left", text= "Health: " + str(enemy.health) + " defence: " + str(enemy.defence))
    Health_Enemy_lb.place(x=380,y=160,width=170,height=25) #creates the eneny health label

    Energy_lb=tk.Label(root, font=tkFont.Font(family='Times',size=10),fg="#333333", justify="right", text="Energy: " + str(player.energy))
    Energy_lb.place(x=500,y=20,width=70,height=25) #creates the player energy label
    root.mainloop()
