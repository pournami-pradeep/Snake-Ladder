import random
from tkinter import *

from snake import SnakeandLadder

root = Tk()
root.title("Snake and Ladder")

# Basic UI
n = 100
r = 5
label_dict = {}
col = 5
while True:
    for i in range(1,11):
        lbl = Label(root,
                    bg = "yellow", 
                    height = 5,              
                    width = 15,
                    text = n,
                    borderwidth=1, 
                    relief="solid")
        lbl.grid(row = r , column = col)
        label_dict[n] = lbl
        n -= 1
        col += 1
     
    r += 1
    col = 14
    for i in range(10,0,-1):
        lbl = Label(root,
                    bg = "yellow", 
                    height = 5,              
                    width = 15,
                    text = n,
                    borderwidth=1, 
                    relief="solid"
                    )
        
        lbl.grid(row = r , column = col)
        label_dict[n] = lbl
        n -= 1
        col -= 1
    r += 1
    col = 5
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
    player1 = SnakeandLadder(e2.get())
    player1.color = "pink"
    player1.name = e2.get()
    global player2
    player2 = SnakeandLadder(e1.get())
    player2.name = e1.get()
    player2.color = "blue"
    player1_btn.config(state=NORMAL)
    ok_button.config(state = DISABLED)
    global player
    player = player1
    # pause_button.config(state=NORMAL)
    return 

# def click_to_continue():
#     pause_button.config(state = NORMAL)
#     if player == player1:
#         player1_btn.config(state=NORMAL)
#     else:
#         player2_btn.config(state=NORMAL)
#     return

e1 = Entry(root, 
           textvariable="Player2",
           font=('Verdana',20),
           fg="pink",
           width=18
           )
e1.grid(row=7,
        column=0,
        pady=3,
        padx=2
        )
e1.insert(0,"Player2")

# def click_to_pause():
#     player1_btn.config(state=DISABLED)
#     player2_btn.config(state=DISABLED)
#     resume_button.config(state=NORMAL)
#     return
    

ok_button = Button(root,text = "click to start game", command=click_to_continue,bg="green")

ok_button.grid(row = 0, column = 6,columnspan=2)
# pause_button = Button(root,text = "click to pause game", command=click_to_pause,bg="green",state=DISABLED)

# pause_button.grid(row = 0, column = 9,columnspan=2)

# resume_button = Button(root,text = "click to continue",  bg = "green", state=DISABLED)
# resume_button.grid(row = 0, column = 12,columnspan=2)
e2 = Entry(root,
           textvariable="Player1",
           font=('Verdana',20),
           fg = "blue",
           width=18
           )

e2.grid(row=7,
        column=16
        )
e2.insert(0,"Player1")
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
                        player1_btn.config(state=DISABLED)
                        player2_btn.config(state=NORMAL)
                    else:
                        player = player.update_player(player1)
                        player2_btn.config(state=DISABLED)
                        player1_btn.config(state=NORMAL)
                if player == player1 :
                    e3.delete(0,END)
                    e3.insert(0,player.name + "rolled a" + str(val))
                if player == player2:
                    e4.delete(0,END)
                    e4.insert(0,player.name + "rolled a " + str(val))

                return
            else:
                label_dict[prev_pos].config(bg = "yellow",text = prev_pos)
            
        
        
        print(val,player.name,player.curr_pos)
        pos = player.update_pos(val)
        
        if pos and  pos == 100 :
            curr_button = label_dict[pos]
            curr_button.config(bg=player.color,text = player.name + " " + "Winner!!")
            player1_btn.config(state=DISABLED)
            player2_btn.config(state=DISABLED)
            if player == player1:
                e3.delete(0,END)
                e3.insert(0,'You won!!')
                e4.delete(0,END)
                e4.insert(0,'You lose.')
            else:
                e3.delete(0,END)
                e3.insert(0,'You lose.')
                e4.delete(0,END)
                e4.insert(0,'You won!!')
                
            root.update()
            return
            
        if pos > 0 and player1.curr_pos == player2.curr_pos:
            curr_button = label_dict[pos]
            curr_button.config(bg = "orange" ,text = player1.name + player2.name)
            continue
        if  pos and pos < 100:
           
            curr_button = label_dict[pos]
            curr_button.config(bg=player.color,text = player.name)
            
            root.update()
        if player == player1:
            e3.delete(0,END)
            e3.insert(0,player.name +" rolled a " + str(val))
        else:
            e4.delete(0,END)
            e4.insert(0,player.name + " rolled a " + str(val))
            
        if val != 6 and pos not in player.snake_ladder:
            if player == player1 :
                player = player.update_player(player2)
                player1_btn.config(state=DISABLED)
                player2_btn.config(state=NORMAL)
            else:
                player = player.update_player(player1)
                player2_btn.config(state=DISABLED)
                player1_btn.config(state=NORMAL)
        return val


player1_btn = Button(root, height=3, text = "Roll here!", command = roll_dice, bg = "medium spring green", state=DISABLED)

player1_btn.grid(row=8, column=16, columnspan=1, sticky="n")
root.grid_columnconfigure(16, weight=1) 
player2_btn = Button(root, height=3, text = "Roll here!", command = roll_dice, bg = "medium spring green", state=DISABLED)

player2_btn.grid(row=8, column=0, columnspan=1, sticky="n")
e3 =  Entry(root, 
            bg = "purple1", 
            font=('Verdana',10)
            )
e3.grid(row=9,
        column=16,
        columnspan=3)
e4 =  Entry(root, 
            bg = "purple1", 
            font=('Verdana',10)
            )
e4.grid(row=9,
        column=0,
        columnspan=3)


root.mainloop()