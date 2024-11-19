import random
from tkinter import *

from snake import SnakeandLadder

root = Tk()
root.title("Snake and Ladder")


# Basic UI
n = 100
r = 0
label_dict = {}
while True:
    for i in range(1,11):
       
        lbl = Label(root,
                    bg = "yellow", 
                    height = 5,              
                    width = 20,
                    text = n,
                    borderwidth=1, 
                    relief="solid")
        lbl.grid(row = r , column = i)
        label_dict[n] = lbl
        n -= 1
        
    r += 1
    for i in range(10,0,-1):
        lbl = Label(root,
                    bg = "yellow", 
                    height = 5,              
                    width = 20,
                    text = n,
                    borderwidth=1, 
                    relief="solid"
                    )
        
        lbl.grid(row = r , column = i)
        label_dict[n] = lbl
        n -= 1
    r += 1
    if n<=0:
        break


label_dict[6].config(bg = "green2")
label_dict[24].config(bg = "green2")
label_dict[55].config(bg = "green2")
label_dict[85].config(bg = "green2")

label_dict[99].config(bg = "red2")
label_dict[40].config(bg = "red2")
label_dict[19].config(bg = "red2")


# Enter players
def click_to_continue():
    global player1 
    player1 = SnakeandLadder(e1.get())
    player1.color = "pink"
    player1.name = e1.get()
    global player2
    player2 = SnakeandLadder(e2.get())
    player2.name = e2.get()
    player2.color = "blue"
    b1.config(state=NORMAL)
    ok_button.config(state = DISABLED)
    global player
    player = player1
    return 

e1 = Entry(root, 
           textvariable="Player1",
           font=('Verdana',20),
           fg="pink"
           )
e1.grid(row=1,
        column=11
        )
e1.insert(0,"Player1")

ok_button = Button(root,text = "click to continue", command=click_to_continue)

ok_button.grid(row = 3, column = 11)
e2 = Entry(root,
           textvariable="Player2",
           font=('Verdana',20),
           fg = "blue"
           )

e2.grid(row=2,
        column=11
        )
e2.insert(0,"Player2")
# global player
# player = player1
# Roll dice
def roll_dice():
    global player
   
    while True:
        val = random.randint(1,6)
        if player.curr_pos in label_dict:
            prev_pos = player.curr_pos
            if prev_pos + val > 100:
                if val != 6:
                    if player == player1 :
                        player = player.update_player(player2)
                    else:
                        player = player.update_player(player1)
                e3.delete(0,END)
                e3.insert(0,player.name + "rolled a" + str(val))
                return
            else:
                label_dict[prev_pos].config(bg = "yellow",text = prev_pos)
            
        
        
        print(val,player.name,player.curr_pos)
        pos = player.update_pos(val)
        
        if pos and  pos == 100 :
            curr_button = label_dict[pos]
            curr_button.config(bg=player.color,text = player.name + " " + "Winner!!")
            b1.config(state=DISABLED)
            e3.delete(0,END)
            e3.insert(0,'Game over.')
            root.update()
            return
            
        if pos > 0 and player1.curr_pos == player2.curr_pos:
            curr_button = label_dict[pos]
            curr_button.config(bg = "orange" ,text = player1.name + player2.name)
        if  pos and pos < 100:
           
            curr_button = label_dict[pos]
            curr_button.config(bg=player.color,text = player.name)
            
            root.update()
        e3.delete(0,END)
        
       
        e3.insert(0,player.name +" rolled a " + str(val))
            
        if val != 6:
            if player == player1 :
                player = player.update_player(player2)
            else:
                player = player.update_player(player1)
        return val


b1 = Button(root, height=3, text = "Roll here!", command = roll_dice, bg = "medium spring green", state=DISABLED)

b1.grid(row=4, column=11, columnspan=1, sticky="n")
root.grid_columnconfigure(11, weight=1) 
e3 =  Entry(root, 
            bg = "purple1", 
            font=('Verdana',10)
            )
e3.grid(row=5,
        column=11,
        columnspan=3)


root.mainloop()