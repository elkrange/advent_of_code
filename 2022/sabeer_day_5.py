# WCZTHTMPS
# BLSGJSDTS
import re
stacks_part1 = []
stacks_part2 = []

for i in range(9):
    stacks_part1.append([])
for i in range(9):
    stacks_part2.append([])

with open("/home/sabeer-ss/Downloads/input-day5.txt", "r") as f:
    input_list = f.readlines()
    for idx, line in enumerate(input_list):
        line = line.strip()
        if not line.startswith("move"):
            line = line.replace("[", "").replace("]", "").split(" ")
            for i, ch in enumerate(line):
                if ch != "9":
                    stacks_part1[i].insert(0, ch)
                    stacks_part2[i].insert(0, ch)
        else:
            no_of_moves, from_stack, to_stack = re.findall(r"\d+", line)
            temp_stack = []
            for n in range(int(no_of_moves)):
                stacks_part1[int(to_stack) - 1].append(stacks_part1[int(from_stack) - 1].pop())
                temp_stack.insert(0, stacks_part2[int(from_stack) - 1].pop())

            stacks_part2[int(to_stack) - 1].extend(temp_stack)

    output1 = []
    output2 = []
    for stack in stacks_part1:
        output1.append(stack.pop())
    print("".join(output1))
    for stack in stacks_part2:
        output2.append(stack.pop())
    print("".join(output2))