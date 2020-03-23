from tkinter import *
from tkinter import messagebox
from random import randint

r = 10
c = 10

def clear(iterator,jiterator):
    global mines
    if mines[iterator][jiterator] == 'M':        
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2, text = "M")
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)
        messagebox.showinfo("Game Over", "You stepped on a mine and lost!!")

    elif mines[iterator][jiterator] == 0:
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2, text = "")
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)
        checko(iterator, jiterator)

    else:
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2, text = mines[iterator][jiterator])
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)


def checko(i,j):
    global mines
    for iii in range(i-1,i+2):
        for jjj in range(j-1, j+2):
            if iii in range(r) and jjj in range(c):
                if type(blist[iii][jjj]) is Button:
                    clear(iii, jjj)


def checkad(x,y):
    global mines
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


root = Tk()
frame = Frame(root, height = 400, width = 400)

blist = []
#initializing buttons in nested list
for row in range(r):
    blist.append([0]*c)
    for column in range(c):
        blist[row][column] = Button(frame,text = ' ', height=1, width=2, command=lambda row=row, column=column: clear(row, column))
        blist[row][column].grid(row = row, column = column)

frame.pack()

root.mainloop()