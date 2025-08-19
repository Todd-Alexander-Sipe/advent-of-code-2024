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


# 8 functions for checking each direction, first checking for in bounds
# Then checking for M, A, and S in the direction chosen
def check_east(lat, lon):
    if lat <= puzzle_width - 4:
        if puzzle[lat + 1][lon] == "M":
            if puzzle[lat + 2][lon] == "A":
                if puzzle[lat + 3][lon] == "S":
                    return True
    return False


def check_west(lat, lon):
    if lat >= 3:
        if puzzle[lat - 1][lon] == "M":
            if puzzle[lat - 2][lon] == "A":
                if puzzle[lat - 3][lon] == "S":
                    return True
    return False


def check_north(lat, lon):
    if lon >= 3:
        if puzzle[lat][lon - 1] == "M":
            if puzzle[lat][lon - 2] == "A":
                if puzzle[lat][lon - 3] == "S":
                    return True
    return False


def check_south(lat, lon):
    if lon <= puzzle_height - 4:
        if puzzle[lat][lon + 1] == "M":
            if puzzle[lat][lon + 2] == "A":
                if puzzle[lat][lon + 3] == "S":
                    return True
    return False


def check_northwest(lat, lon):
    if lon >= 3 and lat >= 3:
        if puzzle[lat - 1][lon - 1] == "M":
            if puzzle[lat - 2][lon - 2] == "A":
                if puzzle[lat - 3][lon - 3] == "S":
                    return True
    return False


def check_northeast(lat, lon):
    if lon >= 3 and lat <= puzzle_width - 4:
        if puzzle[lat + 1][lon - 1] == "M":
            if puzzle[lat + 2][lon - 2] == "A":
                if puzzle[lat + 3][lon - 3] == "S":
                    return True
    return False


def check_southwest(lat, lon):
    if lon <= puzzle_height - 4 and lat >= 3:
        if puzzle[lat - 1][lon + 1] == "M":
            if puzzle[lat - 2][lon + 2] == "A":
                if puzzle[lat - 3][lon + 3] == "S":
                    return True
    return False


def check_southeast(lat, lon):
    if lon <= puzzle_height - 4 and lat <= puzzle_width - 4:
        if puzzle[lat + 1][lon + 1] == "M":
            if puzzle[lat + 2][lon + 2] == "A":
                if puzzle[lat + 3][lon + 3] == "S":
                    return True
    return False


# Iterate through the puzzle, check for an X, and then check each direction
for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] == "X":
            if check_east(i, j):
                real_count += 1
            if check_west(i, j):
                real_count += 1
            if check_north(i, j):
                real_count += 1
            if check_south(i, j):
                real_count += 1
            if check_northwest(i, j):
                real_count += 1
            if check_northeast(i, j):
                real_count += 1
            if check_southwest(i, j):
                real_count += 1
            if check_southeast(i, j):
                real_count += 1


print(real_count)
