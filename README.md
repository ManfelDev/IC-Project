# Final IC Project

### Objective of the Project:

Implement the described combat system with two playable characters and 4 enemies adding more features to make the game more complete.
## Developers

- [@Rafael-j-03](https://github.com/Rafael-j-03)
- [@rodgoe](https://github.com/rodgoe)
## How our project was organized

- The code production was mostly done by Rafael José, Rodrigo Gomes also contributed to it, helping to solve some problems and some logical systems.
The README.md was mostly done by Rodrigo Gomes, in which Rafael José helped composed the commits information. 
- 1st commit - First beta combat system, which contained the 2 player character's, 1 enemy, a simple initiative phase with the turn order system and simple action_phase. - Rafael José - 22202078

- 2nd commit - We have added a condition to end combat, either when both player characters are dead, or when the enemy dies. - Rafael José - 22202078

- 3rd commit - Update on the attacks from the priest, warrior and the enemy. 
More organization in the code.
Correction of the message when the enemy is killed, now negative life no longer appears.
Changed the variable enemy_turnOrder to VampireTurnOrder. - Rafael José - 22202078

- 4th commit - Update on the TurnOrder d20.
Corrections on some notes.
Correction on the enemy attack.
Correction on the print of the turn orders.
Putting the combat up to 4 enemies.
Variable "damage" update.
Changes in the functions of the attacks and spells.
Order correction on the first turn.
Update on the end-game terms. - Rafael José - 22202078

- 5th - Some bug fixes.
New input “Press “enter”” after every action to give time to the player see the current action or what happen after them.
Setting a timer to show the enemy attack 1 by 1 to give time to the player see the enemy damage.
Clear the text before a new round.
Adding color to the text for a better view of what is happening.
Added more notes.
Fix on the turn order, now all the characters play in the round they must play. - Rafael José - 22202078

- 6st - Implementation of a short map. - Rafael José - 22202078

- 7st - README.md Implementation. - Rodrigo Gomes - 22201252


[Git Repository](https://github.com/Rafael-j-03/IC-Project)
## Development of our work

### How we organized our code

- We first specified our squad with the Warrior and the Priest which are the characters that we used for the combat and that the player is able to control, each character has its own attributes that are divided in: Hit-Points (HP); Mana-Points (MP); Armor Points (AP); Weapon (WP) and Initiative (Init).

- After that we created 4 enemies and called them "vampires" that the characters have to fight as soon as they find the "haunted room" inserted inside the map.

- With both characters and enemies we used a "turn order". We called this the initiative phase to set the numbers so it can tell who goes first, second and so on.

- With the characters and enemies defined, we organize the combat actions starting with the Warrior we put him to attack with his respective damage, which is given by his WP minus the enemy's AP, we also create a spell called RushDown that attacks directly on the enemy's life, the damage is given by the Warrior's WP + a d4. After that we implemented the Priest attack and created 2 spells, the exorcism which deals direct damage to the opponent's life, and its damage consists of a d4 * 2.

- Then we organized the combat mechanics for the vampires, creating a simple attack system, where the enemy's attack consists equally to the priest and warrior systems. They start by attacking the warrior until they kill him, and then move on to the priest.

- Now for the combat action phase, if we are controlling the Priest or the Warrior we must choose if we are going to attack or use the mana points to do a spell, with a reference that the character can only use mana if it has the respective points to do so. In another point the Priest can attack with one spell called "Exorcism" or heal an ally with another spell called "Mend". Again the player must be cautious with the number of points that can be used. If the action that the player is trying to perform can't be used an error message will appear and a new action needs to be set.

- Now to arrange who goes first, we simply set the function for who gets the highest number then that's who it will start, and in case of a draw advance the character with the highest Init. We repeated the same action until everyone got their turn finished.

- We set a loop so that if the characters or if the enemies die we execute the same turns previously described.

- If the characters die or if all the enemies are defeated, a special message will appear and the game ends.

- As a bonus we have implemented a small map where combat will take place as soon as the player discovers the room where the enemies are.

## References

- We import three external libraries, os, time and random.
  
- The "random" like the article about it says "This module implements pseudo-random number generators for various distributions.
For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.". And we used it for get random numbers mostly for the dices system.

- The "os" like the article about it says "This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. For creating temporary files and directories see the tempfile module, and for high-level file and directory handling see the shutil module.". We used it just to clear the console of the player before the start of a new round, to get a better view of the game.

- The "time" like the article about it says "This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.". We used it just for setting a time after every enemy action to the player get a better look of the enemy's attack.
