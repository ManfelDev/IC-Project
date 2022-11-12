import random #Random library

#############
# VARIABLES #
#############
command = "" #Initial command for input
index = 0 #Form zero from the index

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
def initiative_phase(): #Function for setting the turn order
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
    print("\nThe warrior got " + str(WarriorTurnOrder))
    print("The priest got " + str(PriestTurnOrder))
    print("The vampire got " + str(vampiresTurnOrder))

    #Start Action phase with the numbers calculated
    action_phase()
    
##########################
# WARRIOR COMBAT ACTIONS #
##########################    
#Attack from the warrior
def warrior_attack(index): #If the vampires got the armor up
    command = input("\nEach enemy do you want to attack?: " +
                                    "\n1. Vampire 1" + 
                                    "\n2. Vampire 2" +
                                    "\n3. Vampire 3" +
                                    "\n4. Vampire 4\n") 
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
        print("Choose a right target!") 
        warrior_attack(index)
        
    return index

def warrior_do_attack(index):
    warrior_dmg = warrior[3] - vampires[index][2] #Warrior damage: warrior's WP - vampires AP
    if vampires[index][0] > 0: #If vampire is alive
        vampires[index][0] = vampires[index][0] - warrior_dmg #Enemy's HP less the warrior's WP - the vampires AP
        if vampires[index][0] > 0: #If vampire's still alive after the attack:
            print("You have hit the enemy, enemy's current life: " + str(vampires[index][0])) #Print the enemy current life
        else: #If the vampire's dead, after the attack:
            print("You have killed vampire " + str(index + 1) + "!")
    else: #If the vampires selected is dead:
        print("\nThe vampire " + (str(index + 1)) + " is dead, choose another target!")
        warrior_attack(index) #Return to warrior's attack selection
        
    return index

#RushDown spell from the warrior  
def warrior_spell(index): #Function for the Warrior Spell
    command = input("\nEach enemy do you want to do the spell?: " +
                                "\n1. Vampire 1" + 
                                "\n2. Vampire 2" +
                                "\n3. Vampire 3" +
                                "\n4. Vampire 4\n")
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
    
    return index

def warrior_rushDown(index):
    d4 = random.randint(1,4) #Four-sided dice
    SpellEffectValue = -1 * (warrior[3] + d4) #Spell effect and the respective damage
    if vampires[index][0] > 0: #If vampire if alive
        vampires[index][0] = vampires[index][0] + SpellEffectValue #Damage gave to the enemy
        warrior[1] = warrior[1] - warrior_SpellCost #Take of MP points after the spell
        if vampires[index][0] > 0:
            print("You have hit the enemy, enemy's current life: " + str(vampires[index][0]))
        else:
            print("You have killed vampire " + str(index + 1)+ "!")
    else: #If vampire is dead:
        print("\nThe vampire " + (str(index + 1)) + " is dead, choose another target!")
        warrior_spell(index) #Return to warrior's target select
        
    return index

#########################
# PRIEST COMBAT ACTIONS #
#########################
#Attack from the priest
def priest_attack(index): #If the vampires got the armor up
    command = input("\nEach enemy do you want to attack?: " +
                                    "\n1. Vampire 1" + 
                                    "\n2. Vampire 2" +
                                    "\n3. Vampire 3" +
                                    "\n4. Vampire 4\n")
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
        print("Choose a right target!") 
        priest_attack(index)
        
    return index

def priest_do_attack(index):
    priest_dmg = priest[3] - vampires[index][2] #Priest damage: priest WP - enemy AP
    if priest_dmg <= vampires[index][2]: #If priest damage <= enemy's AP
        print("You have attacked the enemy but you are to weak to damage him! Try to use a spell next time.")
    elif priest_dmg > vampires[index][2]: #If priest damage > enemy's AP
        if vampires[index][0] > 0: #If the vampire's still alive
            vampires[index][0] = vampires[index][0] - priest_dmg #Do the damage to the enemy life
            if vampires[index][0] > 0: #If the enemy's still alive after the attack:
                print("You have hit the enemy, enemy's current life: " + str(vampires[index][0])) #Print the enemy current life
            else: #If the enemy's dead after the attack:
                print("You have killed vampire " + str(index + 1)+ "!")
        else: #If the vampires selected is dead
            print("\nThe vampires " + (str(index + 1)) + " is dead, choose another target!")
            priest_attack(index) #Returns to priest attack selection
        
    return index

#Exorcism spell from the priest
def priest_spell_exorcism(index): #Function for the Warrior Spell
    command = input("\nEach enemy do you want to do the spell?: " +
                                "\n1. Vampire 1" + 
                                "\n2. Vampire 2" +
                                "\n3. Vampire 3" +
                                "\n4. Vampire 4\n")
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
    
    return index

def priest_exorcism(index):
    d4 = random.randint(1,4) #Four-sided dice
    SpellEffectValue = -1 * (d4 * 2) #Spell effect and the respective damage
    if vampires[index][0] > 0: #If vampire if alive
        vampires[index][0] = vampires[index][0] + SpellEffectValue #Damage gave to the enemy
        priest[1] = priest[1] - priest_Exorcism_SpellCost #Take of MP points after the spell
        if vampires[index][0] > 0: #If the enemy is still alive after the attack:
            print("You have hit the enemy, enemy's current life: " + str(vampires[index][0]))
        else: #If the enemy is dead after the attack:
            print("You have killed vampire " + str(index + 1)+ "!")
    else: #If vampire is dead:
        print("\nThe vampire " + (str(index + 1)) + " is dead, choose another target!")
        priest_spell_exorcism(index)#Return to warrior's target select
        
    return index

#Mend spell from the priest
def priest_spell_mend():
    d6 = random.randint(1,6) #Four-sided dice
    SpellEffectValue = d6 + priest[3] #Spell effect and the respective damage
    warrior[0] = warrior[0] + SpellEffectValue #Damage gave to the enemy
    priest[1] = priest[1] - priest_Mend_SpellCost #Take of MP points after the spell
    print("You healed the warrior! Warrior's current life: ", warrior[0])


########################
# ENEMY COMBAT ACTIONS #
########################
#Attack from the enemy, warrior is attack first because he is in front
def enemy_attack(): 
    if warrior[0] > 0: #If the warrior is alive:
        vampire_dmg = vampires[0][3] - warrior[2] #Vampire's damage to warrior, vampires WP - warrior AP
        warrior[0] = warrior[0] - vampire_dmg #vampire damage the warrior's HP
        if warrior[0] > 0: #If warrior's still alive:
            print("Your warrior got attacked, his current life is: " + str(warrior[0])+ "\n")
        elif warrior[0] <= 0: #If the warrior got killed:
            print("Your warrior got killed!")
    elif priest[0] > 0: #If the warrior is dead then attack the priest:
        vampire_dmg = vampires[0][3] - priest[2] #Vampire's damage to priest
        priest[0] = priest[0] - vampire_dmg
        if priest[0] > 0: #If priest's still alive:
            print("Your priest got attacked, his current life is: " + str(priest[0]))
        elif priest[0] <= 0: #If the priest got killed:
            print("Your priest got killed!")
    
#######################
# COMBAT ACTION PHASE #
#######################
def action_phase():
    def warrior_turn():
                command = input("\nWarrior is playing: " +
                                "\nChoose your action" + 
                                "\n1. Attack." +
                                "\n2. Spell - RushDown (Damages the enemy).\n")
                if command == "1": #Execute the warrior attack
                        warrior_attack(index)
                elif command == "2": #Execute the warrior spell
                    if warrior[1] >= warrior_SpellCost: #If the warrior got the MP suf to do the spell
                        warrior_spell(index) #Warrior spell, RushDown
                    else: #If the warrior got no MP suf to do the spell
                        print("You have no more mana points!")
                        warrior_turn() #Return to priest turn
            
    def priest_turn():
            command = input("\nPriest is playing: " +
                            "\nChoose your action" + 
                            "\n1. Attack." +
                            "\n2. Spell - Exorcism or Mend.\n")
            if command == "1": #Execute the priest attack
                priest_attack(index)
            elif command == "2": #Executes a spell from the priest
                command = input("\nWhat spell do you wanna use?"+ 
                                "\n1. Exorcism - Damages the enemy" +
                                "\n2. Mend - Heal the warrior\n")
                if command == "1": #Executes the exorcism spell
                    if priest[1] >= priest_Exorcism_SpellCost: #If the priest got the AP that's needed to do the spell:
                        priest_spell_exorcism(index) #Use the exorcism spell
                    else:
                        print("You have no more MP!")
                        priest_turn() #Return to priest turn
                elif command == "2":
                    if priest[1] >= priest_Mend_SpellCost: #If the priest got the AP that's needed to do the spell:
                        priest_spell_mend() #Use the mend spell
                        print("You healed the warrior! Warrior's current life: ", warrior[0])
                    else:
                        print("You have no more mana points!")
                        priest_turn() #Return to priest turn
                else:
                    print("Enter a correct action!")
                    priest_turn() #Return to priest turn
    
    def enemy_turn():
            print("\nThe enemy will play.\n")
            if vampires[0][0] > 0:
                print("Vampire 1:")
                enemy_attack() #Enemy attack 1
            if vampires[1][0] > 0:
                print("Vampire 2:")
                enemy_attack() #Enemy attack 2
            if vampires[2][0] > 0:
                print("Vampire 3:")
                enemy_attack() #Enemy attack 3
            if vampires[3][0] > 0:
                print("Vampire 4:")
                enemy_attack() #Enemy attack 4
    
    def first_turn():
        if (WarriorTurnOrder == vampiresTurnOrder) or (WarriorTurnOrder == PriestTurnOrder): #In case of draw return to choose turn order
            initiative_phase()
        elif (PriestTurnOrder == vampiresTurnOrder) or (PriestTurnOrder == WarriorTurnOrder): #In case of draw return to choose the turn order
            initiative_phase()
        elif (vampiresTurnOrder == WarriorTurnOrder) or (vampiresTurnOrder == PriestTurnOrder): #In case of draw return to choose the turn order
            initiative_phase()
        elif (WarriorTurnOrder > vampiresTurnOrder) and (WarriorTurnOrder > PriestTurnOrder): #Warrior first
            warrior_turn()
        elif (PriestTurnOrder > vampiresTurnOrder) and (PriestTurnOrder > WarriorTurnOrder): #Priest first
            priest_turn()
        elif (vampiresTurnOrder > WarriorTurnOrder) and (vampiresTurnOrder > PriestTurnOrder): #Enemy goes first
            enemy_turn()
            
    def second_turn():
        if (WarriorTurnOrder > vampiresTurnOrder) and (WarriorTurnOrder < PriestTurnOrder): #Warrior second
            warrior_turn()
        elif (PriestTurnOrder > vampiresTurnOrder) and (PriestTurnOrder < WarriorTurnOrder): #Priest second
            priest_turn()
        elif (vampiresTurnOrder > WarriorTurnOrder) and (vampiresTurnOrder < PriestTurnOrder): #Enemy second
            enemy_turn()
    
    def third_turn():
        if (WarriorTurnOrder < vampiresTurnOrder) and (WarriorTurnOrder < PriestTurnOrder): #Warrior third
            warrior_turn()
        elif (PriestTurnOrder < vampiresTurnOrder) and (PriestTurnOrder < WarriorTurnOrder): #Priest third
            priest_turn()
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
    if (warrior[0] <= 0 and priest[0] <= 0): #All the player's characters die
        print("You have died! Better luck next time.")
        break
    if (vampires[0][0] <= 0 and vampires[1][0] <= 0 and  vampires[2][0] <= 0 and vampires[3][0]): #The enemy die
        print("You have killed all the vampires! Good job!")
        break