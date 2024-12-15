import re

file_name = "input2024_14.txt"

#Grid size
x_len = 101
y_len = 103
guards = dict()  # x, y, move_x, move_y

with open(file_name, "r") as file:
    for y, line in enumerate(file):
        guard = tuple(int(num) for num in re.findall(r'-?\d+', line))
        guards[y] = guard

for i in range(100):
    for guard, stats in guards.items():
        x, y, mov_x, mov_y = stats
        new_stats = ((x + mov_x) % x_len, (y + mov_y) % y_len, mov_x, mov_y)
        guards[guard] = new_stats
 
top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0
    
for guard in guards.values():
    x, y = guard[0], guard[1]
    if x < (x_len - 1)/2 and y < (y_len - 1)/2:
        top_left += 1
    if x < (x_len - 1)/2 and y > (y_len - 1)/2:
        bottom_left += 1
    if x > (x_len - 1)/2 and y < (y_len - 1)/2:
        top_right += 1
    if x > (x_len - 1)/2 and y > (y_len - 1)/2:
        bottom_right += 1
print(top_left * top_right * bottom_left * bottom_right)
#Correct Answer: 229839456