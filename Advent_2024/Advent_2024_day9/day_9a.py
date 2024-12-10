file_name = "input2024_9.txt"

def calc_solution(disk_file):
    solution = 0
    for index, file_id in enumerate(disk_file):
        if file_id != 0:
            solution += index * (file_id - 1)
    return solution

disk_file = []
with open(file_name, "r") as file:
    for index, char in enumerate(file.read()):
        for _ in range(int(char)):
            if index%2 == 0:
                disk_file.append(int(index/2) + 1)
            else:
                disk_file.append(0)

for index, i in enumerate(disk_file[::-1]):
    if i != 0:
        num_index = len(disk_file) - 1 - index
        zero_index = disk_file.index(0)
        if zero_index < num_index:
            disk_file[zero_index], disk_file[num_index] = disk_file[num_index], disk_file[zero_index]
        else:
            break

print(calc_solution(disk_file))
#Correct Answer: 6340197768906