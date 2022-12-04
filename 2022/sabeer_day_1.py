sum_of_calories: list = []
sum_of_one_elf: int = 0

with open("/home/sabeer-ss/Downloads/input-day1.txt", "r") as f:
    contents = f.readlines()
    for calorie in contents:
        calorie = calorie.strip()
        if calorie == "":
            sum_of_calories.append(sum_of_one_elf)
            sum_of_one_elf = 0
        else:
            sum_of_one_elf += int(calorie)
# part1 Answer -
print(max(sum_of_calories))
# part2 Answer -
print(sum(sorted(sum_of_calories)[-3:]))

