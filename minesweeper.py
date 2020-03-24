from tkinter import *
from tkinter import messagebox
from random import randint

r = 10
c = 10

def clear(iterator,jiterator):
    global mines
    if mines[iterator][jiterator] == 'M':        
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 24, width = 24,bd = 1,relief = 'ridge',image = minep)
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)
        messagebox.showinfo("Game Over", "You stepped on a mine and lost!!")

    elif mines[iterator][jiterator] == 0:
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2,bd = 1,relief = 'ridge', text = " ", font = 'Helvetica 14',)
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)
        checko(iterator, jiterator)

    elif mines[iterator][jiterator] == 1:
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2,bd = 1,relief = 'ridge', text =1,font = 'Helvetica 14', fg = 'blue')
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)

    elif mines[iterator][jiterator] == 2:
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2,bd = 1,relief = 'ridge', text =2,font = 'Helvetica 14', fg = 'green')
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)

    elif mines[iterator][jiterator] == 3:
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2,bd = 1,relief = 'ridge', text =3,font = 'Helvetica 14', fg = 'red')
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)

    elif mines[iterator][jiterator] == 4:
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2,bd = 1,relief = 'ridge', text =4,font = 'Helvetica 14', fg = 'orange')
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)

    elif mines[iterator][jiterator] == 5:
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2,bd = 1,relief = 'ridge', text =5,font = 'Helvetica 14', fg = 'gold')
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)

    elif mines[iterator][jiterator] == 6:
        blist[iterator][jiterator].destroy()
        blist[iterator][jiterator] = Label(frame,height = 1, width = 2,bd = 1,relief = 'ridge', text =6,font = 'Helvetica 14', fg = 'yellow')
        blist[iterator][jiterator].grid(row = iterator, column = jiterator)


def checko(i,j):
    global mines
    for iii in range(i-1,i+2):
        for jjj in range(j-1, j+2):
            if iii in range(r) and jjj in range(c):
                if type(blist[iii][jjj]) is Button:
                    clear(iii, jjj)



def rightc(rr, cc):
    if blist[rr][cc]['text'] == " ":
        blist[rr][cc].destroy()
        blist[rr][cc] = Button(frame, image = flagp, height = 20, width = 20)
        blist[rr][cc].bind('<Button-3>', lambda event, rr = rr, cc = cc: rightc(rr, cc))
        blist[rr][cc].grid(row = rr, column = cc)
    elif blist[rr][cc]['text'] == "":
        blist[rr][cc].destroy()
        blist[rr][cc] = Button(frame,text=' ',image=pixelvirtual,height=20,width=20,command=lambda row=rr,column=cc:clear(row, column))
        blist[rr][cc].bind('<Button-3>', lambda event, rr = rr, cc = cc: rightc(rr, cc))
        blist[rr][cc].grid(row = rr, column = cc)
    

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

def checkwin():
    for k in range(r):
        pass

mines = []
for i in range(r):
    mines.append([0]*c)

cc = 0
while cc<15:
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

pixelvirtual = PhotoImage(height = 1, width = 1)

blist = []
#initializing buttons in nested list
for row in range(r):
    blist.append([0]*c)
    for column in range(c):
        blist[row][column] = Button(frame,text = ' ',image = pixelvirtual ,height=20, width=20, command=lambda row=row, column=column: clear(row, column))
        blist[row][column].bind('<Button-3>', lambda event, row = row, column = column: rightc(row, column))
        blist[row][column].grid(row = row, column = column)

flagp = PhotoImage(file = "C:\\Users\\talk2\\OneDrive\\Desktop\\Python\\minesweeper\\Flag.png")
minep = PhotoImage(file = "C:\\Users\\talk2\\OneDrive\\Desktop\\Python\\minesweeper\\Mine.png")

checkwin()

frame.pack()

root.mainloop()