import tkinter as tk
import random

# Coordinates for icebergs
icebergs_coords = {
    1: (100, 100),
    2: (200, 50),
    3: (300, 100),
    4: (150, 200),
    5: (250, 200),
    6: (200, 300),
    7: (100, 400),
    8: (300, 400),
    9: (200, 500),
    10: (200, 600),
}

# Initialize the game board
root = tk.Tk()
root.title("Iceberg Breaking")

canvas = tk.Canvas(root, width=400, height=700, bg="skyblue")
canvas.pack()

# Draw the icebergs
icebergs = {}
for node, (x, y) in icebergs_coords.items():
    icebergs[node] = canvas.create_oval(
        x - 20, y - 20, x + 20, y + 20, fill="white", outline="black", width=2
    )

# Keep track of dead icebergs
dead_icebergs = []


def break_iceberg():
    """Randomly selects an iceberg to 'break' and updates its appearance."""
    while True:
        iceberg_to_break = random.choice(list(icebergs.keys()))
        if iceberg_to_break not in dead_icebergs:
            # Mark the iceberg as dead
            dead_icebergs.append(iceberg_to_break)

            # Change its color to gray and add a "cracked" effect
            canvas.itemconfig(icebergs[iceberg_to_break], fill="gray", outline="red")
            canvas.create_line(
                icebergs_coords[iceberg_to_break][0] - 15,
                icebergs_coords[iceberg_to_break][1] - 15,
                icebergs_coords[iceberg_to_break][0] + 15,
                icebergs_coords[iceberg_to_break][1] + 15,
                fill="red",
                width=2,
            )
            canvas.create_line(
                icebergs_coords[iceberg_to_break][0] - 15,
                icebergs_coords[iceberg_to_break][1] + 15,
                icebergs_coords[iceberg_to_break][0] + 15,
                icebergs_coords[iceberg_to_break][1] - 15,
                fill="red",
                width=2,
            )

            break


# Button to trigger iceberg breaking
break_button = tk.Button(root, text="Break Iceberg", command=break_iceberg)
break_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
