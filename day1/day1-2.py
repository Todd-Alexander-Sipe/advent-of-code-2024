# Read the file, get a list made of each line from the file
with open("day1/day1.txt", "r") as file:
    lines = file.readlines()


# Create a left list, a right list
left = []
right = []
similarities = []


# Split each line and append left entry to left[] and right entry to right[], eliminating white space and newlines
for line in lines:
    two_numbers = line.split()
    left.append(int(two_numbers[0]))
    right.append(int(two_numbers[1]))


# Sort each list
left.sort()
right.sort()


# Iterate through left list, get multiple number from right list, get similarity value and append it to similarities
for value in left:
    multiple = right.count(value)
    similarity = value * multiple
    similarities.append(similarity)


solution = 0


# Add up similaritiess
for similarity in similarities:
    solution += similarity
print(solution)
