# Read the file, get a list made of each line from the file
with open("day6/day6.txt", "r") as file:
    lines = file.readlines()


# Hold information in containers
puzzle = []
current_position = {
    "lat": 0,
    "lon": 0,
}
starting_position = {
    "lat": 0,
    "lon": 0,
    "facing": "",
}
obstacle_record = []
state = {
    "donezo": False,
    "go_north": False,
    "go_east": False,
    "go_south": False,
    "go_west": False,
}
# 16900 different puzzles (minus one, because of the guard's starting location)
finished_puzzles = {
    "finished": 0,
    "loop_found": 0,
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


# Find the starting position for the puzzle
for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] == "^":
            state["go_north"] = True
            starting_position["lat"] = i
            starting_position["lon"] = j
            starting_position["facing"] = "N"
        if puzzle[i][j] == ">":
            state["go_east"] = True
            starting_position["lat"] = i
            starting_position["lon"] = j
            starting_position["facing"] = "E"
        if puzzle[i][j] == "v":
            state["go_south"] = True
            starting_position["lat"] = i
            starting_position["lon"] = j
            starting_position["facing"] = "S"
        if puzzle[i][j] == "<":
            state["go_west"] = True
            starting_position["lat"] = i
            starting_position["lon"] = j
            starting_position["facing"] = "W"
print(
    "Starting pos: "
    + str(starting_position["lat"])
    + ", "
    + str(starting_position["lon"])
)


# Directional functions
# If we run into a barrier, turn 90 degrees to the right, etc
# Append all found obstacles and the direction the guard is facing to a list
# If that obstacle has been approached at that spot from the direction before, we are in a loop
def travel_north(lat: int, lon: int) -> bool:
    if lat != 0:
        if puzzle[lat - 1][lon] == "#":
            state["go_north"] = False
            state["go_east"] = True
            thing = ("N", lat, lon)
            if thing in obstacle_record:
                return False
            obstacle_record.append(thing)
        else:
            current_position["lat"] = lat - 1
    else:
        state["donezo"] = True
    return True


def travel_east(lat: int, lon: int) -> bool:
    if lon != puzzle_width - 1:
        if puzzle[lat][lon + 1] == "#":
            state["go_east"] = False
            state["go_south"] = True
            thing = ("E", lat, lon)
            if thing in obstacle_record:
                return False
            obstacle_record.append(thing)
        else:
            current_position["lon"] = lon + 1
    else:
        state["donezo"] = True
    return True


def travel_south(lat: int, lon: int) -> bool:
    if lat != puzzle_height - 1:
        if puzzle[lat + 1][lon] == "#":
            state["go_south"] = False
            state["go_west"] = True
            thing = ("S", lat, lon)
            if thing in obstacle_record:
                return False
            obstacle_record.append(thing)
        else:
            current_position["lat"] = lat + 1
    else:
        state["donezo"] = True
    return True


def travel_west(lat: int, lon: int) -> bool:
    if lon != 0:
        if puzzle[lat][lon - 1] == "#":
            state["go_west"] = False
            state["go_north"] = True
            thing = ("W", lat, lon)
            if thing in obstacle_record:
                return False
            obstacle_record.append(thing)
        else:
            current_position["lon"] = lon - 1
    else:
        state["donezo"] = True
    return True


# Run the patrol until the edge of the map is exited
# Carefully reset the starting state of puzzle
# Tally loop discoveries and non-loop puzzles
def run_puzzle() -> None:
    obstacle_record.clear()
    current_position["lat"] = starting_position["lat"]
    current_position["lon"] = starting_position["lon"]
    state["donezo"] = False
    state["go_north"] = False
    state["go_east"] = False
    state["go_south"] = False
    state["go_west"] = False
    if starting_position["facing"] == "N":
        state["go_north"] = True
    if starting_position["facing"] == "E":
        state["go_east"] = True
    if starting_position["facing"] == "S":
        state["go_south"] = True
    if starting_position["facing"] == "W":
        state["go_west"] = True
    while not state["donezo"]:
        if state["go_north"]:
            if not travel_north(current_position["lat"], current_position["lon"]):
                finished_puzzles["loop_found"] += 1
                return
        if state["go_east"]:
            if not travel_east(current_position["lat"], current_position["lon"]):
                finished_puzzles["loop_found"] += 1
                return
        if state["go_south"]:
            if not travel_south(current_position["lat"], current_position["lon"]):
                finished_puzzles["loop_found"] += 1
                return
        if state["go_west"]:
            if not travel_west(current_position["lat"], current_position["lon"]):
                finished_puzzles["loop_found"] += 1
                return
    finished_puzzles["finished"] += 1


# Iterate through the entire puzzle and replace each location with an obstacle, except for the guard's start location
# Run the puzzle to check for loops, restore the puzzle, and continue iterating
for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if (i, j) != (53, 91):
            temp = puzzle[i][j]
            puzzle[i][j] = "#"
            run_puzzle()
            puzzle[i][j] = temp


print(finished_puzzles)
