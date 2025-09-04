# Read the file, get a list made of each line from the file
with open("day2/day2.txt", "r") as file:
    lines = file.readlines()


safe = 0


def check_report(report: list[int]) -> bool:
    safely_increasing = False
    safely_decreasing = False
    safe_report = True

    # Iterate through each report, run through series of checks
    # Break out of inner loop and set safe_report to false, so we count safe reports only
    for i in range(len(report) - 1):
        if report[i] == report[i + 1]:
            safe_report = False
            break

        if abs(report[i] - report[i + 1]) > 3:
            safe_report = False
            break

        if report[i] > report[i + 1]:
            safely_decreasing = True

        if report[i] < report[i + 1]:
            safely_increasing = True

        if safely_increasing and safely_decreasing:
            safe_report = False
            break

    if safe_report:
        return True

    else:
        return False


# Iterate through the list, creating a report out of each line
# PROBLEM: lines is a list, but line is a string... line needs to be a list
for line in lines:
    report_strings = line.split()
    report = list(map(int, report_strings))
    removed_element = 0

    if check_report(report):
        safe = safe + 1

    else:
        for i in range(len(report)):
            removed_element = report[i]
            del report[i]

            if check_report(report):
                safe = safe + 1
                break

            report.insert(i, removed_element)


print(safe)
