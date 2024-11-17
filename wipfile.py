import random

class IcebergGame:
    def __init__(self):
        self.dead_icebergs = []
        self.locations = []
        self.alive_locations = []
        self.round_number = 0
        self.game_status = True

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

        # Players' initial positions
        self.player_positions = {"Player 1": None, "Player 2": None}
        self.starting_positions()

    def set_neighbors(self):
        for location in self.locations:
            location["neighbors"] = self.grid1dict[location["number"]]

    def starting_positions(self):
        player1 = int(input("Player 1: Choose your starting location (0-9): "))
        while player1 not in range(10):
            player1 = int(input("Invalid input! Player 1, choose a location (0-9): "))

        player2 = int(input("Player 2: Choose your starting location (0-9): "))
        while player2 not in range(10):
            player2 = int(input("Invalid input! Player 2, choose a location (0-9): "))

        self.player_positions["Player 1"] = player1
        self.player_positions["Player 2"] = player2
        print(f"Player 1 is on Iceberg {player1}, Player 2 is on Iceberg {player2}")

    def kill_iceberg(self):
        to_die = random.choice(self.alive_locations)
        self.alive_locations.remove(to_die)
        self.dead_icebergs.append(to_die)
        print(f"Iceberg {to_die} has melted!")

        if self.player_positions["Player 1"] == to_die and self.player_positions["Player 2"] == to_die:
            print("Both players were on the melted iceberg! It's a tie!")
            self.game_status = False
        elif self.player_positions["Player 1"] == to_die:
            print("Player 1 was on the melted iceberg! Player 2 wins!")
            self.game_status = False
        elif self.player_positions["Player 2"] == to_die:
            print("Player 2 was on the melted iceberg! Player 1 wins!")
            self.game_status = False

    def move_player(self, player):
        current_position = self.player_positions[player]
        neighbors = self.locations[current_position]["neighbors"]
        valid_moves = [n for n in neighbors if n not in self.dead_icebergs]
        print(f"{player}, you are on Iceberg {current_position}. Neighbors: {valid_moves}")

        if not valid_moves:
            print(f"{player} has no valid moves! The game ends in a tie.")
            self.game_status = False
            return

        new_position = int(input(f"{player}, choose your new location from {valid_moves}: "))
        while new_position not in valid_moves:
            new_position = int(input(f"Invalid move! {player}, choose from {valid_moves}: "))

        self.player_positions[player] = new_position

    def play_round(self):
        self.round_number += 1
        print(f"\n--- Round {self.round_number} ---")
        self.kill_iceberg()

        if not self.game_status:
            return

        self.move_player("Player 1")
        if not self.game_status:
            return

        self.move_player("Player 2")

    def start_game(self):
        print("\nStarting Iceberg Survival Game!")
        while self.game_status and len(self.alive_locations) > 1:
            self.play_round()

        print("\nGame Over!")


# Run the game
game = IcebergGame()
game.start_game()
