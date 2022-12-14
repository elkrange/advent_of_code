f = open("/home/sabeer-ss/Downloads/input-day9.txt", "r")
lines = [line.strip() for line in f.readlines()]

head_position = (50, 50)
tail_position = [(50, 50) for i in range(9)]

tail_total = set()
tail_total.add(tail_position[8])


def move_all_tails():
    tail_position[0] = move_tail(head_position, tail_position[0])
    for i in range(1, 9):
        tail_position[i] = move_tail(tail_position[i - 1], tail_position[i])
    tail_total.add(tail_position[8])


def move_tail(head, tail):
    if (
        (abs(tail[0] - head[0]) > 1) or
        (abs(tail[1] - head[1]) > 1)
    ): # tail is not around
        if tail[0] == head[0]:  # same row
            if tail[1] < head[1]:
                tail = (tail[0], tail[1] + 1)
            else:
                tail = (tail[0], tail[1] - 1)
        elif tail[1] == head[1]:  # same column
            if tail[0] < head[0]:
                tail = (tail[0] + 1, tail[1])
            else:
                tail = (tail[0] - 1, tail[1])
        else:
            if tail[1] < head[1]:
                tail = (tail[0], tail[1] + 1)
            else:
                tail = (tail[0], tail[1] - 1)
            if tail[0] < head[0]:
                tail = (tail[0] + 1, tail[1])
            else:
                tail = (tail[0] - 1, tail[1])
    return tail


for line in lines:
    if line.split()[0] == "R":
        for i in range(int(line.split()[1])):
            head_position = (head_position[0], head_position[1] + 1)
            move_all_tails()

    if line.split()[0] == "L":
        for i in range(int(line.split()[1])):
            head_position = (head_position[0], head_position[1] - 1)
            move_all_tails()

    if line.split()[0] == "D":
        for i in range(int(line.split()[1])):
            head_position = (head_position[0] + 1, head_position[1])
            move_all_tails()

    if line.split()[0] == "U":
        for i in range(int(line.split()[1])):
            head_position = (head_position[0] - 1, head_position[1])
            move_all_tails()

print(len(set(tail_total)))
#6081