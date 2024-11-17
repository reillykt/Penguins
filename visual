import random
import tkinter as tk
from tkinter import messagebox

class IcebergGame:
    def __init__(self, root):
        self.root = root
        self.dead_icebergs = []
        self.locations = []
        self.alive_locations = []
        self.round_number = 0
        self.game_status = True
        self.player_positions = {"Player 1": None, "Player 2": None}

        # Initialize icebergs
        for i in range(10):
            self.locations.append({
                "number": i,
                "aliveness": True,
                "neighbors": [],
                "name": f"Iceberg {i}"
            })
            self.alive_locations.append(i)

        # Map of iceberg neighbors
        self.grid1dict = {
            0: [0, 1, 3, 9], 1: [1, 0, 4], 2: [2, 3, 4, 9], 3: [3, 0, 2, 6, 9],
            4: [4, 1, 2, 8], 5: [5, 6, 8], 6: [6, 3, 5, 7], 7: [7, 6, 8],
            8: [8, 2, 4, 5, 7], 9: [9, 0, 2, 3]
        }
        self.set_neighbors()

        # Create the GUI
        self.canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
        self.canvas.pack()

        # Create icebergs with random positions but loosely grouped
        self.iceberg_circles = {}
        self.iceberg_labels = {}
        self.iceberg_positions = {}  # Store positions for each iceberg

        # Define groups of icebergs to be placed near each other
        iceberg_groups = [
            (0, 1, 2, 3),  # Group 1
            (4, 5, 6),     # Group 2
            (7, 8, 9)      # Group 3
        ]
        
        # Create icebergs near each other in groups
        for group in iceberg_groups:
            base_x = random.randint(100, 500)  # Random x for each group
            base_y = random.randint(100, 500)  # Random y for each group
            for i in group:
                # Larger random offset for each iceberg in the group
                x_offset = random.randint(-100, 100)
                y_offset = random.randint(-100, 100)
                x = base_x + x_offset
                y = base_y + y_offset
                # Ensure icebergs don't overlap by adjusting positions
                while any(abs(x - pos[0]) < 40 and abs(y - pos[1]) < 40 for pos in self.iceberg_positions.values()):
                    x = base_x + random.randint(-100, 100)
                    y = base_y + random.randint(-100, 100)
                self.iceberg_positions[i] = (x, y)
                circle = self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white", outline="black", tag=f"iceberg_{i}")
                label = self.canvas.create_text(x, y, text=f"{i}", tag=f"label_{i}")
                self.iceberg_circles[i] = circle
                self.iceberg_labels[i] = label

        # Player labels to show their positions
        self.player_labels = {
            "Player 1": tk.Label(root, text="Player 1 Position: Not selected", font=("Arial", 12)),
            "Player 2": tk.Label(root, text="Player 2 Position: Not selected", font=("Arial", 12))
        }
        self.player_labels["Player 1"].pack(pady=10)
        self.player_labels["Player 2"].pack(pady=10)

        self.starting_positions()

    def set_neighbors(self):
        for location in self.locations:
            location["neighbors"] = self.grid1dict[location["number"]]

    def starting_positions(self):
        def set_position(player):
            position = int(position_entry.get())
            if position in range(10):
                self.player_positions[player] = position
                self.player_labels[player].config(text=f"{player} is on Iceberg {position}")
                prompt.destroy()
            else:
                messagebox.showerror("Invalid Input", "Choose a location between 0 and 9.")

        for player in ["Player 1", "Player 2"]:
            prompt = tk.Toplevel(self.root)
            prompt.title(f"{player} Starting Position")
            tk.Label(prompt, text=f"{player}, choose your starting location (0-9):").pack()
            position_entry = tk.Entry(prompt)
            position_entry.pack()
            tk.Button(prompt, text="Submit", command=lambda: set_position(player)).pack()
            prompt.wait_window()

    def kill_iceberg(self):
        to_die = random.choice(self.alive_locations)
        self.alive_locations.remove(to_die)
        self.dead_icebergs.append(to_die)

        # Shrink iceberg and remove label
        self.canvas.delete(self.iceberg_labels[to_die])
        self.canvas.itemconfig(self.iceberg_circles[to_die], fill="gray")
        messagebox.showinfo("Iceberg Melted", f"Iceberg {to_die} has melted!")

        # Check if any players were on the iceberg
        if self.player_positions["Player 1"] == to_die and self.player_positions["Player 2"] == to_die:
            messagebox.showinfo("Game Over", "Both players were on the melted iceberg! It's a tie!")
            self.game_status = False
        elif self.player_positions["Player 1"] == to_die:
            messagebox.showinfo("Game Over", "Player 1 was on the melted iceberg! Player 2 wins!")
            self.game_status = False
        elif self.player_positions["Player 2"] == to_die:
            messagebox.showinfo("Game Over", "Player 2 was on the melted iceberg! Player 1 wins!")
            self.game_status = False

    def move_player(self, player):
        current_position = self.player_positions[player]
        neighbors = self.locations[current_position]["neighbors"]
        valid_moves = [n for n in neighbors if n not in self.dead_icebergs]

        if not valid_moves:
            messagebox.showinfo("Game Over", f"{player} has no valid moves! The game ends in a tie.")
            self.game_status = False
            return

        prompt = tk.Toplevel(self.root)
        prompt.title(f"{player} Move")
        tk.Label(prompt, text=f"{player}, you are on Iceberg {current_position}. Neighbors: {valid_moves}").pack()
        position_entry = tk.Entry(prompt)
        position_entry.pack()

        def submit_move():
            new_position = int(position_entry.get())
            if new_position in valid_moves:
                self.player_positions[player] = new_position
                self.player_labels[player].config(text=f"{player} is on Iceberg {new_position}")
                prompt.destroy()
            else:
                messagebox.showerror("Invalid Move", f"Choose a location from {valid_moves}.")

        tk.Button(prompt, text="Submit", command=submit_move).pack()
        prompt.wait_window()

    def play_round(self):
        self.round_number += 1
        self.kill_iceberg()
        if not self.game_status:
            return
        self.move_player("Player 1")
        if not self.game_status:
            return
        self.move_player("Player 2")

    def start_game(self):
        while self.game_status and len(self.alive_locations) > 1:
            self.play_round()
        messagebox.showinfo("Game Over", "Game Over!")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Iceberg Survival Game")
    game = IcebergGame(root)
    game.start_game()
    root.mainloop()
