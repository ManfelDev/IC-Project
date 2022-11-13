import random #Random library - can set random numbers
import time #Time library - can site time to do a action
import os #Let he work with operating system functions

os.system('clear') #Clear the previous console information and messages

#####################################################
# LITTLE EXPLAIN OF THE CHARACTERS' CHARACTERISTICS #
#####################################################
#Hit-Points (HP): Symbolizes the amount of life the character has until he falls unconscious
#Mana-Points (MP): Symbolizes the resource used to create and cast spells
#Armor Points (AP): Symbolizes the amount of damage that is subtracted after an attack
#Weapon (WP): Symbolizes the amount of damage this character does after an attack
#Initiative (Init): Symbolizes how quickly this character can do an action

#############
# VARIABLES #
#############
command = "" #Initial command for input
index = 0 #Form zero from the index
map = (["A","B","C"],["D","E","F"],["G","H","I"]) #Map rooms
x,y = 1,1 #Initial position

#########
# SQUAD #
#########
#Warrior
warrior = [32,5,2,5,2] #HP, MP , AP, WP, Init 
WarriorTurnOrder = 0 #Floor for the warrior's turn order number
warrior_dmg = int
warrior_SpellCost = 5 #Warrior cost to do the spell RushDown

#Priest
priest = [20,25,0,2,6] #HP, MP , AP, WP, Init 
PriestTurnOrder = 0 #Floor for the priest's turn order number
priest_dmg = int
priest_Exorcism_SpellCost = 5 #Exorcism spell cost
priest_Mend_SpellCost = 3 #Mend spell cost

###########
# ENEMIES #
###########
#vampires
vampires = [[15,0,2,3,2],[15,0,2,3,2],[15,0,2,3,2],[15,0,2,3,2]] #HP, MP, AP, WP, Init
vampire_dmg = int
vampiresTurnOrder = 0 #Initial enemy turn order number


###########################
# COMBAT INITIATIVE PHASE #
###########################
def combat():
    def initiative_phase(): #Function for setting the turn order
        os.system('clear') #Clear the previous console information and messages
        #Variables for get in action phase
        global WarriorTurnOrder
        global PriestTurnOrder
        global vampiresTurnOrder

        #Variables to reset the score
        WarriorTurnOrder = 0
        PriestTurnOrder = 0
        vampiresTurnOrder = 0
        
        #Cal the results to who goes first
        WarriorTurnOrder = WarriorTurnOrder + random.randint(1,20) + warrior[4] #Random Value for the Warrior's turn number TurnOrder = d20 + warrior Init
        PriestTurnOrder = PriestTurnOrder + random.randint(1,20) + priest[4] #Random Value for the Priest's turn number TurnOrder = d20 + priest Init
        vampiresTurnOrder = vampiresTurnOrder + random.randint(1,20) + vampires[0][4] #Random Value for the vampires's turn number TurnOrder = d20 + vampires Init
        
        #Print the results
        print("\033[1;37mA round has started:\n")
        print("\033[1;37mThe warrior got \033[1;36m" + str(WarriorTurnOrder))
        print("\033[1;37mThe priest got \033[1;36m" + str(PriestTurnOrder))
        print("\033[1;37mThe vampires got \033[1;36m" + str(vampiresTurnOrder))

        input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        
        #Start Action phase with the numbers calculated
        action_phase()
        
    ##########################
    # WARRIOR COMBAT ACTIONS #
    ##########################    
    #Attack from the warrior
    def warrior_attack(index): #If the vampires got the armor up
        command = input("\n\033[1;34mWhich enemy do you want to attack?: " +
                                        "\n\033[1;37m1. \033[1;31mVampire 1" + 
                                        "\n\033[1;37m2. \033[1;31mVampire 2" +
                                        "\n\033[1;37m3. \033[1;31mVampire 3" +
                                        "\n\033[1;37m4. \033[1;31mVampire 4\033[1;37m\n") 
                        #Let the player select what enemy he want's to attack
        if command == "1": #Vampire 1
            index = 0 
            warrior_do_attack(index) 
        elif command == "2": #Vampire 2
            index = 1
            warrior_do_attack(index) 
        elif command == "3": #Vampire 3
            index = 2
            warrior_do_attack(index) 
        elif command == "4": #Vampire 4
            index = 3
            warrior_do_attack(index)
        else: #If the player put a wrong input
            print("\033[1;31mChoose a right target!")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
            warrior_attack(index)
            
        return index

    def warrior_do_attack(index):
        warrior_dmg = warrior[3] - vampires[index][2] #Warrior damage: warrior's WP - vampires AP
        if vampires[index][0] > 0: #If vampire is alive
            vampires[index][0] = vampires[index][0] - warrior_dmg #Enemy's HP less the warrior's WP - the vampires AP
            if vampires[index][0] > 0: #If vampire's still alive after the attack:
                print("\n\033[1;37mYou have hit the enemy, enemy's current life:\033[1;31m " + str(vampires[index][0])) #Print the enemy current life
                input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
            else: #If the vampire's dead, after the attack:
                print("\n\033[1;31mYou have killed vampire " + str(index + 1) + "!")
                input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        else: #If the vampires selected is dead:
            print("\nThe vampire " + (str(index + 1)) + " is dead, choose another target!")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
            warrior_attack(index) #Return to warrior's attack selection
            
        return index

    #RushDown spell from the warrior  
    def warrior_spell(index): #Function for the Warrior Spell
        command = input("\n\033[1;34mWhich enemy do you want to do the spell?: " +
                                    "\n\033[1;37m1. \033[1;31mVampire 1" + 
                                    "\n\033[1;37m2. \033[1;31mVampire 2" +
                                    "\n\033[1;37m3. \033[1;31mVampire 3" +
                                    "\n\033[1;37m4. \033[1;31mVampire 4\033[1;37m\n")
                                #Let the player select what enemy he want's to do the spell
        if command == "1": #Vampire 1
            index = 0
            warrior_rushDown(index)
        elif command == "2": #Vampire 2
            index = 1
            warrior_rushDown(index)
        elif command == "3": #Vampire 3
            index = 2
            warrior_rushDown(index)
        elif command == "4": #Vampire 4
            index = 3
            warrior_rushDown(index)
        else:
            print("\033[1;31mChoose a right target!")
        
        return index

    def warrior_rushDown(index):
        d4 = random.randint(1,4) #Four-sided dice
        SpellEffectValue = -1 * (warrior[3] + d4) #Spell effect and the respective damage
        if vampires[index][0] > 0: #If vampire if alive
            vampires[index][0] = vampires[index][0] + SpellEffectValue #Damage gave to the enemy
            warrior[1] = warrior[1] - warrior_SpellCost #Take of MP points after the spell
            if vampires[index][0] > 0:
                print("\n\033[1;37mYou have hit the enemy, enemy's current life:\033[1;31m " + str(vampires[index][0]))
                input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
            else:
                print("\n\033[1;31mYou have killed vampire " + str(index + 1)+ "!")
                input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        else: #If vampire is dead:
            print("\nThe vampire " + (str(index + 1)) + " is dead, choose another target!")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
            warrior_spell(index) #Return to warrior's target select
            
        return index

    #########################
    # PRIEST COMBAT ACTIONS #
    #########################
    #Attack from the priest
    def priest_attack(index): #If the vampires got the armor up
        command = input("\n\033[1;34mWhich enemy do you want to attack?: " +
                                    "\n\033[1;37m1. \033[1;31mVampire 1" + 
                                    "\n\033[1;37m2. \033[1;31mVampire 2" +
                                    "\n\033[1;37m3. \033[1;31mVampire 3" +
                                    "\n\033[1;37m4. \033[1;31mVampire 4\033[1;37m\n")
                        #Let the player select what enemy he want's to attack
        if command == "1": #Vampire 1
            index = 0 
            priest_do_attack(index)
        elif command == "2": #Vampire 2
            index = 1
            priest_do_attack(index)
        elif command == "3": #Vampire 3
            index = 2
            priest_do_attack(index)
        elif command == "4": #Vampire 4
            index = 3
            priest_do_attack(index)
        else: # If the player put a wrong input
            print("\033[1;31mChoose a right target!")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
            priest_attack(index)
            
        return index

    def priest_do_attack(index):
        priest_dmg = priest[3] - vampires[index][2] #Priest damage: priest WP - enemy AP
        if priest_dmg <= vampires[index][2]: #If priest damage <= enemy's AP
            print("\n\033[1;31mYou have attacked the enemy but you are to weak to damage him! Try to use a spell next time.")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        elif priest_dmg > vampires[index][2]: #If priest damage > enemy's AP
            if vampires[index][0] > 0: #If the vampire's still alive
                vampires[index][0] = vampires[index][0] - priest_dmg #Do the damage to the enemy life
                if vampires[index][0] > 0: #If the enemy's still alive after the attack:
                    print("\n\033[1;37mYou have hit the enemy, enemy's current life:\033[1;31m " + str(vampires[index][0])) #Print the enemy current life
                    input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
                else: #If the enemy's dead after the attack:
                    print("\n\033[1;31mYou have killed vampire " + str(index + 1)+ "!")
                    input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
            else: #If the vampires selected is dead
                print("\nThe vampires " + (str(index + 1)) + " is dead, choose another target!")
                input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
                priest_attack(index) #Returns to priest attack selection
            
        return index

    #Exorcism spell from the priest
    def priest_spell_exorcism(index): #Function for the Warrior Spell
        command = input("\n\033[1;34mWhich enemy do you want to do the spell?: " +
                                    "\n\033[1;37m1. \033[1;31mVampire 1" + 
                                    "\n\033[1;37m2. \033[1;31mVampire 2" +
                                    "\n\033[1;37m3. \033[1;31mVampire 3" +
                                    "\n\033[1;37m4. \033[1;31mVampire 4\033[1;37m\n")
                                #Let the player select what enemy he want's to do the spell
        if command == "1": #Vampire 1
            index = 0
            priest_exorcism(index)
        elif command == "2": #Vampire 2
            index = 1
            priest_exorcism(index)
        elif command == "3": #Vampire 3
            index = 2
            priest_exorcism(index)
        elif command == "4": #Vampire 4
            index = 3
            priest_exorcism(index)
        else:
            print("\033[1;31mChoose a right target!")
        
        return index

    def priest_exorcism(index):
        d4 = random.randint(1,4) #Four-sided dice
        SpellEffectValue = -1 * (d4 * 2) #Spell effect and the respective damage
        if vampires[index][0] > 0: #If vampire if alive
            vampires[index][0] = vampires[index][0] + SpellEffectValue #Damage gave to the enemy
            priest[1] = priest[1] - priest_Exorcism_SpellCost #Take of MP points after the spell
            if vampires[index][0] > 0: #If the enemy is still alive after the attack:
                print("\n\033[1;37mYou have hit the enemy, enemy's current life:\033[1;31m " + str(vampires[index][0]))
                input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
            else: #If the enemy is dead after the attack:
                print("\n\033[1;31mYou have killed vampire " + str(index + 1)+ "!")
                input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        else: #If vampire is dead:
            print("\nThe vampire " + (str(index + 1)) + " is dead, choose another target!")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
            priest_spell_exorcism(index)#Return to warrior's target select
            
        return index

    #Mend spell from the priest
    def priest_spell_mend():
        d6 = random.randint(1,6) #Four-sided dice
        SpellEffectValue = d6 + priest[3] #Spell effect and the respective damage
        warrior[0] = warrior[0] + SpellEffectValue #Damage gave to the enemy
        priest[1] = priest[1] - priest_Mend_SpellCost #Take of MP points after the spell
        print("\n\033[1;37mYou have healed the warrior! Warrior's current life:\033[1;32m", warrior[0])
        input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game


    ########################
    # ENEMY COMBAT ACTIONS #
    ########################
    #Attack from the enemy, warrior is attack first because he is in front
    def enemy_attack(): 
        if warrior[0] > 0: #If the warrior is alive:
            vampire_dmg = vampires[0][3] - warrior[2] #Vampire's damage to warrior, vampires WP - warrior AP
            warrior[0] = warrior[0] - vampire_dmg #vampire damage the warrior's HP
            if warrior[0] > 0: #If warrior's still alive:
                print("\033[1;37mYour warrior got attacked, his current life is: \033[1;31m" + str(warrior[0]))
            elif warrior[0] <= 0: #If the warrior got killed:
                print("\033[1;31mYour warrior got killed!")
        elif priest[0] > 0: #If the warrior is dead then attack the priest:
            vampire_dmg = vampires[0][3] - priest[2] #Vampire's damage to priest
            priest[0] = priest[0] - vampire_dmg
            if priest[0] > 0: #If priest's still alive:
                print("\033[1;37mYour priest got attacked, his current life is: \033[1;31m" + str(priest[0]))
            elif priest[0] <= 0: #If the priest got killed:
                print("\033[1;37mYour priest got killed!")
        
    #######################
    # COMBAT ACTION PHASE #
    #######################
    def action_phase():
        def warrior_turn():
                command = input("\n\033[1;37mWarrior is playing: " +
                                "\n\033[1;34mChoose your action" + 
                                "\n\033[1;37m1. Attack - Damages the enemy" +
                                "\n\033[1;37m2. Spell - RushDown (Damages the enemy) Needs\033[1;34m " + str(warrior_SpellCost) + "\033[1;37m mana points" +
                                "\n\033[1;37m------------------ Current mana points: \033[1;34m" + str(warrior[1]) +"\033[1;37m ------------------\n")
                if command == "1": #Execute the warrior attack
                        warrior_attack(index)
                elif command == "2": #Execute the warrior spell
                    if warrior[1] >= warrior_SpellCost: #If the warrior got the MP suf to do the spell
                        warrior_spell(index) #Warrior spell, RushDown
                    else: #If the warrior got no MP suf to do the spell
                        print("\n\033[1;31mYou have no more mana points to do this spell!")
                        input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
                        warrior_turn() #Return to priest turn
                else: #If player doesn't choose a available option
                    print("\n\033[1;31mChoose a right action!")
                    input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
                    warrior_turn()
                
        def priest_turn():
                command = input("\n\033[1;37mPriest is playing: " +
                                "\n\033[1;34mChoose your action" + 
                                "\n\033[1;37m1. Attack" +
                                "\n\033[1;37m2. Spell - Exorcism or Mend\n")
                if command == "1": #Execute the priest attack
                    priest_attack(index)
                elif command == "2": #Executes a spell from the priest
                    command = input("\n\033[1;34mWhat spell do you wanna use?"+ 
                                    "\n\033[1;37m1. Exorcism - Damages the enemy - Needs\033[1;34m "+  str(priest_Exorcism_SpellCost) + "\033[1;37m mana points"
                                    "\n\033[1;37m2. Mend - Heals the warrior - Needs\033[1;34m " + str(priest_Mend_SpellCost) + "\033[1;37m mana points"
                                    "\n\033[1;37m-------------- Current mana points: \033[1;34m" + str(priest[1]) +"\033[1;37m --------------\n")
                    if command == "1": #Executes the exorcism spell
                        if priest[1] >= priest_Exorcism_SpellCost: #If the priest got the AP that's needed to do the spell:
                            priest_spell_exorcism(index) #Use the exorcism spell
                        else:
                            print("\n\033[1;31mYou have no more mana points to do this spell!")
                            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
                            priest_turn() #Return to priest turn
                    elif command == "2":
                        if priest[1] >= priest_Mend_SpellCost: #If the priest got the AP that's needed to do the spell:
                            priest_spell_mend() #Use the mend spell
                        else:
                            print("\n\033[1;31mYou have no more mana points to do this spell!")
                            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
                            priest_turn() #Return to priest turn
                    else:
                        print("\033[1;31mChoose a right action!")
                        input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
                        priest_turn() #Return to priest turn
                        
                else: #If player doesn't choose a available option
                    print("\033[1;31mChoose a right action!")
                    input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
                    priest_turn()
        
        def enemy_turn():
                print("\n\033[1;37mThe enemy will play.")
                if vampires[0][0] > 0:
                    time.sleep(1) #Waits a second to do the action
                    print("\n\033[1;31mVampire 1:")
                    enemy_attack() #Enemy attack 1
                if vampires[1][0] > 0:
                    time.sleep(1) #Waits a second to do the action
                    print("\n\033[1;31mVampire 2:")
                    enemy_attack() #Enemy attack 2
                if vampires[2][0] > 0:
                    time.sleep(1) #Waits a second to do the action
                    print("\n\033[1;31mVampire 3:")
                    enemy_attack() #Enemy attack 3
                if vampires[3][0] > 0:
                    time.sleep(1) #Waits a second to do the action
                    print("\n\033[1;31mVampire 4:")
                    enemy_attack() #Enemy attack 4
                input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        
        def first_turn():
                if (PriestTurnOrder >= vampiresTurnOrder) and (PriestTurnOrder >= WarriorTurnOrder): #Priest first
                    priest_turn()
                elif ((WarriorTurnOrder >= vampiresTurnOrder) and (WarriorTurnOrder > PriestTurnOrder)): #Warrior first
                    warrior_turn()
                elif (vampiresTurnOrder > WarriorTurnOrder) and (vampiresTurnOrder > PriestTurnOrder): #Enemy goes first
                    enemy_turn()
                    
        def second_turn():
                if ((PriestTurnOrder >= vampiresTurnOrder) and (PriestTurnOrder < WarriorTurnOrder)) or ((PriestTurnOrder < vampiresTurnOrder) and (PriestTurnOrder >= WarriorTurnOrder)): #Priest second
                    priest_turn()
                elif ((WarriorTurnOrder >= vampiresTurnOrder) and (WarriorTurnOrder >= PriestTurnOrder)) or ((WarriorTurnOrder <= vampiresTurnOrder) and (WarriorTurnOrder >= PriestTurnOrder)) or ((WarriorTurnOrder >= vampiresTurnOrder) and (WarriorTurnOrder <= PriestTurnOrder)): #Warrior second
                    warrior_turn()
                elif ((vampiresTurnOrder >= WarriorTurnOrder) and (vampiresTurnOrder < PriestTurnOrder)) or ((vampiresTurnOrder < WarriorTurnOrder) and (vampiresTurnOrder >= PriestTurnOrder)) or ((vampiresTurnOrder >= PriestTurnOrder) and (vampiresTurnOrder > WarriorTurnOrder)) or ((vampiresTurnOrder >= WarriorTurnOrder) and (vampiresTurnOrder > PriestTurnOrder)): #Enemy second
                    enemy_turn()
            
        def third_turn():
                if (PriestTurnOrder < vampiresTurnOrder) and (PriestTurnOrder < WarriorTurnOrder): #Priest third
                    priest_turn()
                elif (WarriorTurnOrder < vampiresTurnOrder) and (WarriorTurnOrder <= PriestTurnOrder): #Warrior third
                    warrior_turn()
                else: #Enemy third
                    enemy_turn()
                
        while (warrior[0] > 0 or priest[0] > 0) and (vampires[0][0] > 0 or vampires[1][0] > 0 or vampires[2][0] > 0 or vampires[3][0] > 0): #Loop until all of the group die or the enemy dies
            first_turn() #Execute the first turn
            if (warrior[0] > 0 or priest[0] > 0) and (vampires[0][0] > 0 or vampires[1][0] > 0 or vampires[2][0] > 0 or vampires[3][0] > 0):
                second_turn() #Execute the second turn
            if (warrior[0] > 0 or priest[0] > 0) and (vampires[0][0] > 0 or vampires[1][0] > 0 or vampires[2][0] > 0 or vampires[3][0] > 0):
                third_turn() #Execute the third turn
            if (warrior[0] > 0 or priest[0] > 0) and (vampires[0][0] > 0 or vampires[1][0] > 0 or vampires[2][0] > 0 or vampires[3][0] > 0):
                initiative_phase()
            else:
                break

    ####################
    # COMBAT MAIN LOOP #
    ####################
    while (warrior[0] > 0 or priest[0] > 0) and (vampires[0][0] > 0 or vampires[1][0] > 0 or vampires[2][0] > 0 or vampires[3][0] > 0): #Check if all are alive to start the battle
        initiative_phase()
        if (warrior[0] <= 0 and priest[0] <= 0): #All of the player's characters die
            print("\n\033[1;31mYou have died! Better luck next time.")
            break
        if (vampires[0][0] <= 0 and vampires[1][0] <= 0 and  vampires[2][0] <= 0 and vampires[3][0] <= 0): #If all of the enemies die
            print("\n\033[1;96mYou killed all the vampires and ended the castle's curse! Good job!")
            break

#############
# GAME PATH #
#############
print(" \033[1;34m___ ___ ___\n|_A_|_B_|_C_|\n|_D_|_E_|_F_|\n|_G_|_H_|_I_|")
print("\n\033[1;37mYour team is inside the abandoned castle! Find a way out and defeat the castle's curse! (Hint: You have to defeat the enemies that are hiding in one of the rooms!) " +
     "\n\nYou are currently in room: \033[1;34m" + map[y][x])

input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game

while command != "exit": #If the input is different than "exit"
    if map[y][x] == map[0][2]: #If the player go to this room
        print("\n\033[1;37mYOU ENTERED THE CURSED ROOM AND 4 VAMPIRES JUMPED ON YOU, BEAT THEM AND BREAK THE CURSE!")
        input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        combat() #Star combat
        break #Ends the game
    
    command = input("\n\033[1;34mWhere do you want to go?\033[1;37m" + 
                    "\n\033[1;37mnorth"
                    "\n\033[1;37msouth"
                    "\n\033[1;37meast"
                    "\n\033[1;37mwest\n\n")

    if command == "north": #North movement
        if y - 1 >= 0:
            y = y - 1
            print("\n\033[1;37mYou are now in room \033[1;34m" + map[y][x])
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        else:
            print ("\n\033[1;31mYou can't go further than that!")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game

    elif command == "south": #South movement
        if y + 1 <= 2:
            y = y + 1    
            print("\n\033[1;37mYou are now in room \033[1;34m" + map[y][x])
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        else:
            print ("\n\033[1;31mYou can't go further than that!")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game

    elif command == "east": #East movement
        if x + 1 <= 2:
            x = x + 1
            print("\n\033[1;37mYou are now in room \033[1;34m" + map[y][x])
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        else:
            print ("\n\033[1;31mYou can't go further than that!")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game

    elif command == "west": #West movement
        if x - 1 >= 0:
            x = x - 1
            print("\n\033[1;37mYou are now in room \033[1;34m" + map[y][x])
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
        else:
            print ("\n\033[1;31mYou can't go further than that!")
            input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game
    elif command == "exit":
        print("")
    else: #If the player puts the wrong Input
        print("\n\033[1;31mMovement not available")
        input("\n\033[1;33mPress 'ENTER' to continue...") #The player needs to press enter to continue the game