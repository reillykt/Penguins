import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

player1 = 0
player2 = 0
# asking players where they want to start the game
possible_numbers = [1,2,3,4,5,6,7,8,9,0]
def starting_positions():
    player1 = int(input("Player 1: To choose a starting location, enter a digit (0-9): "))
    while player1 not in possible_numbers:
        print("Not a digit!")
        player1 = input("Player 1: To choose a starting location, enter a digit (0-9): ")
    player2 = int(input("Player 2: To choose a starting location, enter a digit (0-9): "))
    while player2 not in possible_numbers:
        print("Not a digit!")
        player2 = input("Player 2: To choose a starting location, enter a digit (0-9): ")
    return player1, player2
player1, player2 = starting_positions()

game_status = True
round = 1
possible_rounds=["Grid 1","Grid 2","Grid 3"]

class Location:
    def __init__(self, neighbors, aliveness, name):
        self.neighbors = neighbors  # instance variable
        self.aliveness = aliveness  # instance variable
        self.name = name
    


#round_neighbors = # either 1, 2, n (which round of edges)

location0 = Location([], True, "Iceberg 0")
location1 = Location([], True, "Iceberg 1")
# if statement connecting which round edges they select and what the neighbors are
location2 = Location([], True, "Iceberg 2")
location3 = Location([], True, "Iceberg 3")
location4 = Location([], True, "Iceberg 4")
location5 = Location([], True, "Iceberg 5")
location6 = Location([], True, "Iceberg 6")
location7 = Location([], True, "Iceberg 7")
location8 = Location([], True, "Iceberg 8")
location9 = Location([], True, "Iceberg 9")
if round == 1:
    location0.neighbors = [0,1,3,9]
    location1.neighbors = [1,0,4]
    location2.neighbors = [2,3,4,9]
    location3.neighbors = [3,0,2,6,9]
    location4.neighbors = [4,1,2,8]
    location5.neighbors = [5,6,8]
    location6.neighbors = [6,3,5,7]
    location7.neighbors = [7,6,8]
    location8.neighbors = [8,2,4,5,7]
    location9.neighbors = [9,0,2,3]

if round == 2:
    location0.neighbors = [2,3,9]
    location1.neighbors = [2,4]
    location2.neighbors = [0,1,8]
    location3.neighbors = [0,6,9]
    location4.neighbors = [1,8]
    location5.neighbors = [6,7,8]
    location6.neighbors = [3,5,9]
    location7.neighbors = [5,8]
    location8.neighbors = [2,4,5,7]
    location9.neighbors = [0,3,6]

if round == 3:
    location0.neighbors = [1,2,9]
    location1.neighbors = [0,2,5]
    location2.neighbors = [0,1,3,4]
    location3.neighbors = [2,6,8,9]
    location4.neighbors = [2,5,8]
    location5.neighbors = [1,4]
    location6.neighbors = [3,7,8]
    location7.neighbors = [6,9]
    location8.neighbors = [3,4,6]
    location9.neighbors = [0,3,7]
alive_locations = [location0,location1,location2,location3,location4,location5,location6,location7,location8,location9]

player_locations = {0:location0, 1:location1, 2:location2, 3:location3, 4:location4, 5:location5, 6:location6, 7:location7, 8:location8, 9:location9}

def next_round(alive_locations, game_status, player1, player2):
    if len(alive_locations) == 1 :
        end_game("tie", game_status)
    else:
        to_die = random.randint(0,len(alive_locations)-1)
        kill(to_die, alive_locations)
        if player1 == player2 == to_die:
            result = "tie"
            end_game(result, game_status)
        elif player1 == to_die:
            lose(player1)
            result = "Player1 loss"
            end_game(result, game_status)
        elif player2== to_die:
            lose(player2)
            result = "Player1 loss"
            end_game(result, game_status)
    player1_neighbors = []
    for neighbor in player_locations[player1].neighbors:
        player1_neighbors.append(str(neighbor))
    current_neighbors1 = player_locations[player1].neighbors
    print(f"Player 1, you are currently at {player_locations[player1].name}. You can move to Icebergs {player1_neighbors}")
    player1 = int(input("Enter your new location: "))
    while player1 not in current_neighbors1:
        print("Not an avaiable iceberg!")
        player1 = input("Player 1: enter one of your possible moves (as an int 0-9) : ")
    
    player2_neighbors = []
    for neighbor in player_locations[player2].neighbors:
        player2_neighbors.append(str(neighbor))
    current_neighbors2 = player_locations[player2].neighbors
    print(f"Player 2, you are currently at {player_locations[player2].name}. You can move to Icebergs {player2_neighbors}")
    player2 = int(input("Enter your new location: "))
    while player2 not in current_neighbors2:
        print("Not an avaiable iceberg!")
        player2 = input("Player 2: enter one of your possible moves (as an int 0-9) : ")
    while game_status == True:
        next_round(alive_locations, game_status, player1, player2)


    
    


def lose(player):
    pass

def tie():
    pass


def kill(index, alive_locations):
    victim = alive_locations[index]
    print(victim.name+" has melted!")
    victim.aliveness = False
    alive_locations.remove(victim)
    for neighbor in victim.neighbors: # to remove victim as a neighbor for each
        alive_locations
        player_locations[neighbor].neighbors.remove(victim)

    return alive_locations

def end_game(result, game_status):
    if result == "tie":
        label = Label(root,text="Game Over: Tie Game!",
                font=('Arial',40,'bold'),  # (font,size,style)
                fg="pink",  # fg stands for foreground
                bg="brown", # bg stands for background
                relief=RAISED, # border
                bd=10, # border width
                padx=20) # pads space between text and border. also can do pady
        label.pack()
    elif result == "Player1 loss":
        label = Label(root,text="Game Over: Player 2 Wins!",
                font=('Arial',25,'bold'),  # (font,size,style)
                fg="pink",  # fg stands for foreground
                bg="brown", # bg stands for background
                relief=RAISED, # border
                bd=10, # border width
                padx=20) # pads space between text and border. also can do pady
        label.pack()
    elif result == "Player2 loss":
        label = Label(root,text="Game Over: Player 1 Wins!",
                font=('Arial',25,'bold'),  # (font,size,style)
                fg="pink",  # fg stands for foreground
                bg="brown", # bg stands for background
                relief=RAISED, # border
                bd=10, # border width
                padx=20) # pads space between text and border. also can do pady
        label.pack()
    root.mainloop()
    game_status = False

root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)

# window = Tk()
x = IntVar()

buttons = []

# def open_map(map):
#     canvas = Canvas(root,height=500,width=500)
#     canvas.create_line(0,0,500,500,fill="blue",width=5)  # first, enter the starting coordinates for your line. then followed plainly by a comma, write the second set of coordinates for where you want your line to end
#     canvas.create_line(0,500,500,0,fill="red",width=5)
#     canvas.create_rectangle(50,50,250,250,fill="pink")  # unlike the lines, fill here actually FILLS the shape with color.
#     canvas.create_polygon(250,0,500,500,0,500,fill="purple",outline="black",width=5)   # just have each set of coordinates typed after each other separated by commas (in this example, there are 3 sets of coords)
#     points = [50,50,50,100,100,75]
#     canvas.create_polygon(points)
#     canvas.create_arc(0,0,500,500,fill="yellow",style=PIESLICE,start=180,extent=180)  # the arc is actually an entire circle, but with just a section of it visible. when you type in coordinates, it's just setting the area of space avaibale to the arc
#         #  the style could be: CHORD, ARC, or PIESLICE (idk maybe others too)
#         # the start is referring to DEGREES. kind of like a rotation around the center of the canvas. COUNTERCLOCKWISE
#         # extent is how much of the degrees you want filled. defaults at 90
#     #pokeball:
#     canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
#     canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
#     canvas.create_oval(190,190,310,310,fill="white",width=10)

#     canvas.pack()
#     root.mainloop()

# program running below
round = 0
def order():
    if(x.get()=="Grid 1"):
        round = 1
    elif(x.get()==1):
        round = 2
    elif(x.get()==2):
        round = 3
        

while game_status ==True:
    next_round(alive_locations, game_status, player1, player2)

# def open_map(map):
#     canvas = Canvas(root,height=500,width=500)
#     canvas.create_line(0,0,500,500,fill="blue",width=5)  # first, enter the starting coordinates for your line. then followed plainly by a comma, write the second set of coordinates for where you want your line to end
#     canvas.create_line(0,500,500,0,fill="red",width=5)
#     canvas.create_rectangle(50,50,250,250,fill="pink")  # unlike the lines, fill here actually FILLS the shape with color.
#     canvas.create_polygon(250,0,500,500,0,500,fill="purple",outline="black",width=5)   # just have each set of coordinates typed after each other separated by commas (in this example, there are 3 sets of coords)
#     points = [50,50,50,100,100,75]
#     canvas.create_polygon(points)
#     canvas.create_arc(0,0,500,500,fill="yellow",style=PIESLICE,start=180,extent=180)  # the arc is actually an entire circle, but with just a section of it visible. when you type in coordinates, it's just setting the area of space avaibale to the arc
#         #  the style could be: CHORD, ARC, or PIESLICE (idk maybe others too)
#         # the start is referring to DEGREES. kind of like a rotation around the center of the canvas. COUNTERCLOCKWISE
#         # extent is how much of the degrees you want filled. defaults at 90
#     #pokeball:s
#     canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
#     canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
#     canvas.create_oval(190,190,310,310,fill="white",width=10)

#     for button in buttons:
#         button.destroy()
#     canvas.pack()
#     root.update()

# def click():
#     # if messagebox.askretrycancel(title="retry?",message="do you want to retry?"):   # in an if/else statement because returns a TRUE OR FALSE answer
#     #     print("This game requires 2 players!")

#     for i in range(len(possible_rounds)):
#         radiobutton = Radiobutton(root,
#                               text=possible_rounds[i],  # adds text to radio buttons
#                               variable=x,  # groups radio buttons together if they share the same variable
#                               value=i,  # assigns each radio button a different value
#                               padx=15,  # adds padding on x axis
#                               pady=10,
#                               font=("Comic Sans",30),
#                               #image=foodImages[i],  # <-- IF YOU WANTED PICTURES. would need to set 3 images with pic = PhotoImage(file=) into a list together then do this
#                               indicatoron=0,
#                               width=100,
#                               command=order(),
#                               )
        
#         radiobutton.pack(anchor=W)
#         buttons.append(radiobutton)
#     root.update()
#     if round != 0:
#         open_map(round)
#         root.update()




# button = Button(root,command=click,text="Play Penguins")
# button.pack()

# window_width = 300
# window_height = 300

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# center_x = int(screen_width/2 - window_width / 2)
# center_y = int(screen_height/2 - window_height / 2)
# root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# root.mainloop()



# # window = Tk()
# # x = IntVar()
# # for i in range(len(possible_rounds)):
# #     radiobutton = Radiobutton(window,
# #                               text=possible_rounds[i],  # adds text to radio buttons
# #                               variable=x,  # groups radio buttons together if they share the same variable
# #                               value=i,  # assigns each radio button a different value
# #                               padx=15,  # adds padding on x axis
# #                               pady=10,
# #                               font=("Comic Sans",30),
# #                               #image=foodImages[i],  # <-- IF YOU WANTED PICTURES. would need to set 3 images with pic = PhotoImage(file=) into a list together then do this
# #                               indicatoron=0,
# #                               width=200,
# #                               command=order,
# #                               )
# #     radiobutton.pack(anchor=W)

# # window.mainloop()