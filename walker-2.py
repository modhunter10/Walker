import random
import os

cmd = 'mode 75,36'
os.system(cmd)
win = '''
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║██║██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║╚═╝╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝'''
lose = '''
██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝'''
n = 0
while True:
    try:
        n = int(input("введите размер поля:"))
        break
    except:
        print("только цифры")
m = [[0 for i in range(n)] for i in range(n)]
aicord = [random.randint(0, n-1), random.randint(0, n-1)]
trapcords1 = [random.randint(0, n-1) for i in range(n*n//5)]
trapcords2 = [random.randint(0, n-1) for i in range(n*n//5)]
targetcord = [random.randint(0, n-1), random.randint(0, n-1)]
playercord = [random.randint(0, n-1), random.randint(0, n-1)]
for i in range(len(trapcords1)):
    m[trapcords1[0+i]][trapcords2[0+i]] = 1
if trapcords1 or trapcords2 == targetcord[0] or targetcord[1]:
    while targetcord[0] == targetcord[1]:
        targetcord = [random.randint(0, n-1), random.randint(0, n-1)]
if playercord[0] == playercord[1]:
    while playercord[0] == playercord[1]:
        playercord = [random.randint(0, n-1), random.randint(0, n-1)]
if playercord[0] or playercord[1] in trapcords1 or trapcords2:
    while playercord[0] == playercord[1]:
        playercord = [random.randint(0, n-1), random.randint(0, n-1)]
if aicord[0] == aicord[1]:
    while aicord[0] == aicord[1]:
        aicord = [random.randint(0, n-1), random.randint(0, n-1)]
if aicord[0] or aicord[1] in trapcords1 or trapcords2:
    while aicord[0] == aicord[1]:
        aicord = [random.randint(0, n-1), random.randint(0, n-1)]

m[targetcord[0]][targetcord[1]] = 2
m[playercord[0]][playercord[1]] = 3
m[aicord[0]][aicord[1]] = 4
def Checker(fc):
    if fc == 0:
        return "░"
    if fc == 1:
        return '▒'
    if fc == 2:
        return '▓'
    if fc == 3:
        return '█'
    if fc == 4:
        return '@'
def matrix():
    global m
    for i in range(n):
        for j in range(n):
            print(Checker(m[i][j]), end = " ")
        print()
print("цель - ▓, ты - █ а мины - ▒\n")
matrix()
game = True
print('перемещение на wasd(после каждого ввода нужно нажимать enter)')
def AI():
    global n, playercord, trapcord
    #если по горизонтали корды одинаковы
    if aicord[1] == playercord[1]:
        print(1)
        if playercord[0] > aicord[0]:
            if m[aicord[0]+1][aicord[1]] == 0 or m[aicord[0]+1][aicord[1]] == 3:
                m[aicord[0]][aicord[1]] = 0
                aicord[0] = aicord[0] + 1
                m[aicord[0]][aicord[1]] = 4
        elif playercord[0] < aicord[0]:
            if m[aicord[0]-1][aicord[1]] == 0 or m[aicord[0]-1][aicord[1]] == 3:
                m[aicord[0]][aicord[1]] = 0
                aicord[0] = aicord[0] - 1
                m[aicord[0]][aicord[1]] = 4
                
    elif aicord[0] == playercord[0]:
        print(2)
        if playercord[0] > aicord[0]:
            if m[aicord[0]][aicord[1]+1] == 0 or m[aicord[0]][aicord[1]+1] == 3:
            m[aicord[0]][aicord[1]] = 0
            aicord[1] = aicord[1] + 1
            m[aicord[0]][aicord[1]] = 4
        elif playercord[0] < aicord[0]:
            if m[aicord[0]][aicord[1]-1] == 0 or m[aicord[0]][aicord[1]-1] == 3:
            m[aicord[0]][aicord[1]] = 0
            aicord[1] = aicord[1] - 1
            m[aicord[0]][aicord[1]] = 4
    
    elif playercord[1] > aicord[1]:
        print(3)
        if aicord[1] == n-1:
            m[aicord[0]][aicord[1]] = 0
            aicord[1] = 0
            m[aicord[0]][aicord[1]] = 4
        else:
            m[aicord[0]][aicord[1]] = 0
            aicord[1] = aicord[1] + 1
            m[aicord[0]][aicord[1]] = 4
    elif playercord[1] < aicord[1]:
        print(4)
        if aicord[1] == 0:
            m[aicord[0]][aicord[1]] = 0
            aicord[1] = n-1
            m[aicord[0]][aicord[1]] = 4
        else:
            m[aicord[0]][aicord[1]] = 0
            aicord[1] = aicord[1] - 1
            m[aicord[0]][aicord[1]] = 4
    elif playercord[0] < aicord[0]:
        print(5)
        if aicord[0] == n-1:
            m[aicord[0]][aicord[1]] = 0
            aicord[0] = 0
            m[aicord[0]][aicord[1]] = 4
        else:
            m[aicord[0]][aicord[1]] = 0
            aicord[0] = aicord[0] + 1
            m[aicord[0]][aicord[1]] = 4
    elif playercord[0] > aicord[0]:
        print(6)
        if aicord[0] == n-1:
            m[aicord[0]][aicord[1]] = 0
            aicord[0] = 0
            m[aicord[0]][aicord[1]] = 4
        else:
            m[aicord[0]][aicord[1]] = 0
            aicord[0] = aicord[0] + 1
            m[aicord[0]][aicord[1]] = 4
    
    
    
            
        
        
        
while game:
    # playercord[0] playercord[1]
    pm = input()
    if pm == 'w':
        
        if playercord[0] == 0:
            m[playercord[0]][playercord[1]] = 0
            playercord[0] = n-1
            m[playercord[0]][playercord[1]] = 3
        else:
            m[playercord[0]][playercord[1]] = 0
            playercord[0] = playercord[0] - 1
            m[playercord[0]][playercord[1]] = 3
        AI()
        matrix()
    elif pm == 'a':
        
        if playercord[1] == 0:
            m[playercord[0]][playercord[1]] = 0
            playercord[1] = n-1
            m[playercord[0]][playercord[1]] = 3
        else:
            m[playercord[0]][playercord[1]] = 0
            playercord[1] = playercord[1] - 1
            m[playercord[0]][playercord[1]] = 3
        AI()
        matrix()
    elif pm == 's':
        
        if playercord[0] == n-1:
            m[playercord[0]][playercord[1]] = 0
            playercord[0] = 0
            m[playercord[0]][playercord[1]] = 3
        else:
            m[playercord[0]][playercord[1]] = 0
            playercord[0] = playercord[0] + 1
            m[playercord[0]][playercord[1]] = 3
        AI()
        matrix()
    elif pm == 'd':
        
        if playercord[1] == n-1:
            m[playercord[0]][playercord[1]] = 0
            playercord[1] = 0
            m[playercord[0]][playercord[1]] = 3
        else:
            m[playercord[0]][playercord[1]] = 0
            playercord[1] = playercord[1] + 1
            m[playercord[0]][playercord[1]] = 3
        AI()
        matrix()
    else:
        matrix()
        print('для передвижения используй wasd(после каждого ввода нужно нажимать enter)')
    if m[playercord[0]][playercord[1]] == m[targetcord[0]][targetcord[1]]:
        print(win)
        break
        input()
    for i in range(len(trapcords1)):
        if m[playercord[0]][playercord[1]] == m[trapcords1[0+i]][trapcords2[0+i]] or m[playercord[0]][playercord[1]] == m[aicord[0]][aicord[1]]:
            print(lose)
            input()
            game = False
            break
            input()

