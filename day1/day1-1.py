# Read the file, get a list made of each line from the file
with open("day1/day1.txt", "r") as file:
    lines = file.readlines()


# Create a left list, a right list, and a diffs list
left = []
right = []
diffs = []


# Split each line and append left entry to left[] and right entry to right[], eliminating white space and newlines
for line in lines:
    two_numbers = line.split()
    left.append(int(two_numbers[0]))
    right.append(int(two_numbers[1]))


# Sort each list
left.sort()
right.sort()


# Append the differences (absolute values) of each pair to diffs[]
for i in range(len(left)):
    diffs.append(abs(left[i] - right[i]))


solution = 0


# Add up the diffs in diffs
for diff in diffs:
    solution += diff
print(solution)
