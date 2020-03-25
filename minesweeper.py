from tkinter import *
from tkinter import messagebox
from random import randint


class minesclass():
    def __init__(self, mr,mc,mn):

        self.mineslist = []
        for i in range(mr):
            self.mineslist.append([0]*mc)

        cc = 0
        while cc<mn:
            a = randint(0,mr-1)
            b = randint(0,mc-1)
            if self.mineslist[a][b] == 'M':
                pass
            else:
                self.mineslist[a][b] = 'M'
                cc +=1

        for xx in range(mr):
            for yy in range(mc):
                self.mineslist[xx][yy] = self.checkad(xx, yy,mr,mc)

    def checkad(self,x,y,mr,mc):
        if self.mineslist[x][y] == 'M':
            return 'M'
        else:
            s = 0
            for ii in range(x-1,x+2):
                for jj in range(y-1, y+2):
                    if ii in range(mr) and jj in range(mc):
                        if self.mineslist[ii][jj] == 'M':
                            s += 1
            return s


class minesweeperclass(Tk):
    def __init__(self, ro, co, no):
        Tk.__init__(self)

        self.geometry('{}x{}'.format((ro*26 + 26*5), (co*26)))

        self.minesleft = no
        
        frame = gridclass(self, ro, co, no)
        frame.grid(row = 0, column = 0, sticky = SW)

        minesleftlabel = Label(self, text = "Mines left :",)
        minesleftl = Label(self, text = self.minesleft)

        minesleftlabel.grid(row = 0, column = 3, sticky = N)
        minesleftl.grid(row = 0, column = 4, sticky = N)

        helpb = Button(self, text = 'Help', height = 1)
        helpb.grid(row = 0, column = 4)

        settingsb = Button(self, text = 'Settings')
        settingsb.grid(row = 0, column = 4, sticky = S)

class gridclass(Frame):
    def __init__(self, parent, r, c, n):
        Frame.__init__(self, parent)
        
        self.rows = r
        self.columns = c
        self.nomines = n
        self.mines = minesclass(self.rows, self.columns, self.nomines)

        self.flagp = PhotoImage(file = "C:\\Users\\talk2\\OneDrive\\Desktop\\Python\\minesweeper\\Flag.png")
        self.minep = PhotoImage(file = "C:\\Users\\talk2\\OneDrive\\Desktop\\Python\\minesweeper\\Mine.png")

        self.pixelvirtual = PhotoImage(height = 1, width = 1)

        self.blist = []
        #initializing buttons in nested list
        for row in range(self.rows):
            self.blist.append([0]*self.columns)
            for column in range(self.columns):
                self.blist[row][column] = Button(self,text = ' ',image = self.pixelvirtual ,height=20, width=20, command=lambda row=row, column=column: self.clear(row, column))
                self.blist[row][column].bind('<Button-3>', lambda event, row = row, column = column: self.flag(parent, row, column, self.nomines))
                self.blist[row][column].grid(row = row, column = column)

    def clear(self, iterator,jiterator):

        if self.mines.mineslist[iterator][jiterator] == 'M':        
            self.blist[iterator][jiterator].destroy()
            self.blist[iterator][jiterator] = Label(self,height = 24, width = 24,bd = 1,relief = 'ridge',image = self.minep)
            self.blist[iterator][jiterator].grid(row = iterator, column = jiterator)
            messagebox.showinfo("Game Over", "You stepped on a mine and lost!!")

        elif self.mines.mineslist[iterator][jiterator] == 0:
            self.blist[iterator][jiterator].destroy()
            self.blist[iterator][jiterator] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text = " ", font = 'Helvetica 14',)
            self.blist[iterator][jiterator].grid(row = iterator, column = jiterator)
            self.checko(iterator, jiterator)

        elif self.mines.mineslist[iterator][jiterator] == 1:
            self.blist[iterator][jiterator].destroy()
            self.blist[iterator][jiterator] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =1,font = 'Helvetica 14', fg = 'blue')
            self.blist[iterator][jiterator].grid(row = iterator, column = jiterator)

        elif self.mines.mineslist[iterator][jiterator] == 2:
            self.blist[iterator][jiterator].destroy()
            self.blist[iterator][jiterator] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =2,font = 'Helvetica 14', fg = 'green')
            self.blist[iterator][jiterator].grid(row = iterator, column = jiterator)

        elif self.mines.mineslist[iterator][jiterator] == 3:
            self.blist[iterator][jiterator].destroy()
            self.blist[iterator][jiterator] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =3,font = 'Helvetica 14', fg = 'red')
            self.blist[iterator][jiterator].grid(row = iterator, column = jiterator)

        elif self.mines.mineslist[iterator][jiterator] == 4:
            self.blist[iterator][jiterator].destroy()
            self.blist[iterator][jiterator] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =4,font = 'Helvetica 14', fg = 'orange')
            self.blist[iterator][jiterator].grid(row = iterator, column = jiterator)

        elif self.mines.mineslist[iterator][jiterator] == 5:
            self.blist[iterator][jiterator].destroy()
            self.blist[iterator][jiterator] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =5,font = 'Helvetica 14', fg = 'gold')
            self.blist[iterator][jiterator].grid(row = iterator, column = jiterator)

        elif self.mines.mineslist[iterator][jiterator] == 6:
            self.blist[iterator][jiterator].destroy()
            self.blist[iterator][jiterator] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =6,font = 'Helvetica 14', fg = 'yellow')
            self.blist[iterator][jiterator].grid(row = iterator, column = jiterator)

    def flag(self,parent, rr, cc, nn):
        # flagging
        if self.blist[rr][cc]['text'] == " ":
            self.blist[rr][cc].destroy()
            self.blist[rr][cc] = Button(self, image = self.flagp, height = 20, width = 20)
            self.blist[rr][cc].bind('<Button-3>', lambda event, rr = rr, cc = cc: self.flag(parent, rr, cc, nn))
            self.blist[rr][cc].grid(row = rr, column = cc)
            self.minescoreup(parent)
        # unflagging
        elif self.blist[rr][cc]['text'] == "":
            self.blist[rr][cc].destroy()
            self.blist[rr][cc] = Button(self,text=' ',image=self.pixelvirtual,height=20,width=20,command=lambda row=rr,column=cc:self.clear(row, column))
            self.blist[rr][cc].bind('<Button-3>', lambda event, rr = rr, cc = cc: self.flag(parent, rr, cc, nn))
            self.blist[rr][cc].grid(row = rr, column = cc)
            self.minescoredown(parent)

    def minescoreup(self, parent):
        parent.minesleft -= 1
        minesleftl = Label(parent, text = parent.minesleft)
        minesleftl.grid(row = 0, column = 4, sticky = N)
        if parent.minesleft == 0:
            self.checkwin()

    def minescoredown(self, parent):
        parent.minesleft += 1
        minesleftl = Label(parent, text = parent.minesleft)
        minesleftl.grid(row = 0, column = 4, sticky = N)
        if parent.minesleft == 0:
            self.checkwin()

    def checkwin(self):
        q = 0
        for k in range(self.rows):
            for l in range(self.columns):
                if type(self.blist[k][l]) == Button and self.blist[k][l]['text'] == "":
                    if self.mines.mineslist[k][l] == 'M':
                        q += 1
        if q == self.nomines:
            messagebox.showinfo("","YOU WIN !!!")

    def checko(self, i,j):
        for iii in range(i-1,i+2):
            for jjj in range(j-1, j+2):
                if iii in range(self.rows) and jjj in range(self.columns):
                    if type(self.blist[iii][jjj]) is Button:
                        self.clear(iii, jjj)


gameone = minesweeperclass(7,7,7)
gameone.mainloop()
