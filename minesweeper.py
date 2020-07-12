from tkinter import Tk, Frame, Button, Label, PhotoImage, Canvas, Entry
from tkinter import messagebox
from random import randint


class Game(Tk):
    def __init__(self, ro, co, no):
        Tk.__init__(self)

        # main window
        self.geometry('{}x{}'.format((ro*26 + 26*5), (co*26)))
        self.bg = 'gray'
        self['bg'] = self.bg

        self.minesleft = no

        self.flagp = PhotoImage(file=".\\Flag.png")
        self.minep = PhotoImage(file=".\\Mine.png")
        self.emptyp = PhotoImage(file=".\\Empty.png")

        self.frame = Grid(self, ro, co, no)
        self.frame.grid(row=0, column=0)

        self.minesleftlabel = Label(self, text="Mines left :", bg=self.bg)
        self.minesleftl = Label(self, text=self.minesleft, bg=self.bg)

        self.minesleftlabel.grid(row=0, column=2, sticky='N')
        self.minesleftl.grid(row=0, column=3, sticky='N')

        self.helpb = Button(self, text='Help', height=1, bg=self.bg)
        self.helpb.grid(row=0, column=3)

        self.settingsb = Button(self, text='Settings',
                                command=lambda: self.settings(), bg=self.bg)
        self.settingsb.grid(row=0, column=3, sticky='S')

    def settings(self):
        self.settingsw = Tk()

        a = Button(self.settingsw, text='7x7',
                   command=lambda: self.config(5, 5, 5))
        a.pack()

        b = Button(self.settingsw, text='10x10',
                   command=lambda: self.config(10, 10, 10))
        b.pack()

        c = Button(self.settingsw, text='15x15',
                   command=lambda: self.config(15, 15, 20))
        c.pack()

        custom = Button(self.settingsw, text='Custom',
                        command=lambda: self.customscreen())
        custom.pack()

    def config(self, r, c, n):
        self.destroy()
        self.settingsw.destroy()
        newgame = Game(r, c, n)
        newgame.mainloop()

    def customscreen(self):
        self.csw = Tk()
        self.c1 = Canvas(self.csw, width=300, height=300)
        w = Label(self.csw, text="SETTINGS")
        w.pack()

        self.c1.pack()

        self.entry1 = Entry(self.csw)
        self.c1.create_window(180, 50, window=self.entry1)
        self.entry2 = Entry(self.csw)
        self.c1.create_window(180, 100, window=self.entry2)
        self.entry3 = Entry(self.csw)
        self.c1.create_window(180, 150, window=self.entry3)

        label1 = Label(self.csw, text="ROWS :")
        self.c1.create_window(80, 50, window=label1)

        label2 = Label(self.csw, text="COLUMNS :")
        self.c1.create_window(80, 100, window=label2)

        label3 = Label(self.csw, text="MINES :")
        self.c1.create_window(80, 150, window=label3)

        button1 = Button(self.csw, text='START', bg='brown', fg='white',
                         height=2, width=5, command=lambda: self.startgame())
        self.c1.create_window(170, 240, window=button1)

    def startgame(self):
        e1 = self.entry1.get()
        e2 = self.entry2.get()
        e3 = self.entry3.get()
        if e1 == '' or e2 == '' or e3 == '':
            warning = Label(self, text='Please fill all the fields')
            self.c1.create_window(180, 200, window=warning)
        else:
            self.destroy()
            self.settingsw.destroy()
            self.csw.destroy()
            gamethree = Game(int(e1), int(e2), int(e3))
            gamethree.mainloop()


class Grid(Frame):
    def __init__(self, parent, r, c, n):
        Frame.__init__(self, parent)

        self.parent = parent

        # grid
        self.rows = r
        self.columns = c
        self.nomines = n
        self.mines = Mines(self.rows, self.columns, self.nomines)

        self.blist = []

        # initializing buttons in nested list
        for row in range(self.rows):
            self.blist.append([0]*self.columns)
            for column in range(self.columns):
                self.blist[row][column] = Button(self, text='u', image=self.parent.emptyp, height=20,
                                                 width=20, command=lambda row=row, column=column: self.clear(row, column))
                self.blist[row][column].bind(
                    '<Button-3>', lambda event, row=row, column=column: self.flag(row, column, self.nomines))
                self.blist[row][column].grid(row=row, column=column)

    def clear(self, xcord, ycord):

        # clearing stuff when clicked
        if self.mines.mineslist[xcord][ycord] == 'M':
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(
                self, height=24, width=24, bd=1, relief='ridge', image=self.parent.minep)
            self.blist[xcord][ycord].grid(row=xcord, column=ycord)
            messagebox.showinfo(
                "Game Over", "You stepped on a mine and lost!!")
            self.aftergame()

        elif self.mines.mineslist[xcord][ycord] == 0:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(
                self, height=1, width=2, bd=1, relief='ridge', text=" ", font='Helvetica 14',)
            self.blist[xcord][ycord].grid(row=xcord, column=ycord)
            self.checko(xcord, ycord)

        elif self.mines.mineslist[xcord][ycord] == 1:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(
                self, height=1, width=2, bd=1, relief='ridge', text=1, font='Helvetica 14', fg='blue')
            self.blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif self.mines.mineslist[xcord][ycord] == 2:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(
                self, height=1, width=2, bd=1, relief='ridge', text=2, font='Helvetica 14', fg='green')
            self.blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif self.mines.mineslist[xcord][ycord] == 3:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(
                self, height=1, width=2, bd=1, relief='ridge', text=3, font='Helvetica 14', fg='red')
            self.blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif self.mines.mineslist[xcord][ycord] == 4:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(
                self, height=1, width=2, bd=1, relief='ridge', text=4, font='Helvetica 14', fg='orange')
            self.blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif self.mines.mineslist[xcord][ycord] == 5:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(
                self, height=1, width=2, bd=1, relief='ridge', text=5, font='Helvetica 14', fg='gold')
            self.blist[xcord][ycord].grid(row=xcord, column=ycord)

        elif self.mines.mineslist[xcord][ycord] == 6:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(
                self, height=1, width=2, bd=1, relief='ridge', text=6, font='Helvetica 14', fg='yellow')
            self.blist[xcord][ycord].grid(row=xcord, column=ycord)

    def flag(self, rr, cc, nn):
        # flagging
        if self.blist[rr][cc]['text'] == "u":
            self.blist[rr][cc].destroy()
            self.blist[rr][cc] = Button(
                self, text='f', image=self.parent.flagp, height=20, width=20)
            self.blist[rr][cc].bind(
                '<Button-3>', lambda event, rr=rr, cc=cc: self.flag(rr, cc, nn))
            self.blist[rr][cc].grid(row=rr, column=cc)
            self.minescoreup()
        # unflagging
        elif self.blist[rr][cc]['text'] == "f":
            self.blist[rr][cc].destroy()
            self.blist[rr][cc] = Button(self, text='u', image=self.parent.emptyp, height=20,
                                        width=20, command=lambda row=rr, column=cc: self.clear(row, column))
            self.blist[rr][cc].bind(
                '<Button-3>', lambda event, rr=rr, cc=cc: self.flag(rr, cc, nn))
            self.blist[rr][cc].grid(row=rr, column=cc)
            self.minescoredown()

    def minescoreup(self):
        # scoring up
        self.parent.minesleft -= 1
        self.parent.minesleftl['text'] = self.parent.minesleft
        if self.parent.minesleft == 0:
            self.checkwin()

    def minescoredown(self):
        # scoring down
        self.parent.minesleft += 1
        self.parent.minesleftl['text'] = self.parent.minesleft
        if self.parent.minesleft == 0:
            self.checkwin()

    def checkwin(self):
        # checking if won
        q = 0
        for k in range(self.rows):
            for l in range(self.columns):
                if type(self.blist[k][l]) == Button and self.blist[k][l]['text'] == "f":
                    if self.mines.mineslist[k][l] == 'M':
                        q += 1
        if q == self.nomines:
            messagebox.showinfo("", "YOU WIN !!!")
            self.aftergame()

    def checko(self, i, j):
        # clearing adjacent empty squares automatically
        for iii in range(i-1, i+2):
            for jjj in range(j-1, j+2):
                if iii in range(self.rows) and jjj in range(self.columns):
                    if type(self.blist[iii][jjj]) is Button:
                        self.clear(iii, jjj)

    def aftergame(self):
        # after game screen
        self.destroy()

        self.parent.geometry('{}x{}'.format(150, 180))

        self.parent.minesleftlabel['text'] = "      "
        self.parent.minesleftlabel.grid(row=0, column=1, sticky='N')
        self.parent.minesleftl.destroy()

        self.parent.lone = Label(self.parent, text="", bg=self.parent.bg)
        self.parent.lone.grid(row=2, column=0)

        self.parent.helpb.grid(row=1, column=2)

        self.parent.settingsb.grid(row=3, column=2)

        self.parent.lthree = Label(self.parent, text=" ", bg=self.parent.bg)
        self.parent.lthree.grid(row=4, column=0)

        self.parent.playagainb = Button(
            self.parent, text="Play Again", command=lambda: self.playagain(), bg=self.parent.bg)
        self.parent.playagainb.grid(row=5, column=2)

    def playagain(self):
        self.parent.destroy()
        gametwo = Game(self.rows, self.columns, self.nomines)
        gametwo.mainloop()


class Mines():
    def __init__(self, mr, mc, mn):
        # creates random mines

        self.mineslist = []
        for i in range(mr):
            self.mineslist.append([0]*mc)

        cc = 0
        while cc < mn:
            a = randint(0, mr-1)
            b = randint(0, mc-1)
            if self.mineslist[a][b] == 'M':
                pass
            else:
                self.mineslist[a][b] = 'M'
                cc += 1

        for xx in range(mr):
            for yy in range(mc):
                self.mineslist[xx][yy] = self.checkad(xx, yy, mr, mc)

    def checkad(self, x, y, mr, mc):
        if self.mineslist[x][y] == 'M':
            return 'M'
        else:
            s = 0
            for ii in range(x-1, x+2):
                for jj in range(y-1, y+2):
                    if ii in range(mr) and jj in range(mc):
                        if self.mineslist[ii][jj] == 'M':
                            s += 1
            return s


if __name__ == '__main__':
    gameone = Game(6, 6, 3)
    gameone.mainloop()
