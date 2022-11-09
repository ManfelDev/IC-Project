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
warrior_SpellCost = 5 #Warrior cost to do the spell

#Priest
priest = [20,25,0,2,6] #HP, MP , AP, WP, Init 
PriestTurnOrder = 0 #Setting floor for the priest turn order
priest_dmg = 0 #Setting floor for the priest dmg
priest_Exorcism_SpellCost = 5 #Exorcism spell cost
priest_Mend_SpellCost = 3 #Mend spell cost

###########
# ENEMIES #
###########
#Vampire
vampire = [15,0,2,2,2] #HP, MP, AP, WP, Init
vampire_dmg = 0 #Setting floor for the vampire dmg
VampireTurnOrder = 0 #Initial enemy turn order number


###########################
# COMBAT INITIATIVE PHASE #
###########################
def initiative_phase(): #Function for setting the turn order
    #Variables for get in action phase
    global WarriorTurnOrder
    global PriestTurnOrder
    global VampireTurnOrder

    #Variables to reset the score
    WarriorTurnOrder = 0
    PriestTurnOrder = 0
    VampireTurnOrder = 0
    
    #Cal the results to who goes first
    WarriorTurnOrder = WarriorTurnOrder + random.randint(0,20) + warrior[4] #Random Value for the Warrior's turn number
    PriestTurnOrder = PriestTurnOrder + random.randint(0,20) + priest[4] #Random Value for the Priest's turn number
    VampireTurnOrder = VampireTurnOrder + random.randint(0,20) + vampire[4] #Random Value for the Vampire's turn number
    
    #Print the results
    print("\nThe warrior got " + str(WarriorTurnOrder)) 
    print("The vampire got " + str(VampireTurnOrder))
    print("The priest got " + str(PriestTurnOrder))

    #Start Action phase with the numbers cal    
    action_phase()
    
##########################
# WARRIOR COMBAT ACTIONS #
##########################    
#Attack from the warrior
def warrior_attack(): #If the vampire got the armor up
    if vampire[2] > 0: #If the vampire got the armor up, then attack the armor
        vampire[2] = vampire[2] - random.randrange(warrior[3]) #Enemy's AP less the random number inside WP from the warrior
        if vampire[2] > 0: 
            print("You damaged the enemy armor! Enemy's current armor :" + str(vampire[2]))
        elif vampire[2] <= 0:
            print("You have destroyed the enemy armor!")
    elif vampire[2] <= 0: #If the vampire got no armor, then attack life
        vampire[0] = vampire[0] - random.randrange(warrior[3]) #Enemy's HP less the random number inside WP from the warrior
        if vampire[0] > 0:
            print("You hit the enemy, enemy current life: " + str(vampire[0]))

#RushDown spell from the warrior  
def warrior_spell(): #Function for the Warrior Spell
    d4 = random.randint(1,4) #Four-sided dice
    SpellEffectValue = -1 * (warrior[3] + d4) #Spell effect and the respective damage
    vampire[0] = vampire[0] + SpellEffectValue #Damage gave to the enemy
    warrior[1] = warrior[1] - warrior_SpellCost #Take of MP points after the spell

#########################
# PRIEST COMBAT ACTIONS #
#########################
#Attack from the priest
def priest_attack():
    if vampire[2] > 0: #If the vampire got the armor up
        vampire[2] = vampire[2] - random.randrange(priest[3]) #Enemy's AP less the random number inside WP from the priest
        if vampire[2] > 0: 
            print("You damaged the enemy armor! Enemy's current armor :" + str(vampire[2]))
        elif vampire[2] <= 0:
            print("You have destroyed the enemy armor!")
    elif vampire[2] <= 0: #If the vampire got no armor, attack life
        vampire[0] = vampire[0] - random.randrange(priest[3]) #Enemy's HP less the random number inside WP from the priest
        print("You hit the enemy, enemy current life: " + str(vampire[0]))

#Exorcism spell from the priest
def priest_spell_exorcism():
    d4 = random.randint(1,4) #Four-sided dice
    SpellEffectValue = -1 * (d4 * 2) #Spell effect and the respective damage
    vampire[0] = vampire[0] + SpellEffectValue #Damage gave to the enemy
    priest[1] = priest[1] - priest_Exorcism_SpellCost #Take of MP points after the spell

#Mend spell from the priest
def priest_spell_mend():
    d6 = random.randint(1,6) #Four-sided dice
    SpellEffectValue = d6 + priest[3] #Spell effect and the respective damage
    warrior[0] = warrior[0] + SpellEffectValue #Damage gave to the enemy
    priest[1] = priest[1] - priest_Mend_SpellCost #Take of MP points after the spell


########################
# ENEMY COMBAT ACTIONS #
########################
#Attack from the enemy
def enemy_attack():
    if warrior[2] > 0: #If the warrior got the armor up
        warrior[2] = warrior[2] - random.randrange(vampire[3])
        if warrior[2] > 0:
            print("Your warrior got the armor damaged! Warrior's current armor: " + str(warrior[2]))
        elif warrior[2] <= 0:
            print("Your warrior's armor is destroyed!")
    elif warrior[2] <= 0:
        warrior[0] = warrior[0] - random.randrange(vampire[3])
        print("Your warrior got attacked, his current life is: " + str(warrior[0]))
    elif warrior[0] <= 0: #If the warrior got killed
        print("Your warrior got killed!") 
    elif priest[2] > 0: 
        priest[2] = priest[2] - random.randrange(vampire[3])
        if priest[2] > 0:
            print("Your priest got the armor damaged! Priest's current armor: " + str(priest[2]))
        elif priest[2] <= 0:
            print("Your warrior's armor is destroyed!")
    
#######################
# COMBAT ACTION PHASE #
#######################
def action_phase():
    def warrior_turn():
            command = input("\nWarrior is playing: " +
                            "\nChoose your action" + 
                            "\n1. Attack." +
                            "\n2. Magic.\n")
            if command == "1": #Execute the warrior attack
                warrior_attack()
            elif command == "2": #Execute the warrior spell
                if warrior[1] >= warrior_SpellCost: #If the warrior got the MP suf to do the spell
                    warrior_spell()
                    print("You have damage your enemy! Enemy's current life: ", vampire[0])
                else: #If the warrior got no MP suf to do the spell
                    print("You have no more MP!")
                    warrior_turn()
            else: #If the player put's a incorrect input
                print("Enter a correct action!")
                warrior_turn()
    def priest_turn():
            command = input("\nPriest is playing: " +
                            "\nChoose your action" + 
                            "\n1. Attack." +
                            "\n2. Magic.\n")
            if command == "1": #Execute the priest attack
                warrior_attack()
            elif command == "2": #Executes a spell from the priest
                command = input("\nWhat spell do you wanna use?"+ 
                                "\n1. Exorcism - Damage the enemy" +
                                "\n2. Mend - Heal the warrior\n")
                if command == "1": #Executes the exorcism spell
                    if priest[1] >= priest_Exorcism_SpellCost:
                        priest_spell_exorcism()
                        print("You have damage your enemy! Enemy's current life: ", vampire[0])
                    else:
                        print("You have no more MP!")
                        priest_turn()
                elif command == "2":
                    if priest[1] >= priest_Mend_SpellCost:
                        priest_spell_mend()
                        print("You healed the warrior! Warrior's current life: ", warrior[0])
                    else:
                        print("You have no more Mana Points!")
                        priest_turn()
            else:
                print("Enter a correct action!")
                priest_turn()
    
    def enemy_turn():            
            print("\nThe enemy will play.")
            enemy_attack()
    
    def first_turn():
        if (WarriorTurnOrder > VampireTurnOrder) and (WarriorTurnOrder > PriestTurnOrder): #Warrior first
            warrior_turn()
        elif (PriestTurnOrder > VampireTurnOrder) and (PriestTurnOrder > WarriorTurnOrder): #Priest first
            priest_turn()
        elif (VampireTurnOrder > WarriorTurnOrder) and (VampireTurnOrder > PriestTurnOrder): #Enemy goes first
            enemy_turn()
        elif (WarriorTurnOrder == VampireTurnOrder) or (WarriorTurnOrder == PriestTurnOrder): #In case of draw return to turn order
            initiative_phase()
        elif (PriestTurnOrder == VampireTurnOrder) or (PriestTurnOrder == WarriorTurnOrder): #In case of draw return to turn order
            initiative_phase()
        elif (VampireTurnOrder == WarriorTurnOrder) or (VampireTurnOrder == PriestTurnOrder): #In case of draw return to turn
            initiative_phase()
            
    def second_turn():
        if (WarriorTurnOrder > VampireTurnOrder) and (WarriorTurnOrder < PriestTurnOrder): #Warrior second
            warrior_turn()
        elif (PriestTurnOrder > VampireTurnOrder) and (PriestTurnOrder < WarriorTurnOrder): #Priest second
            priest_turn()
        elif (VampireTurnOrder > WarriorTurnOrder) and (VampireTurnOrder < PriestTurnOrder): #Enemy second
            enemy_turn()
    
    def third_turn():
        if (WarriorTurnOrder < VampireTurnOrder) and (WarriorTurnOrder < PriestTurnOrder): #Warrior third
            warrior_turn()
        elif (PriestTurnOrder < VampireTurnOrder) and (PriestTurnOrder < WarriorTurnOrder): #Priest third
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
            print("You have killed the vampire! Good job!.")
            break
        else:
            break

####################
# COMBAT MAIN LOOP #
####################
if (warrior[0] > 0 and priest[0] > 0) and vampire[0] > 0: #Check all are alive to start the battle
    initiative_phase()