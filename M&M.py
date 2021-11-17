import time
import random

Kleuren = ['Oranje', 'Blauw', 'Groen', 'Bruin', 'Geel']

Randomizer = random.randint(0, 4)

def yes():
    print("M&M: Hoeveel kleuren M&Ms wilt u in de zak doen?")
    Keus = int(input())
    if Keus <= 60:
        print('Aan het berekenen..')
        time.sleep(2)
        print('Oke ik heb ' + str(Keus) + 'x ' + Kleuren[Randomizer] + ' In het zakje gedaan.')
    else:
        print('Te veel..')
        return yes()

yes() 