# Pygame-simple
======= PROCESS LOG =======

Name:Mohammad Fahim Uddin Alvi

UtorID:alvimoh3

Student Number:1005506668

This file is where you will tell us details about the process you went through in creating your project. This is where we want a record of your thoughts, rough notes, failed attempts, things that you tried to get to work that didn't work, etc. e.g. "My first step was to figure out what my main classes will be. I figured out they were ... And then I tried to write code for ... This code didn't work because ..."

You have two options for the format (you can also mix and match the two) -

(1)
A day-to-day journal format.

e.g.
On Friday, I tried to add [this feature].
I looked at [this website], which was helpful.
I managed to almost finish adding it, but [this went wrong].
I wanted to add it because [...], but decided not to in the end, because [...].
If I had more time, I would [...]

OR

(2)
Instead of dividing it up by days, you can divide it up
by task/feature. 

e.g.
Task 1: Added New Monster
I tried to add this by [...]. What worked well was [...]
What didn't work the way I wanted it to was [...]

Task 2: Adding Invisible Treasure
I tried to add this by [...]. What worked well was [...]
What didn't work the way I wanted it to was [...]

===========================

YOUR LOG STARTS HERE


Progress Report on Assignment 1

dragon icon credit : <div>Icons made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
dragon icon(website): https://www.flaticon.com/free-icon/dragon_1016749
other icons used from: https://www.deviantart.com/7soul1/art/420-Pixel-Art-Icons-for-RPG-129892453 

This stage of the game is same as ghost level but with a different goal.Instead of just collecting stars we have to collect orbs of power to kill the
mighty dragon.Then using the key ,found in the crypts, end the stage.Long story short, ghost is essentially the dragon and the stars replaced with orbs.
If five orbs are collected then the dragon disappears(means killed/slayed xD).  

Task1: Loading new map which was easy to do from instructions.Then setup_current_level.I named my level 2 setup method as custom_game which is same as
       setup_ghost_game but new objects added accordingly.Instead or stars now orbs take their place.

Task2: For task1 to work, I had to make new actors - key ,orb and DragonMonster(unecessary cuz same as ghost but meh).Running the game worked but my console
       gave a wierd error (srgb something) I figured it was because my new icons weren't 24x24 so I used this website (https://www.iloveimg.com/resize-image)
       to turn those into 24x24.Lo and behold the error disappeared.Orb was same as star class and DragonMonster was same as ghost but with a method that causes
       it to die.To collect the orbs I had to make another counter (_orbs_collected)which increased as my character collected them.Another counter for key(key_collected)
       to know if key is obtained.So I had to change move method of player accordingly.

Task3: Find if we won the stage.So if the conditions were not met I printed a line to let the player know on the move method player class.Same Conditions applied
       on game_won.But there was a problem, sometimes collecting orbs and taking the key ended game.This was because I used an attribute called door_touched to know if 
       the door was attempted to open but after level 1 I forgot to make that attribute "False" which led to that problem.My move method also had some problem which
       weren't game breaking errors but wierd enough to notice.I looked into my previous work and fixed the problem.

Task4: Killing the damn monster.The game worked perfectly but the dragon did not disappear after I took 5 orbs.So my final task was to make the monster killable.To do this I created a new method under
       Player class, called orb_power which looped through game._actors to find the monster object and then remove it if conditions applied.I ran the code but It was not working
       except for the monster some other objects were removed at a constant pattern.So for that loop ,which was triggered only by left movement for now,I printed out every object it 
       removed to know the pattern and fix it.Turns out I wrote:

               
                if self._orbs_collected >=5:
                   for actor in game._actors:
                       if actor.actor_type()== 2:
                           game.remove_actor(actor)  
        
        instead of:

                for actor in game._actors:
                    if self._orbs_collected >=5 and actor.actor_type()== 2:
                       game.remove_actor(actor)
        
        In my head it seemed right but really it wasn't.Now that it is fixed.After collecting 5 orbs the dragon disappears and we can easily get the key and run for the door.I commented out check_player_death
        to make my character mortal again and tested the game.
       
                  
 

