marker_position = 4  # or 14 for part2
with open("/home/sabeer-ss/Downloads/input-day6.txt", "r") as f:
    input_list = f.readlines()
    input_str = input_list[0].strip()
    for idx, i in enumerate(input_str):
        marker = input_str[idx: idx + marker_position]
        if len(set(marker)) == len(marker):
            print(len(set(marker)) + idx)
            break
