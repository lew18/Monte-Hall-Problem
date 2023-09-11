#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:06:41 2023
Updates through Sep 06 2023

@author: lew kurtz

"""

import random
from functools import reduce
import numpy as np

def announcer(verbose, announcement):
    if verbose:
        print(announcement)

def assignDoors():
    winningDoor = random.randint(1, 3)      # This is Monte secretly picking the winning door
    iguanaDoor = (winningDoor % 3) + 1
    ostrichDoor = (iguanaDoor % 3) + 1 
    
    return winningDoor, iguanaDoor, ostrichDoor

# if the Contestant has chosen the door with the Convertible,
# then Monte randomly decides which door to reveal
# else Monte reveals the door that does not have the Convertible
def revealALosingDoor(verbose, dS, wD, iD, oD):
    if dS == 1:
        if wD == 1:
            revealedLoser = random.randint(2, 3)
        elif wD == 2:
            revealedLoser = 3
        else:
            revealedLoser = 2
    elif dS == 2:
        if wD == 2:
            revealedLoser = random.randint(2, 3)
            if revealedLoser == 2:
                revealedLoser = 1
        elif wD == 1:
            revealedLoser = 3
        else:
            revealedLoser = 1
    else:
        if wD == 3:
            revealedLoser = random.randint(1, 2)
        elif wD == 2:
            revealedLoser = 1
        else:
            revealedLoser = 2
        
    if revealedLoser == iD:
        announcer(verbose, "What's that behind door #{}? It's an iguana!".format(iD))
    else:
        announcer(verbose, "What's that behind door #{}? It's an osterich!".format(oD))
    
    return revealedLoser

def swapSelection(swap, dS, wD, iD, oD, rLD):
    selection = dS
    if swap:
        if selection == 1:
            if rLD == 2:
                selection = 3
            else:
                selection = 2
        elif selection == 2:
            if rLD == 1:
                selection = 3
            else:
                selection = 1
        else:
            if rLD == 1:
                selection = 2
            else:
                selection = 1
    
    return selection
        
# game play:
# doors #1, #2, #3
# Monty puts convertible behind one door, animals behind other two doors.
# Contestant picks a door, hoping it holds the convertible.
# Monty reveals one of the animals.
# if Contestant stays with original door and it has the convertible, yay!
# if Contestant stays with original door and it has not the convertible, sad.
# If Contestant switches to un-picked un-revealed door and it has the convertible, yay!
# If Contestant switches to un-picked un-revelaed door and it has not the convertible, sad.

def lmad(verbose, NOP, switch):
    NUMBER_OF_PLAYS=NOP
    
    print("\n\nLet's Make A Deal.")
    print("Contestant picks a door, Monty reveals a losing door, Contestant chooses to:   {}".format(switch))
    playCount = 0
    doorWinningCount = [0, 0, 0]

    winCount=0
    while playCount < NUMBER_OF_PLAYS:
        playCount += 1
        winningDoor, iguanaDoor, ostrichDoor = assignDoors() 

        # Contestant picks a door
        doorSelection = random.randint(1, 3)

        # Monty reveals one of the animals
        revealedLosingDoor = revealALosingDoor(verbose, doorSelection, winningDoor, iguanaDoor, ostrichDoor)

        # Contestant makes decision to hold or switch
        doorSelection = swapSelection(switch=="switch", doorSelection, winningDoor, iguanaDoor, ostrichDoor, revealedLosingDoor)

        # Monte reveals the winning door
        doorWinningCount[winningDoor - 1] += 1
        
        # The Announcer tells teh Contestant if they won the convertible or not.
        if doorSelection == winningDoor:
            announcer(verbose, "Round {}, You won the new convertible!".format(playCount))
            winCount +=1
        else:
            announcer(verbose, "Round {}, Door #{} has the new convertible.".format(playCount, winningDoor))
    
    print("\nNumber of times door 1, 2, 3 had the convertible: {}.".format(doorWinningCount))
    print("Contestant won {} times out of {} games.\n".format(winCount, NUMBER_OF_PLAYS))
    if switch == "switch":
        print("If switching gives 1 in 2 odds, would expect to win about {} out of {} times."
              .format(int(NUMBER_OF_PLAYS/2), NUMBER_OF_PLAYS))
        print("If switching gives 2 in 3 odds, would expect to win about {} out of {} times."
              .format(int(2*NUMBER_OF_PLAYS/3), NUMBER_OF_PLAYS))
    else:
        print("If holding gives 1 in 2 odds, would expect to win about {} out of {} times."
              .format(int(NUMBER_OF_PLAYS/2), NUMBER_OF_PLAYS))
        print("If holding gives 1 in 3 odds, would expect to win about {} out of {} times."
              .format(int(NUMBER_OF_PLAYS/3), NUMBER_OF_PLAYS))


# Not-Monty randomly reveals an unpicked door
def revealADoor(verbose, dS, wD, iD, oD):
    if dS == 1:
        revealedDoor = random.randint(2, 3)
    elif dS == 2:
        revealedDoor = random.randint(2, 3)
        if revealedDoor == 2:
            revealedDoor = 1
    else:
        revealedDoor = random.randint(1, 2)
        
    if revealedDoor == iD:
        announcer(verbose, "What's that behind door #{}? It's an iguana!".format(iD))
    elif revealedDoor == oD:
        announcer(verbose, "What's that behind door #{}? It's an osterich!".format(oD))
    else:
        announcer(verbose, "That's awkward, we just revealed the convertible behind door #{}!".format(wD))
    
    return revealedDoor

# game play:
# doors #1, #2, #3
# Not-Monty puts convertible behind one door, animals behind other two doors.
# Contestant picks a door, hoping it holds the convertible.
# Not-Monty reveals one of the two other doors.
# If Not-Monty reveals the convertible, Contestant loses.
# if Contestant stays with original door and it has the convertible, yay!
# if Contestant stays with original door and it has not the convertible, sad.
# If Contestant switches to un-picked un-revealed door and it has the convertible, yay!
# If Contestant switches to un-picked un-revelaed door and it has not the convertible, sad.

def not_lmad(verbose, NOP, switch):
    NUMBER_OF_PLAYS=NOP
    
    print("\n\nNot Let's Make A Deal.")
    print("Contestant picks a door, Not-Monty reveals a door (could be the winner), Contestant chooses to:   {}".format(switch))
    playCount = 0
    doorWinningCount = [0, 0, 0]
    revealedDoorIsWinnerCount = 0

    winCount=0
    while playCount < NUMBER_OF_PLAYS:
        playCount += 1
        winningDoor, iguanaDoor, ostrichDoor = assignDoors() 

        # Contestant picks a door
        doorSelection = random.randint(1, 3)

        # Monty reveals one of the animals
        revealedDoor = revealADoor(verbose, doorSelection, winningDoor, iguanaDoor, ostrichDoor)
        
        # Monte reveals the winning door (even though maybe already revealed)
        doorWinningCount[winningDoor - 1] += 1

        if revealedDoor == winningDoor:
            revealedDoorIsWinnerCount += 1
            announcer(verbose, "Round {}, there's the convertible behind door #{}".format(playCount, winningDoor))
        else:
            # Contestant makes decision to hold or switch
            doorSelection = swapSelection(switch=="switch", doorSelection, winningDoor, iguanaDoor, ostrichDoor, revealedDoor)
                        
            # The Announcer tells teh Contestant if they won the convertible or not.
            if doorSelection == winningDoor:
                announcer(verbose, "Round {}, You won the new convertible!".format(playCount))
                winCount +=1
            else:
                announcer(verbose, "Round {}, Door #{} has the new convertible.".format(playCount, winningDoor))

    gamesPlayed = NUMBER_OF_PLAYS - revealedDoorIsWinnerCount
    print("\nNumber of times door 1, 2, 3 had the convertible: {}.".format(doorWinningCount))
    print("Number of times the winning door was revealed: {}".format(revealedDoorIsWinnerCount))
    print("Contestant won {} times out of {} games.\n".format(winCount, gamesPlayed))
    if switch == "switch":
        print("If switching gives 1 in 2 odds, would expect to win about {} out of {} times."
              .format(int(gamesPlayed/2), gamesPlayed))
        print("If switching gives 2 in 3 odds, would expect to win about {} out of {} times."
              .format(int(2*gamesPlayed/3), gamesPlayed))
    else:
        print("If holding gives 1 in 2 odds, would expect to win about {} out of {} times."
              .format(int(gamesPlayed/2), gamesPlayed))
        print("If holding gives 1 in 3 odds, would expect to win about {} out of {} times."
              .format(int(gamesPlayed/3), gamesPlayed))


if __name__ == '__main__':
    NUMBER_OF_PLAYS=63000
    verbose=False
    lmad(verbose, NUMBER_OF_PLAYS, "hold")
    lmad(verbose, NUMBER_OF_PLAYS,"switch")
    print("\n")
    not_lmad(verbose, NUMBER_OF_PLAYS, "hold")
    not_lmad(verbose, NUMBER_OF_PLAYS,"switch")
