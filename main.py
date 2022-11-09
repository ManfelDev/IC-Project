import random #Random library

#############
# VARIABLES #
#############
command = "" #Initial command for input

#########
# SQUAD #
#########
#Warrior
warrior = [32,5,2,5,2] #HP, MP , AP, WP, Init 
WarriorTurnOrder = 0 #Initial warrior turn order number
warrior_dmg = 0 #Setting floor for the warrior dmg

#Priest
priest = [20,25,0,2,6] #HP, MP , AP, WP, Init 
PriestTurnOrder = 0 #Setting floor for the priest turn order
priest_dmg = 0 #Setting floor for the priest dmg

###########
# ENEMIES #
###########
#Vampire
vampire = [15,0,2,2,2] #HP, MP, AP, WP, Init
vampire_dmg = 0 #Setting floor for the vampire dmg


###############
# TURN ORDERS #
###############
enemy_turnOrder = 0 #Initial enemy turn order number

def initiative_phase(): #Function for setting the turn order
    #Variables for get in action phase
    global WarriorTurnOrder
    global PriestTurnOrder
    global enemy_turnOrder

    #Variables to reset the score
    WarriorTurnOrder = 0
    PriestTurnOrder = 0
    enemy_turnOrder = 0
    
    #Cal the results to who goes first
    WarriorTurnOrder = WarriorTurnOrder + random.randint(0,20) + warrior[4] #Random Value for the Warrior's turn number
    PriestTurnOrder = PriestTurnOrder + random.randint(0,20) + priest[4] #Random Value for the Priest's turn number
    enemy_turnOrder = enemy_turnOrder + random.randint(0,20) + vampire[4] #Random Value for the Vampire's turn number
    
    #Print the results
    print("\nThe warrior got " + str(WarriorTurnOrder)) 
    print("The vampire got " + str(enemy_turnOrder))
    print("The priest got " + str(PriestTurnOrder))

    #Start Action phase with the numbers cal    
    action_phase()
    
#Attack from the warrior
def warrior_attack(): #If the vampire got the armor up
    if vampire [2] > 0: #If the vampire got the armor up, then attack the armor
        vampire[2] = vampire[2] - random.randrange(warrior[3])
        if vampire[2] > 0:
            print("You damaged the enemy armor! Enemy's current armor :" + str(vampire[2]))
        elif vampire[2] <= 0:
            print("You have destroyed the enemy armor!")
    elif vampire[2] <= 0: #If the vampire got no armor, then attack life
        vampire[0] = vampire[0] - random.randrange(warrior[3])
        print("You hit the enemy, enemy current life: " + str(vampire[0]))
    
    return vampire

#Attack from the priest
def priest_attack():
    if vampire [2] > 0: #If the vampire got the armor up
        vampire[2] = vampire[2] - random.randrange(warrior[3])
        if vampire[2] > 0:
            print("You damaged the enemy armor! Enemy's current armor :" + str(vampire[2]))
        elif vampire[2] <= 0:
            print("You have destroyed the enemy armor!")
    elif vampire[2] <= 0: #If the vampire got no armor, attack life
        vampire[0] = vampire[0] - random.randrange(priest[3])
        print("You hit the enemy, enemy current life: " + str(vampire[0]))

#Attack from the enemy
def enemy_attack():
    if warrior[2] > 0: #If the warrior got the armor up
        warrior[2] = warrior[2] - random.randrange(vampire[3])
        print("Your warrior got the armor damaged!")
    elif warrior[2] <= 0:
        warrior[0] = warrior[0] - random.randrange(vampire[3])
        print("Your warrior got attacked, his current life is: " + str(warrior[0]))
    elif warrior[0] <= 0: #If the warrior is dead
        print("Your warrior got killed!") 
    elif warrior[0] <= 0 and priest[2] > 0:
        priest[2] = priest[2] - random.randrange(vampire[3])
        print("Your priest got the armor damaged")
    
#######################
# COMBAT ACTION PHASE #
#######################
def action_phase():
    def warrior_turn():
            command = input("\nWarrior is playing: " +
                            "\nChoose your action" + 
                            "\n1. Attack." +
                            "\n2. Magic.\n")
            if command == "1":
                warrior_attack()
           # elif command == "2":
                #magic()
            else:
                print("Enter a correct action!")
                warrior_turn()
    def priest_turn():
            command = input("\nPriest is playing: " +
                            "\nChoose your action" + 
                            "\n1. Attack." +
                            "\n2. Magic.\n")
            if command == "1":
                warrior_attack()
            #elif command == "2":
            #    magic()
            else:
                print("Enter a correct action!")
                priest_turn()
    
    def enemy_turn():            
            print("\nThe enemy will play.")
            enemy_attack()
    
    def first_turn():
        if (WarriorTurnOrder > enemy_turnOrder) and (WarriorTurnOrder > PriestTurnOrder): #Warrior first
            warrior_turn()
        elif (PriestTurnOrder > enemy_turnOrder) and (PriestTurnOrder > WarriorTurnOrder): #Priest first
            priest_turn()
        elif (enemy_turnOrder > WarriorTurnOrder) and (enemy_turnOrder > PriestTurnOrder): #Enemy goes first
            enemy_turn()
        elif (WarriorTurnOrder == enemy_turnOrder) or (WarriorTurnOrder == PriestTurnOrder): #In case of draw return to turn order
            initiative_phase()
        elif (PriestTurnOrder == enemy_turnOrder) or (PriestTurnOrder == WarriorTurnOrder): #In case of draw return to turn order
            initiative_phase()
        elif (enemy_turnOrder == WarriorTurnOrder) or (enemy_turnOrder == PriestTurnOrder): #In case of draw return to turn
            initiative_phase()
            
    def second_turn():
        if (WarriorTurnOrder > enemy_turnOrder) and (WarriorTurnOrder < PriestTurnOrder): #Warrior second
            warrior_turn()
        elif (PriestTurnOrder > enemy_turnOrder) and (PriestTurnOrder < WarriorTurnOrder): #Priest second
            priest_turn()
        elif (enemy_turnOrder > WarriorTurnOrder) and (enemy_turnOrder < PriestTurnOrder): #Enemy second
            enemy_turn()
    
    def third_turn():
        if (WarriorTurnOrder < enemy_turnOrder) and (WarriorTurnOrder < PriestTurnOrder): #Warrior third
            warrior_turn()
        elif (PriestTurnOrder < enemy_turnOrder) and (PriestTurnOrder < WarriorTurnOrder): #Priest third
            priest_turn()
        else: #Enemy third
            enemy_turn()
             
    while (warrior[0] > 0 and priest[0] > 0) and vampire[0] > 0: #Loop until all of the group die or the enemy dies
        first_turn() #Execute the first turn
        if (warrior[0] > 0 and priest[0] > 0) and vampire[0] > 0:
            second_turn() #Execute the second turn
        if (warrior[0] > 0 and priest[0] > 0) and vampire[0] > 0:
            third_turn() #Execute the third turn
        if (warrior[0] > 0 and priest[0] > 0) and vampire[0] > 0:
            initiative_phase()
        elif (warrior[0] <= 0 and priest[0] <= 0): #All the player's characters die
            print("You have died! Better luck next time.")
            break
        elif vampire[0] <= 0: #The enemy die
            print("You have killed the vampire! Continue your journey.")
            break
        else:
            break

if (warrior[0] > 0 and priest[0] > 0) and vampire[0] > 0: #Check all are alive to start the battle
    initiative_phase()