from tkinter import Tk, Frame, Button, Label, PhotoImage, Canvas, Entry
from tkinter import messagebox
from random import randint



def clear(xcord, ycord):

    # clearing stuff when clicked
    if mineslist[xcord][ycord] == 'M':
        blist[xcord][ycord].destroy()
        blist[xcord][ycord] = Label(
            Game, height=24, width=24, bd=1, relief='ridge', image=minep)
        blist[xcord][ycord].grid(row=xcord, column=ycord)
        messagebox.showinfo(
            "Game Over", "You stepped on a mine and lost!!")
        # aftergame()

    elif mineslist[xcord][ycord] == 0:
        blist[xcord][ycord].destroy()
        blist[xcord][ycord] = Label(
            Game, height=1, width=2, bd=1, relief='ridge', text=" ", font='Helvetica 14',)
        blist[xcord][ycord].grid(row=xcord, column=ycord)
        checko(xcord, ycord)

    elif mineslist[xcord][ycord] == 1:
        blist[xcord][ycord].destroy()
        blist[xcord][ycord] = Label(
            Game, height=1, width=2, bd=1, relief='ridge', text=1, font='Helvetica 14', fg='blue')
        blist[xcord][ycord].grid(row=xcord, column=ycord)

    elif mineslist[xcord][ycord] == 2:
        blist[xcord][ycord].destroy()
        blist[xcord][ycord] = Label(
            Game, height=1, width=2, bd=1, relief='ridge', text=2, font='Helvetica 14', fg='green')
        blist[xcord][ycord].grid(row=xcord, column=ycord)

    elif mineslist[xcord][ycord] == 3:
        blist[xcord][ycord].destroy()
        blist[xcord][ycord] = Label(
            Game, height=1, width=2, bd=1, relief='ridge', text=3, font='Helvetica 14', fg='red')
        blist[xcord][ycord].grid(row=xcord, column=ycord)

    elif mineslist[xcord][ycord] == 4:
        blist[xcord][ycord].destroy()
        blist[xcord][ycord] = Label(
            Game, height=1, width=2, bd=1, relief='ridge', text=4, font='Helvetica 14', fg='orange')
        blist[xcord][ycord].grid(row=xcord, column=ycord)

    elif mineslist[xcord][ycord] == 5:
        blist[xcord][ycord].destroy()
        blist[xcord][ycord] = Label(
            Game, height=1, width=2, bd=1, relief='ridge', text=5, font='Helvetica 14', fg='gold')
        blist[xcord][ycord].grid(row=xcord, column=ycord)

    elif mineslist[xcord][ycord] == 6:
        blist[xcord][ycord].destroy()
        blist[xcord][ycord] = Label(
            Game, height=1, width=2, bd=1, relief='ridge', text=6, font='Helvetica 14', fg='yellow')
        blist[xcord][ycord].grid(row=xcord, column=ycord)

def flag(rr, cc, nn):
    # flagging
    if blist[rr][cc]['text'] == "u":
        blist[rr][cc].destroy()
        blist[rr][cc] = Button(
            Game, text='f', image=flagp, height=20, width=20)
        blist[rr][cc].bind(
            '<Button-3>', lambda event, rr=rr, cc=cc: flag(rr, cc, nn))
        blist[rr][cc].grid(row=rr, column=cc)
        # minescoreup()
    # unflagging
    elif blist[rr][cc]['text'] == "f":
        blist[rr][cc].destroy()
        blist[rr][cc] = Button(Game, text='u', image=emptyp, height=20,
                                    width=20, command=lambda row=rr, column=cc: clear(row, column))
        blist[rr][cc].bind(
            '<Button-3>', lambda event, rr=rr, cc=cc: flag(rr, cc, nn))
        blist[rr][cc].grid(row=rr, column=cc)
        # minescoredown()

def checkwin():
    # checking if won
    q = 0
    for k in range(rows):
        for l in range(columns):
            if type(blist[k][l]) == Button and blist[k][l]['text'] == "f":
                if mineslist[k][l] == 'M':
                    q += 1
    if q == nomines:
        messagebox.showinfo("", "YOU WIN !!!")

def checko(i, j):
    # clearing adjacent empty squares automatically
    for iii in range(i-1, i+2):
        for jjj in range(j-1, j+2):
            if iii in range(rows) and jjj in range(columns):
                if type(blist[iii][jjj]) is Button:
                    clear(iii, jjj)

def checkad(x, y, mr, mc):
    if mineslist[x][y] == 'M':
        return 'M'
    else:
        s = 0
        for ii in range(x-1, x+2):
            for jj in range(y-1, y+2):
                if ii in range(mr) and jj in range(mc):
                    if mineslist[ii][jj] == 'M':
                        s += 1
        return s


Game = Tk()

frame = Frame(Game)

mr,rows = 8,8
mc,columns = 8,8
mn,nomines = 8,8

# creates random mines

mineslist = []
for i in range(mr):
    mineslist.append([0]*mc)

cc = 0
while cc < mn:
    a = randint(0, mr-1)
    b = randint(0, mc-1)
    if mineslist[a][b] == 'M':
        pass
    else:
        mineslist[a][b] = 'M'
        cc += 1

for xx in range(mr):
    for yy in range(mc):
        mineslist[xx][yy] = checkad(xx, yy, mr, mc)

flagp = PhotoImage(file=".\\Flag.png")
minep = PhotoImage(file=".\\Mine.png")
emptyp = PhotoImage(file=".\\Empty.png")

blist = []

# initializing buttons in nested list
for row in range(rows):
    blist.append([0]*columns)
    for column in range(columns):
        blist[row][column] = Button(Game, text='u', image=emptyp, height=20,
                                            width=20, command=lambda row=row, column=column: clear(row, column))
        blist[row][column].bind(
            '<Button-3>', lambda event, row=row, column=column: flag(row, column, nomines))
        blist[row][column].grid(row=row, column=column)


Game.mainloop()
