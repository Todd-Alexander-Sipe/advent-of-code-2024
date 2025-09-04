# Read the file, get a list made of each line from the file
with open("day7/day7.txt", "r") as file:
    lines = file.readlines()


# Store all numbers from each line in a list of lists
# Make sure to trim ":"
inputs = []


# Store all equations that have a solution that works into a list
good_equations = []


# Clean up the input
for line in lines:
    inputs.append(line.replace(":", "").split())


# Function that takes three inputs:
#   number_of_operators => This should be the number of operators that exist for a given set: [3, 4, 5]
#                          which will always be the length of the set - 1, in the example above that is 2
#   operator_index =>      This is going to be 2 to the power of the number of operators so index can be correct for loop
#   problem_answer =>      This is the number that the end product should be equal to
#   operands =>            This is the list of operands
#
# The function breaks out the appropriate information and equates the number of iterations needed
#   for an equation to be tested to a binary number where each "0" represents addition: "+",
#   and each "1" represents multiplication: "*"
def check_a_problem(
    number_of_operators: int,
    operator_index: int,
    problem_answer: int,
    operands: list[str],
) -> None:
    for i in range(operator_index):
        operators = ""
        problem = []
        current_binary_number = bin(i)[2:].zfill(number_of_operators)
        for char in current_binary_number:
            if char == "0":
                operators += "+"
            if char == "1":
                operators += "*"
        for j in range(len(operators)):
            problem.append(operands[j])
            problem.append(operators[j])
        problem.append(operands[-1])
        while len(problem) > 1:
            product_or_sum = 0
            left_side = int(problem[0])
            operator = problem[1]
            right_side = int(problem[2])
            del problem[:3]
            if operator == "+":
                product_or_sum = str(left_side + right_side)
            if operator == "*":
                product_or_sum = str(left_side * right_side)
            problem.insert(0, product_or_sum)
        if int(problem[0]) == problem_answer:
            good_equations.append(problem_answer)
            break


# Iterate through each equation to check if the equation has a viable answer
for input in inputs:
    problem_answer = int(input[0])
    del input[:1]
    number_of_operators = len(input) - 1
    operator_index = 2 ** (number_of_operators)
    check_a_problem(number_of_operators, operator_index, problem_answer, input)


print(sum(good_equations))
