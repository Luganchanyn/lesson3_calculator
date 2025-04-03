def move_last_to_first(lst):
    if len(lst) > 1:
        return [lst[-1]] + lst[:-1]
    return lst

print(move_last_to_first([44, 38, 45, 15, 65, 999, 1997]))  # [1997, 44, 38, 45, 15, 65, 999]
print(move_last_to_first([7]))             # [7]
print(move_last_to_first([]))              # []
print(move_last_to_first([127, 33, 49, 14, 88]))  # [88, 127, 33, 49, 14]
