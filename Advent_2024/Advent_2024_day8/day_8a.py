file_path = "input2024_8.txt"

char_pos = {}
unique_antinodes = set()
    
with open(file_path, "r") as file:
    #map_input for finding valid_antinodes, char_pos for valid antenna
    map_input = [list(line.strip()) for line in file]
    for y, row in enumerate(map_input):
        for x, char in enumerate(row):
            if char != '.':
                char_pos.setdefault(char, set()).add((y,x))

def valid_pos(pos):
    return 0 <= pos[0] < len(map_input) and 0 <= pos[1] < len(map_input[0])

for char, pos in char_pos.items():
    for i, pos1 in enumerate(pos):
        for j, pos2 in enumerate(pos):
            if i != j:
                distance = (pos1[0] - pos2[0], pos1[1] - pos2[1])
                antinode1 = tuple(a + b for a, b in zip(pos1, distance))
                antinode2 = tuple(a - b for a, b in zip(pos2, distance))
                if valid_pos(antinode1):
                    unique_antinodes.add(antinode1)
                if valid_pos(antinode2):
                    unique_antinodes.add(antinode2)

print(len(unique_antinodes))
#Correct Answer: 305