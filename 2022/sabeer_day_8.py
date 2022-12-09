s = 0
with open("/home/sabeer-ss/Downloads/input-day8.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

for idx1, line in enumerate(lines):
    if idx1 == 0 or idx1 == len(lines) - 1:
        s += len(line)
    else:
        for idx2, num in enumerate(line):
            if idx2 == 0 or idx2 == len(line) - 1:
                s += 1
            else:
                visible1 = True
                visible2 = True
                visible3 = True
                visible4 = True
                for i, nearby_num in enumerate(line[idx2+1: len(line)]):
                    if int(nearby_num) >= int(num):
                        visible1 = False
                for i, nearby_num in enumerate(line[0: idx2]):
                    if int(nearby_num) >= int(num):
                        visible2 = False
                for i in range(idx1 +1, len(lines)):
                    if int(lines[i][idx2]) >= int(num):
                        visible3 = False
                for i in range(0, idx1):
                    if int(lines[i][idx2]) >= int(num):
                        visible4 = False
                if visible1 or visible2 or visible3 or visible4:
                    s += 1
print(s)
#1546
#-------------Part2 ------------

scores = []
for idx1, line in enumerate(lines):
    for idx2, num in enumerate(line):
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        for i, nearby_num in enumerate(line[idx2+1: len(line)]):
            cnt1 += 1
            if int(nearby_num) >= int(num):
                break
        for i, nearby_num in enumerate(reversed(line[0: idx2])):
            cnt2 += 1
            if int(nearby_num) >= int(num):
                break
        for i in range(idx1 +1, len(lines)):
            cnt3 += 1
            if int(lines[i][idx2]) >= int(num):
                break
        for i in range(idx1-1, -1, -1):
            cnt4 += 1
            if int(lines[i][idx2]) >= int(num):
                break
        scores.append(cnt1 * cnt2 * cnt3 * cnt4)
print(max(scores))
# 519064
