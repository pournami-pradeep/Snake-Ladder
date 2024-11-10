import random
from tkinter import *

# from snake import SnakeandLadder

root = Tk()
root.title("Snake & Ladder")

# one to hundred UI
n = 100
r = 0
while True:

    for i in range(1,11):
        button = Button(root, text = n, bg = "white")
        button.grid(row = r, column=i)
        n -= 1
    
    r += 1   

    for i in range(10,0,-1):
        button = Button(root, text = n, bg = "white")
        button.grid(row = r,column=i)
        n -= 1
    r += 1
    if n <= 0:
        break


# button for start game and endgame
b1 = Button(root, text = "START GAME", bg = "green")
b2 = Button(root, text = "END GAME", bg = "red")
b1.grid(row=0,column= 11)
b2.grid(row=0,column=12)

# Enter players
e1 = Entry(root, textvariable="Player1")
e1.grid(row=1,column=11, columnspan=2)
e1.insert(0,"Player1")
e2 = Entry(root,textvariable="Player2")
e2.grid(row=2,column=11, columnspan=2)
e2.insert(0,"Player2")

# Roll dice
e3 =  Entry(root, bg = "yellow")
e3.grid(row=4,column=12, rowspan=3)

def roll_dice():
    val = random.randint(1,6)
    e3.delete(0,END)
    e3.insert(0,"You rolled a " + str(val))
    return val
dice_btn = PhotoImage(file=r"image.png")
dice_btn = dice_btn.subsample(5,5)
b1 = Button(root, image=dice_btn, command= roll_dice)

b1.grid(row=4,column= 11, rowspan=3)



# print(e1.get())
# # Create Players
# player1 = SnakeandLadder(e1.get())
# player2 = SnakeandLadder(e2.get())

# b4 = Button(root, text = "Ok")
# b4.pack()




#Roll dice

# i = 0
# def roll_dice(i):
#     if i % 2 == 0:
#         player = player1
#     else:
#         player = player2
#     val = random.randint(1,6)
#     player.update_pos(val)
#     return val
# b3 = Button(root, text = "ROLL", bg = "blue" ,command = roll_dice)

# b3.pack()
# print(player.curr_pos)

root.mainloop()