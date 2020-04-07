from tkinter import Tk, Frame, Button, Label, PhotoImage,Canvas,Entry
from tkinter import messagebox
from random import randint

class minesweeperclass(Tk):
    def __init__(self, ro, co, no):
        Tk.__init__(self)

        # main window
        self.geometry('{}x{}'.format((ro*26 + 26*5), (co*26)))

        self.minesleft = no
        
        self.frame = gridclass(self, ro, co, no)
        self.frame.grid(row = 0, column = 0)

        self.minesleftlabel = Label(self, text = "Mines left :",)
        self.minesleftl = Label(self, text = self.minesleft)

        self.minesleftlabel.grid(row = 0, column = 2, sticky = 'N')
        self.minesleftl.grid(row = 0, column = 3, sticky = 'N')

        self.helpb = Button(self, text = 'Help', height = 1)
        self.helpb.grid(row = 0, column = 3)

        self.settingsb = Button(self, text = 'Settings', command = lambda: self.settings())
        self.settingsb.grid(row = 0, column = 3, sticky = 'S')

    def settings(self):
        spage = Settings(self)
        spage.mainloop()


class gridclass(Frame):
    def __init__(self, parent, r, c, n):
        Frame.__init__(self, parent)

        # grid
        self.rows = r
        self.columns = c
        self.nomines = n
        self.mines = minesclass(self.rows, self.columns, self.nomines)

        self.flagp = PhotoImage(file = ".\\Flag.png")
        self.minep = PhotoImage(file = ".\\Mine.png")
        self.empty = PhotoImage(file = ".\\Empty.png")

        self.blist = []

        # initializing buttons in nested list
        for row in range(self.rows):
            self.blist.append([0]*self.columns)
            for column in range(self.columns):
                self.blist[row][column] = Button(self,text = ' ',image = self.empty ,height=20, width=20, command=lambda row=row, column=column: self.clear(parent, row, column))
                self.blist[row][column].bind('<Button-3>', lambda event, row = row, column = column: self.flag(parent, row, column, self.nomines))
                self.blist[row][column].grid(row = row, column = column)

    def clear(self, parent, xcord,ycord):

        # clearing stuff when clicked
        if self.mines.mineslist[xcord][ycord] == 'M':        
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(self,height = 24, width = 24,bd = 1,relief = 'ridge',image = self.minep)
            self.blist[xcord][ycord].grid(row = xcord, column = ycord)
            messagebox.showinfo("Game Over", "You stepped on a mine and lost!!")
            self.aftergame(parent)

        elif self.mines.mineslist[xcord][ycord] == 0:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text = " ", font = 'Helvetica 14',)
            self.blist[xcord][ycord].grid(row = xcord, column = ycord)
            self.checko(parent, xcord, ycord)

        elif self.mines.mineslist[xcord][ycord] == 1:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =1,font = 'Helvetica 14', fg = 'blue')
            self.blist[xcord][ycord].grid(row = xcord, column = ycord)

        elif self.mines.mineslist[xcord][ycord] == 2:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =2,font = 'Helvetica 14', fg = 'green')
            self.blist[xcord][ycord].grid(row = xcord, column = ycord)

        elif self.mines.mineslist[xcord][ycord] == 3:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =3,font = 'Helvetica 14', fg = 'red')
            self.blist[xcord][ycord].grid(row = xcord, column = ycord)

        elif self.mines.mineslist[xcord][ycord] == 4:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =4,font = 'Helvetica 14', fg = 'orange')
            self.blist[xcord][ycord].grid(row = xcord, column = ycord)

        elif self.mines.mineslist[xcord][ycord] == 5:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =5,font = 'Helvetica 14', fg = 'gold')
            self.blist[xcord][ycord].grid(row = xcord, column = ycord)

        elif self.mines.mineslist[xcord][ycord] == 6:
            self.blist[xcord][ycord].destroy()
            self.blist[xcord][ycord] = Label(self,height = 1, width = 2,bd = 1,relief = 'ridge', text =6,font = 'Helvetica 14', fg = 'yellow')
            self.blist[xcord][ycord].grid(row = xcord, column = ycord)

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
            self.blist[rr][cc] = Button(self,text=' ',image=self.empty,height=20,width=20,command=lambda row=rr,column=cc:self.clear(parent, row, column))
            self.blist[rr][cc].bind('<Button-3>', lambda event, rr = rr, cc = cc: self.flag(parent, rr, cc, nn))
            self.blist[rr][cc].grid(row = rr, column = cc)
            self.minescoredown(parent)

    def minescoreup(self, parent):
        # scoring up
        parent.minesleft -= 1
        parent.minesleftl.destroy()
        parent.minesleftl = Label(parent, text = parent.minesleft)
        parent.minesleftl.grid(row = 0, column = 3, sticky = 'N')
        if parent.minesleft == 0:
            self.checkwin(parent)

    def minescoredown(self, parent):
        # scoring down
        parent.minesleft += 1
        parent.minesleftl.destroy()
        parent.minesleftl = Label(parent, text = parent.minesleft)
        parent.minesleftl.grid(row = 0, column = 3, sticky = 'N')
        if parent.minesleft == 0:
            self.checkwin(parent)

    def checkwin(self, parent):
        # checking if won
        q = 0
        for k in range(self.rows):
            for l in range(self.columns):
                if type(self.blist[k][l]) == Button and self.blist[k][l]['text'] == "":
                    if self.mines.mineslist[k][l] == 'M':
                        q += 1
        if q == self.nomines:
            messagebox.showinfo("","YOU WIN !!!")
            self.aftergame(parent)
           

    def checko(self,parent, i,j):
        # clearing adjacent empty squares automatically
        for iii in range(i-1,i+2):
            for jjj in range(j-1, j+2):
                if iii in range(self.rows) and jjj in range(self.columns):
                    if type(self.blist[iii][jjj]) is Button:
                        self.clear(parent, iii, jjj)

    def aftergame(self, parent):
        
        # after game screen
        self.destroy()

        parent.geometry('{}x{}'.format(130,170))

        parent.minesleftlabel['text'] = "      "
        parent.minesleftlabel.grid(row = 0, column = 1, sticky = 'N')
        parent.minesleftl.destroy()

        parent.lone = Label(parent, text = "")
        parent.lone.grid(row = 2, column = 0)

        parent.helpb.grid(row = 1, column = 2)

        parent.settingsb.grid(row = 3, column = 2)

        parent.lthree = Label(parent, text = " ")
        parent.lthree.grid(row = 4, column = 0)

        parent.playagainb = Button(parent, text = "Play Again", command = lambda: self.playagain(parent))
        parent.playagainb.grid(row = 5, column = 2)

    def playagain(self, parent):
        parent.destroy()
        gametwo = minesweeperclass(self.rows, self.columns, self.nomines)
        gametwo.mainloop()


class minesclass():
    def __init__(self, mr,mc,mn):
        # creates random mines

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

class Settings(Tk):
    def __init__(self,parent):
        Tk.__init__(self)

        self.rows = 1
        self.columns = 1

        a = Button(self, text = '7x7', command = lambda: self.configure(5,5,5,parent))
        a.pack()

        b = Button(self, text = '10x10', command = lambda: self.configure(10,10,10,parent))
        b.pack()

        c = Button(self, text = '15x15', command = lambda: self.configure(15,15,20,parent))
        c.pack()

        custom = Button(self, text = 'Custom', command = lambda: self.customscreen(parent))
        custom.pack()

    def configure(self,r,c,n,parent):
        self.rows = r
        self.columns = c
        self.mines = n
        parent.destroy()
        newgame = minesweeperclass(r,c,n)
        self.destroy()
        newgame.mainloop()

    def customscreen(self,parent):
        parent.destroy()
        self.destroy()
        self.cs = customscreen()
        self.cs.mainloop()
        

class customscreen(Tk):
    def __init__(self):
        Tk.__init__(self)

        c1 = Canvas(self, width = 300, height = 300)
        w = Label(self, text="SETTINGS")
        w.pack()

        c1.pack()

        self.entry1 = Entry (self) 
        c1.create_window(180, 50, window=self.entry1)
        self.entry2 = Entry (self) 
        c1.create_window(180, 100, window=self.entry2)
        self.entry3 = Entry (self) 
        c1.create_window(180, 150, window=self.entry3)

        label1= Label(self, text="ROWS :")
        c1.create_window(80, 50,window=label1)

        label2= Label(self, text="COLUMNS :")
        c1.create_window(80, 100,window=label2)

        label3= Label(self, text="MINES :")
        c1.create_window(80,150,window=label3)
        

        button1 = Button(text='START',bg='brown', fg='white',height=2,width=5, command = lambda:self.startgame())
        c1.create_window(170, 240, window=button1)

    def startgame(self):
        e1 = self.entry1.get()
        e2 = self.entry2.get()
        e3 = self.entry3.get()
        if e1 == '' or e2 == '' or e3 == '':
            warning = Label(self, text = 'Please fill all the fields')
            c1.create_window(180,200, window = warning)
        else:
            print(e1,e2, e3)



if __name__ == "__main__":
    gameone = minesweeperclass(7,7,7)
    gameone.mainloop()
