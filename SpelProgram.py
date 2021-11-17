from math import gamma
import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

Game = random.randint(0, 6)
Game += 1

def spelProgramma(spelList):
    print(spelList[Game])
spelProgramma(spelList)