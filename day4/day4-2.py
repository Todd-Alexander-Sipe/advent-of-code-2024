# Walking away from this, I am left wishing I had broken these down into simpler functions:
#   check_left(), check_upleft(), etc
# I am also left feeling as if I should have done in bounds checking for the first
#   problem as I did for the second


# Read the file, get a list made of each line from the file
with open("day4/day4.txt", "r") as file:
    lines = file.readlines()


# Create what will become a list of lists of the characters for the puzzle
puzzle = []


# Puzzle has a '\n' character at the end of each line, thus the - 1
puzzle_width = len(lines[0]) - 1
puzzle_height = len(lines)


# Iterate through the lines of the input to create a list of only X, M, A, and S characters (no \n characters)
for line in lines:
    puzzle_line = []
    for i in range(len(line)):
        if line[i] != "\n":
            puzzle_line.append(line[i])
    puzzle.append(puzzle_line)


real_count = 0


# Ensure what we are checking is in bounds
def check_in_bounds(lat: int, lon: int) -> bool:
    if lat == 0 or lat == puzzle_height - 1 or lon == 0 or lon == puzzle_width - 1:
        return False
    else:
        return True


# 4 different functions that check the positions of the four different X style arrangements
# all according to the M positions:
# Left: M S  Top: M M  Right: S M  Bottom: S S
#        A         A           A            A
#       M S       S S         S M          M M
def check_left(lat: int, lon: int) -> bool:
    if puzzle[lat - 1][lon - 1] == "M":
        if puzzle[lat - 1][lon + 1] == "M":
            if puzzle[lat + 1][lon - 1] == "S":
                if puzzle[lat + 1][lon + 1] == "S":
                    return True
    return False


def check_top(lat: int, lon: int) -> bool:
    if puzzle[lat - 1][lon - 1] == "M":
        if puzzle[lat - 1][lon + 1] == "S":
            if puzzle[lat + 1][lon - 1] == "M":
                if puzzle[lat + 1][lon + 1] == "S":
                    return True
    return False


def check_right(lat: int, lon: int) -> bool:
    if puzzle[lat - 1][lon - 1] == "S":
        if puzzle[lat - 1][lon + 1] == "S":
            if puzzle[lat + 1][lon - 1] == "M":
                if puzzle[lat + 1][lon + 1] == "M":
                    return True
    return False


def check_bottom(lat: int, lon: int) -> bool:
    if puzzle[lat - 1][lon - 1] == "S":
        if puzzle[lat - 1][lon + 1] == "M":
            if puzzle[lat + 1][lon - 1] == "S":
                if puzzle[lat + 1][lon + 1] == "M":
                    return True
    return False


# Iterate through the puzzle, check for an A, and then check each potential X formation
for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] == "A":
            if check_in_bounds(i, j):
                if check_left(i, j):
                    real_count += 1
                if check_top(i, j):
                    real_count += 1
                if check_right(i, j):
                    real_count += 1
                if check_bottom(i, j):
                    real_count += 1


print(real_count)
