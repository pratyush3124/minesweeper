from tkinter import Tk, Frame, Button, Label, PhotoImage, Canvas, Entry
from tkinter import messagebox
from random import randint


def Play():

    mr,rows = 8,8
    mc,columns = 8,8
    mn,nomines = 8,8

    minesleft = mn

    blist = []


    def clear(xcord, ycord):

        # clearing stuff when clicked
        if mineslist[xcord][ycord] == 'M':
            blist[xcord][ycord].destroy()
            blist[xcord][ycord] = Label(
                frame, height=24, width=24, bd=1, relief='ridge', image=minep)
            blist[xcord][ycord].grid(row=xcord, column=ycord)
            messagebox.showinfo(
                "Game Over", "You stepped on a mine and lost!!")
            # aftergame()

        elif mineslist[xcord][ycord] == 0:
            blist[xcord][ycord].destroy()
            blist[xcord][ycord] = Label(
                frame, height=1, width=2, bd=1, relief='ridge', text=" ", font='Helvetica 14',)
            blist[xcord][ycord].grid(row=xcord, column=ycord)
            checkad(xcord, ycord)

        elif mineslist[xcord][ycord] == 1:
            blist[xcord][ycord].destroy()
            blist[xcord][ycord] = Label(
                frame, height=1, width=2, bd=1, relief='ridge', text=1, font='Helvetica 14', fg='blue')
            blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif mineslist[xcord][ycord] == 2:
            blist[xcord][ycord].destroy()
            blist[xcord][ycord] = Label(
                frame, height=1, width=2, bd=1, relief='ridge', text=2, font='Helvetica 14', fg='green')
            blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif mineslist[xcord][ycord] == 3:
            blist[xcord][ycord].destroy()
            blist[xcord][ycord] = Label(
                frame, height=1, width=2, bd=1, relief='ridge', text=3, font='Helvetica 14', fg='red')
            blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif mineslist[xcord][ycord] == 4:
            blist[xcord][ycord].destroy()
            blist[xcord][ycord] = Label(
                frame, height=1, width=2, bd=1, relief='ridge', text=4, font='Helvetica 14', fg='orange')
            blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif mineslist[xcord][ycord] == 5:
            blist[xcord][ycord].destroy()
            blist[xcord][ycord] = Label(
                frame, height=1, width=2, bd=1, relief='ridge', text=5, font='Helvetica 14', fg='gold')
            blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif mineslist[xcord][ycord] == 6:
            blist[xcord][ycord].destroy()
            blist[xcord][ycord] = Label(
                frame, height=1, width=2, bd=1, relief='ridge', text=6, font='Helvetica 14', fg='yellow')
            blist[xcord][ycord].grid(row=xcord, column=ycord)

    def flag(rr, cc, nn):
        # flagging
        if blist[rr][cc]['text'] == "u":
            blist[rr][cc].destroy()
            blist[rr][cc] = Button(
                frame, text='f', image=flagp, height=20, width=20)
            blist[rr][cc].bind(
                '<Button-3>', lambda event, rr=rr, cc=cc: flag(rr, cc, nn))
            blist[rr][cc].grid(row=rr, column=cc)
            minescore(1)
        # unflagging
        elif blist[rr][cc]['text'] == "f":
            blist[rr][cc].destroy()
            blist[rr][cc] = Button(frame, text='u', image=emptyp, height=20,
                                        width=20, command=lambda row=rr, column=cc: clear(row, column))
            blist[rr][cc].bind(
                '<Button-3>', lambda event, rr=rr, cc=cc: flag(rr, cc, nn))
            blist[rr][cc].grid(row=rr, column=cc)
            minescore(-1)

    def minescore(s):
        nonlocal minesleft
        minesleft -= s
        mineslabel['text'] = minesleft
        if minesleft == 0:
            checkwin()

    def checkad(i, j):
        # clearing adjacent empty squares automatically
        for iii in range(i-1, i+2):
            for jjj in range(j-1, j+2):
                if iii in range(rows) and jjj in range(columns):
                    if type(blist[iii][jjj]) is Button:
                        clear(iii, jjj)

    def checknum(x, y, mr, mc):
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

    def playagain():
        Game.destroy()
        Play()

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

    Game = Tk()

    frame = Frame(Game)
    frame.grid(row=0,column=0)

    playagb = Button(Game,text='Play Again',command=playagain)
    playagb.grid(row=1,column=1)

    minesleftl = Label(Game,text='Mines Left = ')
    mineslabel = Label(Game,text=minesleft)

    minesleftl.grid(row=0,column=1)
    mineslabel.grid(row=0,column=2)

    flagp = PhotoImage(file=".\\Flag.png")
    minep = PhotoImage(file=".\\Mine.png")
    emptyp = PhotoImage(file=".\\Empty.png")

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
            mineslist[xx][yy] = checknum(xx, yy, mr, mc)

    

    # initializing buttons in nested list
    for row in range(rows):
        blist.append([0]*columns)
        for column in range(columns):
            blist[row][column] = Button(frame, text='u', image=emptyp, height=20,
                                                width=20, command=lambda row=row, column=column: clear(row, column))
            blist[row][column].bind(
                '<Button-3>', lambda event, row=row, column=column: flag(row, column, nomines))
            blist[row][column].grid(row=row, column=column)


    Game.mainloop()


Play()