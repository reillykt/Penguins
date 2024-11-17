import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import time

dead_icebergs = []

player1 = 0
player2 = 0
# asking players where they want to start the game

game_status = True
round = 1
possible_rounds=["Grid 1","Grid 2","Grid 3"]

class Location:
    def __init__(self, neighbors, aliveness, name, number):
        self.neighbors = neighbors  # instance variable
        self.aliveness = aliveness  # instance variable
        self.name = name
        self.number = number
    
locations = []
locations_dict = {}
for i in range(10):  # Adjust the range to however many locations you need
    location = Location(i, True, f"Iceberg {i}", i)
    locations.append(location)
    locations_dict[i] = location


# location0 = Location([], True, "Iceberg 0")
# location1 = Location([], True, "Iceberg 1")
# # if statement connecting which round edges they select and what the neighbors are
# location2 = Location([], True, "Iceberg 2")
# location3 = Location([], True, "Iceberg 3")
# location4 = Location([], True, "Iceberg 4")
# location5 = Location([], True, "Iceberg 5")
# location6 = Location([], True, "Iceberg 6")
# location7 = Location([], True, "Iceberg 7")
# location8 = Location([], True, "Iceberg 8")
# location9 = Location([], True, "Iceberg 9")

#dictionary storing 3 maps
neighbors_by_map = {
    1: [[1, 3, 9],
        [0, 4],
        [3, 4, 9],
        [0, 2, 6, 9],
        [1, 2, 8],
        [6, 8],
        [3, 5, 7],
        [6, 8],
        [2, 4, 5, 7],
        [0, 2, 3]],

    2: [[2, 3, 9],
        [2, 4],
        [0, 1, 8],
        [0, 6, 9],
        [1, 8],
        [6, 7, 8],
        [3, 5, 9],
        [5, 8],
        [2, 4, 5, 7],
        [0, 3, 6]],

    3: [[1, 2, 9],
        [0, 2, 5],
        [0, 1, 3, 4],
        [2, 6, 8, 9],
        [2, 5, 8],
        [1, 4],
        [3, 7, 8],
        [6, 9],
        [3, 4, 6],
        [0, 3, 7]]
}
grid1dict = {0:[0,1, 3, 9], 1:[0, 1, 4], 2:[2, 3, 4, 9], 3: [0, 2, 3, 6, 9], 4: [1, 2, 4, 8], 5:[5,6, 8], 6: [3, 5,6, 7], 7:[6,7, 8], 8:[2, 4, 5, 7,8], 9:[0, 2, 3,9] }

def set_neighbors(round_num):
    for location in locations:
        location.neighbors = grid1dict[location.number]
        # print(f"{location.name} has the neighnbors {location.neighbors}")
    # neighbors = neighbors_by_map.get(round_num) # neighbors is a list of lists of integers
    # if neighbors:
    #     for i, neighbor_list in enumerate(neighbors): # for index (which location has those neighbors), list of neighbors
    #         for idx in neighbor_list:
    #             print(f"{locations[i].neighbors}")
                #locations[i].neighbors = locations[i].neighbors.append([locations[idx]])

set_neighbors(round)
#convert player input to the coresponding location
# def assign_location(player_input):
#     return locations[player_input]

# player1 = assign_location(player1)
# player2 = assign_location(player2)
                                      
alive_locations = [locations[0],locations[1],locations[2],locations[3],locations[4],locations[5],locations[6],locations[7],locations[8],locations[9]]

#player_locations = {0:location0, 1:location1, 2:location2, 3:location3, 4:location4, 5:location5, 6:location6, 7:location7, 8:location8, 9:location9}

def starting_positions():
    player1 = int(input("\nPlayer 1: To choose a starting location, enter a digit (0-9): "))
    while player1 not in range(10):
        print("Not a single digit!")
        player1 = int(input("Player 1: To choose a starting location, enter a digit (0-9): "))
    player2 = int(input("\nPlayer 2: To choose a starting location, enter a digit (0-9): "))
    while player2 not in range(10):
        print("Not a single digit!")
        player2 = int(input("Player 2: To choose a starting location, enter a digit (0-9): "))
    return player1, player2
player1, player2 = starting_positions()


round_number = 0
def next_round(alive_locations, game_status, player1, player2, round_number, locations_dict):
    check_endgame({"Player 1": player1, "Player 2": player2}, dead_icebergs, round_number, total_rounds = 9)
    if len(alive_locations) == 1 :
        end_status = end_game("tie", game_status)
        return "Game Over"
    else:
        round_number += 1
        to_die = random.randint(0,len(alive_locations)-1)
        to_compare = alive_locations[to_die].number
        print(f"{player1}")
        print(f"{locations_dict[player1]}")
        print(f"{locations_dict[player1].neighbors}")
        alive_locations, locations_dict = kill(to_die, alive_locations)
        print(f"{locations_dict[player1].neighbors}")
        print(f"Current Standings: Sunken icebergs: {dead_icebergs},    Player 1 on iceberg: {player1},    and Player 2 on iceberg: {player2}\n")
        if player1 == player2 == to_compare:
            result = "tie_loss"
            end_status = end_game(result, game_status)
            return "Game Over"
        elif player1 == to_compare:
            lose(player1)
            result = "Player1 loss"
            end_status = end_game(result, game_status)
            return "Game Over"
        elif player2== to_compare:
            lose(player2)
            result = "Player1 loss"
            end_status = end_game(result, game_status)
            return "Game Over"
        else:
            player1_neighbors = []
            if game_status == True:
                for neighbor in locations_dict[player1].neighbors:
                    player1_neighbors.append(str(neighbor))
                print(f"Player 1, you are currently at {locations[player1].name}. You can move to/stay at Icebergs: {player1_neighbors}")
                new_player1 = input(f"Enter your new location out of options {player1_neighbors}: ")
                while new_player1 not in player1_neighbors:
                    print("Not an available iceberg!")
                    new_player1 = input(f"Player 1, Enter your new location out of options {player1_neighbors}: ")
                player1 = new_player1
                
                player2_neighbors = []
                for neighbor in locations[player2].neighbors:
                    player2_neighbors.append(str(neighbor))
                print(f"\nPlayer 2, you are currently at {locations[player2].name}. You can move to/stay at Icebergs: {player2_neighbors}")
                new_player2 = input(f"Enter your new location out of options {player2_neighbors}: ")
                while new_player2 not in player2_neighbors:
                    print("Not an available iceberg!")
                    new_player2 = input(f"Player 2, Enter your new location out of options {player2_neighbors}: ")
                player2 = int(new_player2)
                while game_status == True:
                    next_round(alive_locations, game_status, player1, player2, round_number, locations_dict)


    
    


def lose(player):
    pass

def tie():
    pass


import tkinter as tk
from tkinter import messagebox
import random

class IcebergGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Iceberg Survival Game")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        self.locations = []
        self.dead_icebergs = []
        self.alive_locations = []
        self.player_positions = {"Player 1": 0, "Player 2": 0}
        self.round_number = 0
        self.game_status = True

        # Initialize icebergs
        for i in range(10):
            location = {"number": i, "aliveness": True, "neighbors": [], "name": f"Iceberg {i}"}
            self.locations.append(location)
            self.alive_locations.append(location)

        # Neighbors for map 1
        self.grid1dict = {
            0: [1, 3, 9], 1: [0, 4], 2: [3, 4, 9], 3: [0, 2, 6, 9],
            4: [1, 2, 8], 5: [6, 8], 6: [3, 5, 7], 7: [6, 8],
            8: [2, 4, 5, 7], 9: [0, 2, 3]
        }

        self.set_neighbors()

        # GUI components
        self.canvas = tk.Canvas(root, width=600, height=500, bg="lightblue")
        self.canvas.pack()

        self.control_frame = tk.Frame(root)
        self.control_frame.pack()

        self.start_btn = tk.Button(self.control_frame, text="Start Game", command=self.start_game)
        self.start_btn.pack(side=tk.LEFT, padx=10)

        self.next_btn = tk.Button(self.control_frame, text="Next Round", state=tk.DISABLED, command=self.next_round)
        self.next_btn.pack(side=tk.LEFT, padx=10)

        self.status_label = tk.Label(self.control_frame, text="Welcome to the Iceberg Survival Game!")
        self.status_label.pack(pady=10)

        self.iceberg_positions = {}
        self.draw_icebergs()

    def set_neighbors(self):
        for location in self.locations:
            location["neighbors"] = self.grid1dict[location["number"]]

    def draw_icebergs(self):
        positions = [
            (100, 100), (200, 50), (300, 100), (400, 50),
            (100, 300), (200, 250), (300, 300), (400, 250),
            (250, 400), (300, 450)
        ]
        for idx, (x, y) in enumerate(positions):
            self.iceberg_positions[idx] = self.canvas.create_oval(
                x, y, x + 50, y + 50, fill="white", tags=f"iceberg_{idx}"
            )
            self.canvas.create_text(x + 25, y + 25, text=str(idx), tags=f"iceberg_text_{idx}")

    def start_game(self):
        self.player_positions["Player 1"] = random.choice(range(10))
        self.player_positions["Player 2"] = random.choice(range(10))
        while self.player_positions["Player 2"] == self.player_positions["Player 1"]:
            self.player_positions["Player 2"] = random.choice(range(10))

        self.update_icebergs()
        self.status_label.config(text="Game Started! Players have chosen starting positions.")
        self.start_btn.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL)

    def update_icebergs(self):
        for location in self.locations:
            idx = location["number"]
            fill_color = "white"
            if idx == self.player_positions["Player 1"]:
                fill_color = "red"
            elif idx == self.player_positions["Player 2"]:
                fill_color = "blue"
            elif idx in self.dead_icebergs:
                fill_color = "gray"

            self.canvas.itemconfig(self.iceberg_positions[idx], fill=fill_color)

    def next_round(self):
        if not self.alive_locations:
            self.end_game("tie")
            return

        self.round_number += 1
        to_die = random.choice(self.alive_locations)
        self.dead_icebergs.append(to_die["number"])
        self.alive_locations.remove(to_die)

        for neighbor in to_die["neighbors"]:
            self.locations[neighbor]["neighbors"] = [
                n for n in self.locations[neighbor]["neighbors"] if n != to_die["number"]
            ]

        self.update_icebergs()

        if self.player_positions["Player 1"] in self.dead_icebergs:
            self.end_game("Player 2 wins")
        elif self.player_positions["Player 2"] in self.dead_icebergs:
            self.end_game("Player 1 wins")
        elif not self.alive_locations:
            self.end_game("tie")

    def end_game(self, result):
        self.status_label.config(text=f"Game Over: {result}")
        self.next_btn.config(state=tk.DISABLED)
        messagebox.showinfo("Game Over", f"{result}")


# Run the game
root = tk.Tk()
game = IcebergGame(root)
root.mainloop()


def kill(index, alive_locations):
    victim = alive_locations[index] #Location object
    print(f"current dead iceburgs: {dead_icebergs}")
    dead_icebergs.append(victim.number)
    time.sleep(1)
    print("\n")
    print(victim.name+" has melted!\n")
    time.sleep(1)
    victim.aliveness = False
    alive_locations.remove(victim)
    for neighbor in victim.neighbors: # all of victim's neighbors
        # print(f"near sunk iceberg: iceberg {neighbor}")
        # print(f"^'s current neighbors{locations_dict[neighbor].neighbors}")
        updated_neighbors = []
        for neigh in locations_dict[neighbor].neighbors:
            if neigh != victim.number:
                updated_neighbors.append(neigh)
        locations_dict[neighbor].neighbors = updated_neighbors
        # print(f"^'s new neighbors: {locations_dict[neighbor].neighbors}")
    return alive_locations, locations_dict

def end_game(result, game_status):
    if result == "tie_loss":
        print("You both died! Tie Game!")
        game_status = False
    elif result == "tie":
        print("You both win! Tie Game!")
        game_status = False
    elif result == "Player1 loss":
        print("Player 1's iceberg sank! Player 2 wins!")
        game_status = False
    elif result == "Player2 loss":
        print("Player 2's iceberg sank! Player 1 wins!")
        game_status = False
    return game_status


player_positions = {"Player 1": player1, "Player 2": player2}

def check_endgame(player_positions, dead_icebergs, round_number, total_rounds=9):
    """
    Determines if the game should end and who the winner is.
    
    Args:
        player_positions (dict): Current positions of the players {player1: loc1, player2: loc2}.
        dead_icebergs (list): List of "dead" icebergs.
        round_number (int): Current round number.
        total_rounds (int): Total number of rounds (default 9).
    
    Returns:
        str: The outcome of the game (winner, loser, or tie).
    """
    player1, player2 = player_positions.keys()
    position1, position2 = player_positions[player1], player_positions[player2]
    
    # Check if either player is on a dead iceberg
    if position1 in dead_icebergs and position2 in dead_icebergs:
        return "Both players lost (tie) - both were on dead icebergs."
    elif position1 in dead_icebergs:
        return f"{player2} wins! {player1} was on a dead iceberg."
    elif position2 in dead_icebergs:
        return f"{player1} wins! {player2} was on a dead iceberg."
    
    # Check if either player has no valid moves
    # player1_moves = [loc for loc in graph[position1] if loc not in dead_icebergs]
    # player2_moves = [loc for loc in graph[position2] if loc not in dead_icebergs]
    
    # if not player1_moves and not player2_moves:
    #     return "Both players are stuck (tie)."
    # elif not player1_moves:
    #     return f"{player2} wins! {player1} has no valid moves."
    # elif not player2_moves:
    #     return f"{player1} wins! {player2} has no valid moves."
    
    # Check if it's the final round
    if round_number == total_rounds:
        return "Game ends in a tie - both players survived all rounds!"
    
    # If none of the above, the game continues
    return "\nBoth Players survive: Game continues."

# Example usage

result = check_endgame(player_positions, dead_icebergs, round_number)
print(result)


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
        


next_round(alive_locations, game_status, player1, player2, round_number, locations_dict)
# result = check_endgame(player_positions, dead_icebergs, round_number)
# print(result)

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