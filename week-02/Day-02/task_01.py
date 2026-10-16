students = {
    "Ada": 78,
    "Chidi": 45,
    "Fatima": 92,
    "Emeka": 58,
    "Zara": 33
}

def score_sort(scores: dict):
    sorted_dict = dict()

    for _ in scores:
        if scores[_] >= 50:
            sorted_dict[_] = scores[_]
    return sorted_dict

print(score_sort(students))
