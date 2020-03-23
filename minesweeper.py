from tkinter import *
from tkinter import messagebox
from random import randint

def bpress(i,j):
    global mines
    if mines[i][j] == 'M':        
        blist[i][j].destroy()
        blist[i][j] = Label(frame, text = "M")
        blist[i][j].grid(row = i, column = j)
        messagebox.showinfo("Game Over", "You stepped on a mine and lost!!")

    elif mines[i][j] == 0:
        blist[i][j].destroy()
        blist[i][j] = Label(frame, text = "")
        blist[i][j].grid(row = i, column = j)

    else:
        blist[i][j].destroy()
        blist[i][j] = Label(frame, text = mines[i][j])
        blist[i][j].grid(row = i, column = j)
    

def checkad(x,y):
    if mines[x][y] == 'M':
        return 'M'
    else:
        n = 0
        for ii in range(x-1,x+2):
            for jj in range(y-1, y+2):
                if ii in range(r) and jj in range(c):
                    if mines[ii][jj] == 'M':
                        n += 1
        return n

r = 10
c = 10

mines = []
for i in range(r):
    mines.append([0]*c)

cc = 0
while cc<20:
    a = randint(0,r-1)
    b = randint(0,c-1)
    if mines[a][b] == 'M':
        pass
    else:
        mines[a][b] = 'M'
        cc +=1

for xx in range(r):
    for yy in range(c):
        mines[xx][yy] = checkad(xx, yy)

print(mines)#test

root = Tk()
frame = Frame(root, height = 400, width = 400)

blist = []
#initializing buttons in nested list
for row in range(r):
    blist.append([0]*c)
    for column in range(c):
        blist[row][column] = Button(frame,text = ' ', height = 1, width = 2, command = lambda row = row, column = column: bpress(row, column))
        blist[row][column].grid(row = row, column = column)

frame.pack()

root.mainloop()