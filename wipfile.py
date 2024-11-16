import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

round = 0
possible_rounds=["Grid 1","Grid 2","Grid 3"]

class Location:
    def __init__(self, neighbors, aliveness):
        self.neighbors = neighbors  # instance variable
        self.aliveness = aliveness  # instance variable
    


#round_neighbors = # either 1, 2, n (which round of edges)

location0 = Location([], True)
location1 = Location([], True)
# if statement connecting which round edges they select and what the neighbors are
location2 = Location([], True)
location3 = Location([], True)
location4 = Location([], True)
location5 = Location([], True)
location6 = Location([], True)
location7 = Location([], True)
location8 = Location([], True)
location9 = Location([], True)

alive_locations = [location0,location1,location2,location3,location4,location5,location6,location7,location8,location9]

def next_round(alive_locations):
    length = 0
    for location in alive_locations:
        length +- 1
    to_die = random.randint(0,length)

def kill(index, alive_locations):
    victim = alive_locations[index]
    victim.aliveness = False
    alive_locations.remove(victim)
    return alive_locations



root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('Radio Button Demo')

# window = Tk()
x = IntVar()

buttons = []

def open_map(map):
    canvas = Canvas(root,height=500,width=500)
    canvas.create_line(0,0,500,500,fill="blue",width=5)  # first, enter the starting coordinates for your line. then followed plainly by a comma, write the second set of coordinates for where you want your line to end
    canvas.create_line(0,500,500,0,fill="red",width=5)
    canvas.create_rectangle(50,50,250,250,fill="pink")  # unlike the lines, fill here actually FILLS the shape with color.
    canvas.create_polygon(250,0,500,500,0,500,fill="purple",outline="black",width=5)   # just have each set of coordinates typed after each other separated by commas (in this example, there are 3 sets of coords)
    points = [50,50,50,100,100,75]
    canvas.create_polygon(points)
    canvas.create_arc(0,0,500,500,fill="yellow",style=PIESLICE,start=180,extent=180)  # the arc is actually an entire circle, but with just a section of it visible. when you type in coordinates, it's just setting the area of space avaibale to the arc
        #  the style could be: CHORD, ARC, or PIESLICE (idk maybe others too)
        # the start is referring to DEGREES. kind of like a rotation around the center of the canvas. COUNTERCLOCKWISE
        # extent is how much of the degrees you want filled. defaults at 90
    #pokeball:
    canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
    canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
    canvas.create_oval(190,190,310,310,fill="white",width=10)

    canvas.pack()
    root.mainloop()

# program running below
round = 0
def order():
    if(x.get()=="Grid 1"):
        round = 1
    elif(x.get()==1):
        round = 2
    elif(x.get()==2):
        round = 3
        



def open_map(map):
    canvas = Canvas(root,height=500,width=500)
    canvas.create_line(0,0,500,500,fill="blue",width=5)  # first, enter the starting coordinates for your line. then followed plainly by a comma, write the second set of coordinates for where you want your line to end
    canvas.create_line(0,500,500,0,fill="red",width=5)
    canvas.create_rectangle(50,50,250,250,fill="pink")  # unlike the lines, fill here actually FILLS the shape with color.
    canvas.create_polygon(250,0,500,500,0,500,fill="purple",outline="black",width=5)   # just have each set of coordinates typed after each other separated by commas (in this example, there are 3 sets of coords)
    points = [50,50,50,100,100,75]
    canvas.create_polygon(points)
    canvas.create_arc(0,0,500,500,fill="yellow",style=PIESLICE,start=180,extent=180)  # the arc is actually an entire circle, but with just a section of it visible. when you type in coordinates, it's just setting the area of space avaibale to the arc
        #  the style could be: CHORD, ARC, or PIESLICE (idk maybe others too)
        # the start is referring to DEGREES. kind of like a rotation around the center of the canvas. COUNTERCLOCKWISE
        # extent is how much of the degrees you want filled. defaults at 90
    #pokeball:s
    canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
    canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
    canvas.create_oval(190,190,310,310,fill="white",width=10)

    for button in buttons:
        button.destroy()
    canvas.pack()
    root.update()

def click():
    # if messagebox.askretrycancel(title="retry?",message="do you want to retry?"):   # in an if/else statement because returns a TRUE OR FALSE answer
    #     print("This game requires 2 players!")

    for i in range(len(possible_rounds)):
        radiobutton = Radiobutton(root,
                              text=possible_rounds[i],  # adds text to radio buttons
                              variable=x,  # groups radio buttons together if they share the same variable
                              value=i,  # assigns each radio button a different value
                              padx=15,  # adds padding on x axis
                              pady=10,
                              font=("Comic Sans",30),
                              #image=foodImages[i],  # <-- IF YOU WANTED PICTURES. would need to set 3 images with pic = PhotoImage(file=) into a list together then do this
                              indicatoron=0,
                              width=100,
                              command=order(),
                              )
        
        radiobutton.pack(anchor=W)
        buttons.append(radiobutton)
    root.update()
    if round != 0:
        open_map(round)
        root.update()




button = Button(root,command=click,text="Play Penguins")
button.pack()

root.mainloop()



# window = Tk()
# x = IntVar()
# for i in range(len(possible_rounds)):
#     radiobutton = Radiobutton(window,
#                               text=possible_rounds[i],  # adds text to radio buttons
#                               variable=x,  # groups radio buttons together if they share the same variable
#                               value=i,  # assigns each radio button a different value
#                               padx=15,  # adds padding on x axis
#                               pady=10,
#                               font=("Comic Sans",30),
#                               #image=foodImages[i],  # <-- IF YOU WANTED PICTURES. would need to set 3 images with pic = PhotoImage(file=) into a list together then do this
#                               indicatoron=0,
#                               width=200,
#                               command=order,
#                               )
#     radiobutton.pack(anchor=W)

# window.mainloop()