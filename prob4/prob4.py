# Read the file, get a list made of each line from the file
with open("prob3\prob3.txt", "r") as file:
    lines = file.readlines()

safe = 0

def check_report(line):
    safely_increasing = False
    safely_decreasing = False
    safe_report = True
    report_strings = line.split()
    report = list(map(int, report_strings))
    
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
for line in lines:
    if check_report(line):
        safe = safe + 1

print(safe)
