# Read the file, get a list made of each line from the file
with open("day5/day5.txt", "r") as file:
    lines = file.readlines()


rules = []
updates = []
incorrect_updates = []
corrected_middle_sums = 0


# Split the input into rules and updates
def split_input() -> None:
    for line in lines:
        if "|" in line:
            pair = line.strip().split("|")
            rules.append(pair)
        if "," in line:
            updates.append(line.strip().split(","))


# Function to run through all rules for a given update list, and populate the list of incorrect updates
def gather_incorrect_updates(update: str) -> None:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                incorrect_updates.append(update)
                break


# Recursive function to fix order of lists, recursing down to the base case of a properly ordered list,
# returning the middle value of that list... explaining line for line for myself in the future
def make_correction(update: str) -> int:
    # Check all rules
    for rule in rules:
        # Check if rule should apply to list
        if rule[0] in update and rule[1] in update:
            # Set indexes for making the swap line easier to read
            index_1 = update.index(rule[0])
            index_2 = update.index(rule[1])
            # Swap the two numbers that flagged the rule
            if index_1 > index_2:
                update[index_1], update[index_2] = update[index_2], update[index_1]
                # Need to return the function call to properly recurse down to the base case:
                # (an ordered list according to the rules)
                return make_correction(update)
    # Return the middle value of the correctly sorted list
    return get_middle(update)


# Function to return the middle index of the list using floor division assuming all updates are odd
def get_middle(update: str) -> int:
    return update[len(update) // 2]


# Split the inputs
split_input()
# Gather incorrect updates
for update in updates:
    gather_incorrect_updates(update)
# Make corrections to the incorrect updates, calling each incorrect update recursively until correct
for update in incorrect_updates:
    corrected_middle_sums += int(make_correction(update))
print(corrected_middle_sums)
