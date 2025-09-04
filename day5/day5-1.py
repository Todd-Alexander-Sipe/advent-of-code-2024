# Read the file, get a list made of each line from the file
with open("day5/day5.txt", "r") as file:
    lines = file.readlines()


rules = []
updates = []
middle_sums = 0


# Split the input into rules and updates
def split_input() -> None:
    for line in lines:
        if "|" in line:
            pair = line.strip().split("|")
            rules.append(pair)
        if "," in line:
            updates.append(line.strip().split(","))


# Function to run through all rules for a given update list
def check_update(update: str) -> bool:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True


# Function to return the middle index of the list using floor division assuming all updates are odd
def get_middle(update: str) -> int:
    return update[len(update) // 2]


# Split the inputs, iterate through each update to get the middle value of each good update, and print the sum
split_input()
for update in updates:
    if check_update(update):
        middle_sums += int(get_middle(update))
print(middle_sums)
