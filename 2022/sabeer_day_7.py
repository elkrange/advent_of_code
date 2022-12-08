import operator
from collections import defaultdict
total_space = 70000000
space_needed = 30000000
path = []
results = defaultdict(int)

with open("/home/sabeer-ss/Downloads/input-day7.txt", "r") as f:
    input_list = [item.strip() for item in f.readlines()]

for line in input_list:
    line_inputs = line.split()
    if line_inputs[1] == "cd":
        if line_inputs[2] == "..":
            path.pop()
        else:
            path.append(line_inputs[2])
    elif line_inputs[0][0].isnumeric():
        for i in range(len(path)+1):
            results["/".join(path[:i])] += int(line_inputs[0])

output = 0
for k, v in results.items():
    if v <= 100000:
        output += v
print(output)

# ---Part2
remaining_space = total_space - results[""]
shortage = space_needed - remaining_space
sorted_results = sorted(results.items(), key=operator.itemgetter(1))
for k, v in sorted_results:
    if v > shortage:
        print(v)
        break
# 1444896
# 404395