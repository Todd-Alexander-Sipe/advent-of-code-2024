# Read the file, get a list made of each line from the file
with open("day6/day6.txt", "r") as file:
    lines = file.readlines()


# Hold information in containers
puzzle = []
position = {
    "lat": 0,
    "lon": 0,
}
state = {
    "donezo": False,
    "go_north": False,
    "go_east": False,
    "go_south": False,
    "go_west": False,
}


# Create list of lists for the puzzle characters, excluding \n
for line in lines:
    puzzle_line = []
    for i in range(len(line)):
        if line[i] != "\n":
            puzzle_line.append(line[i])
    puzzle.append(puzzle_line)


# Immutable puzzle size
puzzle_width = len(puzzle[0])
puzzle_height = len(puzzle)


# Function to find the start of our patrol person and store it in position dict
def find_start_location() -> None:
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == "^":
                state["go_north"] = True
                position["lat"] = i
                position["lon"] = j
            if puzzle[i][j] == ">":
                state["go_east"] = True
                position["lat"] = i
                position["lon"] = j
            if puzzle[i][j] == "v":
                state["go_south"] = True
                position["lat"] = i
                position["lon"] = j
            if puzzle[i][j] == "<":
                state["go_west"] = True
                position["lat"] = i
                position["lon"] = j
    print("Starting pos: " + str(position["lat"]) + ", " + str(position["lon"]))


# Directional functions
# Change the spot to X to mark we've been there
# If we find an obstacle, turn 90 degrees to the right and continue
def travel_north(lat: int, lon: int) -> None:
    puzzle[lat][lon] = "X"
    if lat != 0:
        if puzzle[lat - 1][lon] == "#":
            puzzle[lat][lon] == ">"
            state["go_north"] = False
            state["go_east"] = True
        else:
            puzzle[lat - 1][lon] = "^"
            position["lat"] = lat - 1
    else:
        state["donezo"] = True


def travel_east(lat: int, lon: int) -> None:
    puzzle[lat][lon] = "X"
    if lon != puzzle_width - 1:
        if puzzle[lat][lon + 1] == "#":
            puzzle[lat][lon] == "v"
            state["go_east"] = False
            state["go_south"] = True
        else:
            puzzle[lat][lon + 1] = ">"
            position["lon"] = lon + 1
    else:
        state["donezo"] = True


def travel_south(lat: int, lon: int) -> None:
    puzzle[lat][lon] = "X"
    if lat != puzzle_height - 1:
        if puzzle[lat + 1][lon] == "#":
            puzzle[lat][lon] == "<"
            state["go_south"] = False
            state["go_west"] = True
        else:
            puzzle[lat + 1][lon] = "v"
            position["lat"] = lat + 1
    else:
        state["donezo"] = True


def travel_west(lat: int, lon: int) -> None:
    puzzle[lat][lon] = "X"
    if lon != 0:
        if puzzle[lat][lon - 1] == "#":
            puzzle[lat][lon] == "^"
            state["go_west"] = False
            state["go_north"] = True
        else:
            puzzle[lat][lon - 1] = "<"
            position["lon"] = lon - 1
    else:
        state["donezo"] = True


find_start_location()


# Run the puzzle, using the state dictionary to determine what to do
while not state["donezo"]:
    if state["go_north"]:
        travel_north(position["lat"], position["lon"])
    if state["go_east"]:
        travel_east(position["lat"], position["lon"])
    if state["go_south"]:
        travel_south(position["lat"], position["lon"])
    if state["go_west"]:
        travel_west(position["lat"], position["lon"])


count_x = 0


# Count how many Xs are in the puzzle
for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] == "X":
            count_x += 1


print(count_x)
