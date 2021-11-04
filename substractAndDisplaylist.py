import time

def addAndDisplayList():
    listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listTwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    for x in range(0, 11):
        x -= 1
        print(str(listOne[x]) + ' - ' +  (str(listTwo[0 + x])) + (' = ') +  str(listOne[0 + x] - listTwo[0 + x]))
        
addAndDisplayList()