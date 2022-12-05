fully_contains_sum = 0
overlaps_sum = 0

with open("/home/sabeer-ss/Downloads/input-day4.txt", "r") as f:
    input_list = f.readlines()
    for item in input_list:
        assignment = item.strip().split(",")
        section1_start = int(assignment[0].split("-")[0])
        section1_end = int(assignment[0].split("-")[1])
        section2_start = int(assignment[1].split("-")[0])
        section2_end = int(assignment[1].split("-")[1])
        if (
            (section2_start >= section1_start and section2_end <= section1_end) or
            (section1_start >= section2_start and section1_end <= section2_end)
        ):
            fully_contains_sum += 1

        if section1_start <= section2_end and section2_start <= section1_end:
            overlaps_sum += 1

print(fully_contains_sum)
print(overlaps_sum)
