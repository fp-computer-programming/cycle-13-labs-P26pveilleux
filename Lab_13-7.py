with open ("alma_mater.txt", "r") as file:
    lines = file.readlines()
    reversed_lines = reversed(lines)


for line in reversed_lines:
    print(line)