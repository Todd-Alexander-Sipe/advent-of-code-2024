import re

# Read the file, get a list made of each line from the file
with open("day3/day3.txt", "r") as file:
    lines = file.readlines()


# List to store all legal products
mull = []


# Regex pattern to find viable "mul(###,###)" matches (up to three digits for each multiple)
pattern = r"mul\(\d{1,3},\d{1,3}\)"


# Function to gather multiples, multiply them, and append the result to the list of legal products
def mul_it(input: str) -> None:
    cleaned_input = input.replace("mul(", "").replace(")", "")
    pair = cleaned_input.split(",")
    first = int(pair[0])
    second = int(pair[1])
    product = first * second
    mull.append(product)


# Iterate through lines, find all regex matches, iterate through sublist of matches to call function
for line in lines:
    match = re.findall(pattern, line)
    for valid_mul in match:
        mul_it(valid_mul)


print(sum(mull))
