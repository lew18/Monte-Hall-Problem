# Monte-Hall-Problem
Simple python program to show odds in Monte Hall problem

What is the controversy?
In “Let’s make a Deal” last game has three doors. Contestant chooses a door. A losing door is then revealed. The Contestant is then given the option to swap to the unchosen unrevealed door. Should they?
•	Some say “yes, because the unchosen unrevealed door has 2/3 chance of being a winner”.
•	Others say “does not matter since originally selected door and unchosen unrevealed door have equal chance of being a winner”.


What is happening?
1.	Odds are set at the time the game picks the winning door.
2.	With three doors and one winning door, the odds are 1 in 3 that a given door is the winner and 2 in 3 that the given door is a loser.
3.	Contestant picks a door. At this point, the two unpicked doors have
•	a 2 in 3 chance of having the winner and one loser.
•	a 1 in 3 chance of having two losers.
4.	Game then reveals a known (by the game) losing door, with no further activity. This revelation has just shown a/the losing door, and the other door retains the 2 in 3 chance of being the winner.

The key is the method used to reveal a door.
If randomly chosen, then the odds change.
If controlled, then the odds do not change.


If game is changed to:
Contestant picks a door, game randomly reveals an unpicked door.
If the door revealed is the winner, then odds for the other two doors are now zero.
If the door revealed is not the winner, then odds change to 1 in 2.


Much more thorough and clear explanation here:
https://en.wikipedia.org/wiki/Monty_Hall_problem


The simple python code runs the last game of “Let’s Make a Deal” many times to get good averages, and then shows how it would change if the door revealed was randomly chosen instead of deliberately chosen.
