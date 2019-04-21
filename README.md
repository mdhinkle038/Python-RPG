# Python-RPG
Python RPG was created for my CT-206 Scripting Languages Class
Its currently not finished, but plan on finishing it in the near future.

REQUIREMENTS FOR THE GAME

Part 1:

Write a welcome message for your players telling them the name of your game.
Tell your players their race options and input their response (I went with traditional fantasy options, but you can go with anything, as long as it’s not offensive).

Part 2:

If your players chose a valid option, output a message congratulating them and telling them what race they chose. Decide how you want to deal with players who choose an invalid option. HINT: You could put this in a loop to give them another chance, or choose a race for them and tell them it was chosen for them because their response was invalid.

Part 3:

Tell your players their class options and input their response (again, I went with traditional fantasy options, but you can use whatever you’d like).
Create a similar message to the one you made for race telling players their class. Make sure you deal with invalid selections.

Part 4:

Ask players for the name of their character and input it to a variable.
Output a message telling them their name, race, and class.

Part 5:

Create default stats for your players (we will modify these based on their race and class (I am using hit points, strength, defense, magic, and agility and setting their default values to 10 each).
For each race and class, modify (add to or subtract from) one or more stats.
Print out a message telling your players their stats.

Part 6:

Assign your players a quest or allow them to choose one (keep in mind that with multiple quests at this point you will either need to implement each of them, or make it so that the player is unable to go on (or survive) some of the quests.
Create an exit variable and set it to false near the beginning of your program.
Create a loop (after your exit variable is declared and set) around your game with the condition that the loop will continue as long as the exit variable is false. This will allow players to leave the game if they die or get tired of playing.
Create an alive variable right above the exit variable and set it to True.

Part 7:

Create some monsters. Make each one a dictionary that lists their stats. These will probably be similar to yours and should have stats that are useful for combat.
Create an array and put your monsters in it.

Part 8:

Create a loop that checks whether you are alive and on a quest.
Give your player a list of action options (such as exiting the game, fighting a monster, searching, traveling, etc).
If the player chooses the monster option, randomly choose a monster from monsters list and tell the player what they are fighting. For syntax on generating a random-enough number: https://pythonspot.com/random-numbers/ (Links to an external site.)Links to an external site.

Part 9:

Create a function for a random combat encounter that has the player fight the random monster they found (in Part 8). Call the function.

Part 10:

Break code from your random encounter function into additional functions as needed to improve your code (if needed).

Part 11:

Create a Loot class.
Create loot instances and store them in a list.
Create an inventory list.
When you defeat a monster in combat, choose and random item from your loot list, add it to your inventory, and tell the player what loot they received.

Part 12:

Add attributes to your Loot class that tells whether your loot is equipable and whether it is equipped.
Update your instances to give them values for these attributes.
Add a method to your Loot class that, when called, checks whether the item is equipable and whether it is unequipped, and if so, equips the item. If not, tell the player why the item was not equipped.
After a new piece of loot is added to the inventory, if the item is equipable, give the player the option to equip the item.
