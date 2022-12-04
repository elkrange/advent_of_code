"""
A, X - Rock
B, Y - Paper
C, Z - Scissors
"""
scores_total: int = 0
scores_selected = {"X": 1, "Y": 2, "Z": 3}
scores_outcome = {"WIN": 6, "DRAW": 3, "LOOSE": 0}

win_scenarios = [("C", "X"), ("B", "Z"), ("A", "Y")]
draw_scenarios = [("A", "X"), ("B", "Y"), ("C", "Z")]
loose_scenarios = [("A", "Z"), ("C", "Y"), ("B", "X")]

with open("/home/sabeer-ss/Downloads/input-day2.txt", "r") as f:
    input_list = f.readlines()
    for item in input_list:
        item = tuple(item.strip().split())
        if item in win_scenarios:
            scores_total += scores_outcome["WIN"] + scores_selected[item[1]]
        elif item in draw_scenarios:
            scores_total += scores_outcome["DRAW"] + scores_selected[item[1]]
        elif item in loose_scenarios:
            scores_total += scores_outcome["LOOSE"] + scores_selected[item[1]]

print(scores_total)

# ------------Part2------------------

win_scenarios = {"C": "X", "B": "Z", "A": "Y"}
draw_scenarios = {"A": "X", "B": "Y", "C": "Z"}
loose_scenarios = {"A": "Z", "C": "Y", "B": "X"}

scores_total = 0
with open("/home/sabeer-ss/Downloads/input-day2.txt", "r") as f:
    input_list = f.readlines()
    for item in input_list:
        item = tuple(item.strip().split())
        if item[1] == "Z":
            scores_total += scores_outcome["WIN"] + scores_selected[win_scenarios[item[0]]]
        elif item[1] == "Y":
            scores_total += scores_outcome["DRAW"] + scores_selected[draw_scenarios[item[0]]]
        elif item[1] == "X":
            scores_total += scores_outcome["LOOSE"] + scores_selected[loose_scenarios[item[0]]]

print(scores_total)
