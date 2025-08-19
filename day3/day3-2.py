import re

# Read the file, get a list made of each line from the file
with open("day3/day3.txt", "r") as file:
    lines = file.readlines()


# List to store all legal commands
# Specifically: mul(###,###), do(), and don't()
commands = []


# List to store good values to add
mull = []


# Regex pattern to find viable "mul(###,###)" matches (up to three digits for each multiple),
# do(), or don't() patterns
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"


# Function to return product of two numbers from a string that looks like "mul(###,###)"
def mul_it(input):
    cleaned_input = input.replace("mul(", "").replace(")", "")
    pair = cleaned_input.split(",")
    first = int(pair[0])
    second = int(pair[1])
    return first * second


# Iterate through lines, find all regex matches, iterate through sublist of matches to call function
for line in lines:
    matches = re.findall(pattern, line)
    for element in matches:
        commands.append(element)


# Boolean to control whether or not we add a value
machine_on = True


# Iterate through list turning machine on or off based on commands, and add good numbers to the good list
for i in range(len(commands)):
    if commands[i] == "do()":
        machine_on = True

    if commands[i] == "don't()":
        machine_on = False

    if commands[i] != "do()" and commands[i] != "don't()":
        if machine_on:
            mull.append(mul_it(commands[i]))


print(sum(mull))
