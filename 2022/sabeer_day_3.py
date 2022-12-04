import string
from itertools import islice

list_of_rucksacks = []
priority_dict = {}
priority_sum = 0

with open("/home/sabeer-ss/Downloads/input-day3.txt", "r") as f:
    input_list = f.readlines()
    for item in input_list:
        list_of_rucksacks.append(item.strip())

for idx, ch in enumerate(string.ascii_lowercase):
    priority_dict[ch] = idx + 1

for idx, ch in enumerate(string.ascii_uppercase):
    priority_dict[ch] = idx + 27

for item in list_of_rucksacks:
    first = item[:len(item) // 2]
    second = item[len(item) // 2:]
    for i in range(len(first)):
        if first[i] in second:
            priority_sum += priority_dict[first[i]]
            break

print(priority_sum)

# ------------------Part2--------------------
# 2790
priority_sum_part2 = 0

for idx in range(len(list_of_rucksacks)//3):
    each_grp = list(islice(list_of_rucksacks, (idx * 3), (idx + 1) * 3))
    for i in range(len(each_grp[0])):
        if each_grp[0][i] in each_grp[1] and each_grp[0][i] in each_grp[2]:
            priority_sum_part2 += priority_dict[each_grp[0][i]]
            break

print(priority_sum_part2)