#Both parts included in one file as only change is number of iterations
file_path = "input2024_11.txt"

stones = {}
stones_part2 = {}

with open(file_path, "r") as file:
    numbers = file.read().split()
    for i in numbers:
        key = int(i)
        if key in stones:
            stones[key] += 1
            stones_part2[key] += 1
        else:
            stones[key] = 1
            stones_part2[key] = 1

def blink(stones):
    new_stones = {}
    for key, value in stones.items():
        if len(str(key)) % 2 == 0:
            keystr = str(key)
            new_stone_1 = int(keystr[:len(keystr)//2])
            new_stone_2 = int(keystr[len(keystr)//2:])
            new_stone_vals = (new_stone_1, new_stone_2)
        elif key == 0:
            new_stone_vals = (1,)
        else:
            new_stone_vals = (int(key) * 2024,)
        for new_key in new_stone_vals:
            if new_key in new_stones:
                new_stones[new_key] += value
            else:
                new_stones[new_key] = value
    return new_stones

def count_stones(stones):
    num_stones = 0
    for value in stones.values():
        num_stones += value
    return num_stones

##Part 1
for i in range(25):
    stones = blink(stones)
print(f"Part 1: {count_stones(stones)}")
#Correct Answer: 233875

##Part 2
for i in range(75):
    stones_part2 = blink(stones_part2)
print(f"Part 2: {count_stones(stones_part2)}")
#Correct Answer: 277444936413293