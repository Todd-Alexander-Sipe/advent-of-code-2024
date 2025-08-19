# Read the file, get a list made of each line from the file
with open("day5/day5.txt", "r") as file:
    lines = file.readlines()


rules = []
updates = []
page_order = []
rules_in_order = []
rules_dict = {}


# Split the input into rules and updates
def split_input():
    for line in lines:
        if "|" in line:
            pair = line.strip().split("|")
            rules.append(pair)
        if "," in line:
            updates.append(line.strip().split(","))


# Function to gather all unique values found in the rules list
def unique_values():
    for rule in rules:
        if rule[0] not in page_order:
            page_order.append(rule[0])
        if rule[1] not in page_order:
            page_order.append(rule[1])


def create_dict():
    for rule in rules:
        rules_dict[rule[1]] = []
    for rule in rules:
        rules_dict[rule[1]].append(rule[0])


split_input()
unique_values()
create_dict()
print(rules_dict)
# print(updates)


# rules.sort(key=lambda x: x[1])
# print(rules)


# Gather all unique values found in the rules list
# for rule in rules:
#     unique_values(rule)


# Function to apply the ruleset and properly order the page_order list
# NOT FUNCTIONING PROPERLY
# def order_pages(line):
#     # Split input line, creating a list: pair
#     pair = line.split("|")
#     first = pair[0]
#     second = pair[1]
#     print("rule: " + first + " should be placed before " + second)
#     if page_order.index(first) > page_order.index(second):
#         print(
#             "moving "
#             + first
#             + " from index: "
#             + str(page_order.index(first))
#             + " to index "
#             + str(page_order.index(second))
#         )
#         page_order.remove(first)
#         page_order.insert(page_order.index(second), first)


# print(page_order)


# for rule in rules:
#     order_pages(rule)


# print(page_order)
