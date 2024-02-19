import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import random

def card_focus(button: tk.Button):
        button.tkraise()
        button.place(y=330,width=162,height=172)

def card_unfocus(button: tk.Button):
        card_num=int(str(button.winfo_name).split(".")[-1][-3])
        if card_counter > 0 and card_num < card_counter - 1:
             card_below = cards[card_num + 1]
             button.lower(card_below)
        button.place(y=430,width=81,height=86)

class Entity:
     health = 10
     defence = 0
     energy_limit = 4
     energy = 4


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

        hero_frame = tk.Frame(root, width=128,height=184, borderwidth=2, relief="groove")
        hero_frame.place(x=60,y=140)

        enemy_frame = tk.Frame(root, width=128,height=184, borderwidth=2, relief="groove")
        enemy_frame.place(x=420,y=140)

        while card_counter <= 5:
            self.New_card()

        End_turn_btn = tk.Button(root, bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center", text="End turn", command= lambda: self.End_turn_btn())
        End_turn_btn.place(x=250,y=20,width=70,height=25)

        enemy.health = 10
        player.health = 10
        


    def End_turn_btn(self):
         enemy.defence = 0
         while enemy.energy >= 1:
              match random.randint(0, 3):
                 case 1:
                    self.attack(enemy, player)
                 case 2:
                    self.defend(enemy)
                 case _:
                    self.attack(enemy, player)
         enemy.energy = 4
         player.energy = 4
         player.defence = 0
         global cards
         for card in cards:
             card.destroy()
         global card_counter 
         card_counter = 0
         while card_counter <= 5:
            self.New_card()


    def attack(self, attacker: Entity, defender: Entity, card: tk.Button=None):
         if attacker.energy > 0:
            if defender.defence > 0:
                defender.defence -= 1
            else:
               defender.health -= 1
            attacker.energy -= 1
            if defender.health == 0 and defender == enemy:
                tkinter.messagebox.showinfo("You win",  "the enemy's health has reached 0. You win")
                root.destroy()
            elif defender.health == 0:
                tkinter.messagebox.showinfo("You lose", "your health has reached 0. GAME OVER")
                root.destroy()
            if card != None:
                Health_Enemy_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                Energy_lb["text"] = "Energy: " + str(attacker.energy)
                card["state"] = "disabled"
            else:
                try:
                    Health_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                finally:
                    return
                

    def defend(self, defender: Entity, card: tk.Button=None):
         if defender.energy > 0:
            defender.defence += 1
            defender.energy -= 1
            if card != None:
                Health_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                Energy_lb["text"] = "Energy: " + str(defender.energy)
                card["state"] = "disabled"
            else:
                try:
                    Health_Enemy_lb["text"] = "Health: " + str(defender.health) + " defence: " + str(defender.defence)
                finally:
                    return
                
    def heal(self, defender: Entity, card: tk.Button=None):
         if defender.energy > 0:
            defender.health += 1
            defender.energy -= 1
            Health_lb["text"] = "Health: " + str(defender.health) + "defence: " + str(defender.defence)
            Energy_lb["text"] = "Energy: " + str(defender.energy)
            card["state"] = "disabled"
         
    def New_card(self):
        global card_counter
        card_type = 0
        card = tk.Button(root, name="card_" + str(card_counter), bg="#f0f0f0", font=tkFont.Font(family='Times',size=10), fg="#000000", justify="center")
        match random.randint(0, 3):
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
        card.bind("<Enter>", lambda x: card_focus(card))
        card.bind("<Leave>", lambda x: card_unfocus(card))
        card_counter += 1
            

if __name__ == "__main__":
    player = Entity()
    enemy = Entity()
    card_counter = 0
    cards = []
    root = tk.Tk()
    app = Battle_Encounter(root)

    Health_lb=tk.Label(root, font=tkFont.Font(family='Times',size=10),fg="#333333", justify="left", text= "Health: " + str(player.health) + " defence: " + str(player.defence))
    Health_lb.place(x=10,y=20,width=170,height=25)

    Health_Enemy_lb=tk.Label(root, font=tkFont.Font(family='Times',size=10),fg="#333333", justify="left", text= "Health: " + str(enemy.health) + " defence: " + str(enemy.defence))
    Health_Enemy_lb.place(x=380,y=160,width=170,height=25)

    Energy_lb=tk.Label(root, font=tkFont.Font(family='Times',size=10),fg="#333333", justify="right", text="Energy: " + str(player.energy))
    Energy_lb.place(x=500,y=20,width=70,height=25)
    root.mainloop()
