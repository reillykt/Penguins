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